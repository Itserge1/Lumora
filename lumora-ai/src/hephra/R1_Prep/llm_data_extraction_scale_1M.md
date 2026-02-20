For **1 million PDFs**, you need a production-grade distributed system. Here's a comprehensive architecture:

# **Architecture to process 1 million PDF**
---

## **Architecture Overview**

```
PDF URLs → Message Queue → Worker Pool → Database → Results
           (RabbitMQ/SQS)  (100s workers)  (PostgreSQL)
```

---

## **1. Cloud-Based Distributed System (Recommended)**

### **Option A: AWS-based Solution**

```python
# architecture.py
"""
Components:
- S3: Store PDFs and results
- SQS: Message queue for PDF processing jobs
- Lambda/ECS: Workers for processing
- DynamoDB/RDS: Store results
- CloudWatch: Monitoring
"""

import boto3
import json
from concurrent.futures import ThreadPoolExecutor

class PDFProcessor:
    def __init__(self):
        self.s3 = boto3.client('s3')
        self.sqs = boto3.client('sqs')
        self.dynamodb = boto3.resource('dynamodb')
        self.queue_url = 'your-sqs-queue-url'
        self.table = self.dynamodb.Table('pdf_results')
    
    def submit_jobs(self, pdf_list):
        """Submit 1M jobs to SQS in batches"""
        batch_size = 10  # SQS batch limit
        
        for i in range(0, len(pdf_list), batch_size):
            batch = pdf_list[i:i + batch_size]
            entries = [
                {
                    'Id': str(idx),
                    'MessageBody': json.dumps({
                        'file_name': fn,
                        'file_url': url
                    })
                }
                for idx, (fn, url) in enumerate(batch)
            ]
            
            self.sqs.send_message_batch(
                QueueUrl=self.queue_url,
                Entries=entries
            )
            
            if i % 10000 == 0:
                print(f"Submitted {i} jobs...")
    
    def process_message(self, message):
        """Worker function - runs on Lambda/ECS"""
        body = json.loads(message['Body'])
        file_name = body['file_name']
        file_url = body['file_url']
        
        try:
            # Process PDF
            result = get_data(file_name, file_url)
            
            # Store in DynamoDB
            self.table.put_item(
                Item={
                    'file_name': file_name,
                    'file_url': file_url,
                    'result': json.dumps(result),
                    'status': 'completed',
                    'timestamp': int(time.time())
                }
            )
            
            # Delete message from queue
            self.sqs.delete_message(
                QueueUrl=self.queue_url,
                ReceiptHandle=message['ReceiptHandle']
            )
            
        except Exception as e:
            # Log error and potentially move to DLQ
            print(f"Error processing {file_name}: {e}")
            raise

# Lambda handler
def lambda_handler(event, context):
    processor = PDFProcessor()
    
    for record in event['Records']:
        processor.process_message(record)
    
    return {'statusCode': 200}
```

**AWS Lambda Configuration:**
```yaml
# lambda_config.yaml
FunctionName: pdf-processor
Runtime: python3.11
Timeout: 900  # 15 minutes
MemorySize: 3008  # Max for Lambda
ReservedConcurrentExecutions: 1000  # Process 1000 PDFs simultaneously

# SQS Configuration
QueueName: pdf-processing-queue
VisibilityTimeout: 900
MessageRetentionPeriod: 1209600  # 14 days
```

---

### **Option B: Kubernetes + Celery (More Control)**

```python
# worker.py
from celery import Celery
import redis
from kombu import Queue

# Configure Celery with Redis/RabbitMQ
app = Celery(
    'pdf_processor',
    broker='redis://redis-cluster:6379/0',
    backend='redis://redis-cluster:6379/1'
)

app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
    task_acks_late=True,
    worker_prefetch_multiplier=1,
    task_reject_on_worker_lost=True,
)

@app.task(bind=True, max_retries=3, rate_limit='100/m')
def process_pdf(self, file_name, file_url):
    try:
        result = get_data(file_name, file_url)
        
        # Store in PostgreSQL
        store_result(file_name, file_url, result)
        
        return {'status': 'success', 'file_name': file_name}
    
    except Exception as e:
        # Exponential backoff retry
        self.retry(exc=e, countdown=2 ** self.request.retries)

# producer.py
def submit_million_pdfs(pdf_list):
    """Submit 1M tasks efficiently"""
    from celery import group
    
    # Process in chunks
    chunk_size = 10000
    
    for i in range(0, len(pdf_list), chunk_size):
        chunk = pdf_list[i:i + chunk_size]
        
        # Create group of tasks
        job = group(
            process_pdf.s(fn, url) 
            for fn, url in chunk
        )
        
        # Submit asynchronously
        result = job.apply_async()
        
        print(f"Submitted chunk {i//chunk_size + 1}")
        
        # Optional: wait for chunk completion
        # result.get(timeout=3600)

# kubernetes_deployment.yaml
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: celery-workers
spec:
  replicas: 100  # Scale to 100s of workers
  template:
    spec:
      containers:
      - name: celery-worker
        image: your-pdf-processor:latest
        command: ["celery", "-A", "worker", "worker", "--concurrency=4"]
        resources:
          requests:
            memory: "2Gi"
            cpu: "1"
          limits:
            memory: "4Gi"
            cpu: "2"
        env:
        - name: OPENAI_API_KEY
          valueFrom:
            secretKeyRef:
              name: openai-secret
              key: api-key
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: celery-worker-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: celery-workers
  minReplicas: 50
  maxReplicas: 500
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

---

## **2. Database Schema for 1M Records**

```python
# database.py
from sqlalchemy import create_engine, Column, String, JSON, DateTime, Integer, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class PDFResult(Base):
    __tablename__ = 'pdf_results'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    file_name = Column(String(255), nullable=False)
    file_url = Column(String(1000), nullable=False, unique=True)
    url_hash = Column(String(32), nullable=False, index=True)
    result = Column(JSON, nullable=True)
    status = Column(String(20), nullable=False, default='pending')  # pending, processing, completed, failed
    error_message = Column(String(1000), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    retry_count = Column(Integer, default=0)
    
    __table_args__ = (
        Index('idx_status_created', 'status', 'created_at'),
        Index('idx_url_hash', 'url_hash'),
    )

# PostgreSQL connection with connection pooling
engine = create_engine(
    'postgresql://user:password@localhost:5432/pdf_db',
    pool_size=20,
    max_overflow=40,
    pool_pre_ping=True
)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def store_result(file_name, file_url, result):
    session = Session()
    try:
        url_hash = hashlib.md5(file_url.encode()).hexdigest()
        
        pdf_result = session.query(PDFResult).filter_by(url_hash=url_hash).first()
        
        if pdf_result:
            pdf_result.result = result
            pdf_result.status = 'completed'
            pdf_result.updated_at = datetime.datetime.utcnow()
        else:
            pdf_result = PDFResult(
                file_name=file_name,
                file_url=file_url,
                url_hash=url_hash,
                result=result,
                status='completed'
            )
            session.add(pdf_result)
        
        session.commit()
    finally:
        session.close()
```

---

## **3. Cost Optimization Strategies**

```python
# batch_optimizer.py
class BatchOptimizer:
    """
    OpenAI Batch API: 50% cheaper, 24h turnaround
    Perfect for 1M PDFs if not time-sensitive
    """
    
    def create_batch_files(self, pdf_list, batch_size=50000):
        """Split into multiple batch files (max 50K per batch)"""
        batches = []
        
        for i in range(0, len(pdf_list), batch_size):
            batch = pdf_list[i:i + batch_size]
            filename = f"batch_{i//batch_size}.jsonl"
            
            with open(filename, 'w') as f:
                for idx, (file_name, file_url) in enumerate(batch):
                    pdf_text = get_text_from_pdf(file_url)
                    
                    request = {
                        "custom_id": f"{file_name}_{idx}",
                        "method": "POST",
                        "url": "/v1/chat/completions",
                        "body": {
                            "model": "gpt-4o-mini",
                            "temperature": 0,
                            "messages": [{
                                "role": "user",
                                "content": create_prompt(pdf_text)
                            }]
                        }
                    }
                    f.write(json.dumps(request) + '\n')
            
            batches.append(filename)
        
        return batches
    
    def submit_all_batches(self, batch_files):
        """Submit all batch files"""
        batch_ids = []
        
        for batch_file in batch_files:
            # Upload file
            with open(batch_file, 'rb') as f:
                uploaded_file = client.files.create(file=f, purpose="batch")
            
            # Create batch
            batch = client.batches.create(
                input_file_id=uploaded_file.id,
                endpoint="/v1/chat/completions",
                completion_window="24h"
            )
            
            batch_ids.append(batch.id)
            print(f"Submitted batch {batch.id}")
        
        return batch_ids
    
    def monitor_batches(self, batch_ids):
        """Monitor batch completion"""
        import time
        
        while True:
            completed = 0
            for batch_id in batch_ids:
                batch = client.batches.retrieve(batch_id)
                
                if batch.status == 'completed':
                    completed += 1
                    # Download results
                    self.download_results(batch)
                elif batch.status == 'failed':
                    print(f"Batch {batch_id} failed")
            
            print(f"{completed}/{len(batch_ids)} batches completed")
            
            if completed == len(batch_ids):
                break
            
            time.sleep(300)  # Check every 5 minutes

# Cost estimate
"""
1M PDFs with gpt-4o-mini:
- Real-time API: ~$1000-2000 (depending on PDF size)
- Batch API (50% off): ~$500-1000
- Processing time: 24-48 hours for batch
"""
```

---

## **4. Monitoring & Progress Tracking**

```python
# monitoring.py
from prometheus_client import Counter, Histogram, Gauge
import time

# Metrics
pdfs_processed = Counter('pdfs_processed_total', 'Total PDFs processed')
pdfs_failed = Counter('pdfs_failed_total', 'Total PDFs failed')
processing_time = Histogram('pdf_processing_seconds', 'Time to process PDF')
queue_size = Gauge('queue_size', 'Current queue size')

class ProgressTracker:
    def __init__(self, total_pdfs):
        self.total = total_pdfs
        self.completed = 0
        self.failed = 0
        self.start_time = time.time()
    
    def update(self, success=True):
        if success:
            self.completed += 1
            pdfs_processed.inc()
        else:
            self.failed += 1
            pdfs_failed.inc()
        
        # Print progress
        if self.completed % 1000 == 0:
            self.print_stats()
    
    def print_stats(self):
        elapsed = time.time() - self.start_time
        rate = self.completed / elapsed if elapsed > 0 else 0
        remaining = (self.total - self.completed) / rate if rate > 0 else 0
        
        print(f"""
        Progress: {self.completed}/{self.total} ({self.completed/self.total*100:.2f}%)
        Failed: {self.failed}
        Rate: {rate:.2f} PDFs/second
        Elapsed: {elapsed/3600:.2f} hours
        Estimated remaining: {remaining/3600:.2f} hours
        """)

# dashboard.py - Simple web dashboard
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

@app.route('/stats')
def get_stats():
    conn = psycopg2.connect("dbname=pdf_db")
    cur = conn.cursor()
    
    cur.execute("""
        SELECT 
            status,
            COUNT(*) as count
        FROM pdf_results
        GROUP BY status
    """)
    
    stats = dict(cur.fetchall())
    conn.close()
    
    return jsonify(stats)

if __name__ == '__main__':
    app.run(port=5000)
```

---

## **5. Complete Production Setup**

```bash
# docker-compose.yml
version: '3.8'

services:
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
  
  postgres:
    image: postgres:15
    environment:
      POSTGRES_DB: pdf_db
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
  
  celery_worker:
    build: .
    command: celery -A worker worker --concurrency=4 --loglevel=info
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    depends_on:
      - redis
      - postgres
    deploy:
      replicas: 10  # Start with 10 workers
  
  flower:
    build: .
    command: celery -A worker flower
    ports:
      - "5555:5555"
    depends_on:
      - redis
  
  prometheus:
    image: prom/prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    ports:
      - "9090:9090"
  
  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"

volumes:
  redis_data:
  postgres_data:
```

---

## **Recommended Strategy for 1M PDFs:**

1. **Use OpenAI Batch API** (50% cost savings)
   - Split into 20 batches of 50K PDFs each
   - Total cost: ~$500-1000
   - Time: 24-48 hours

2. **If you need real-time processing:**
   - AWS Lambda with SQS (easiest)
   - Or Kubernetes + Celery (more control)
   - 500-1000 concurrent workers
   - Time: 2-10 hours depending on workers

3. **Infrastructure:**
   - PostgreSQL for results storage
   - Redis for queue/cache
   - S3 for PDF/result backups
   - CloudWatch/Prometheus for monitoring

4. **Estimated Costs:**
   - OpenAI API: $500-2000
   - AWS infrastructure: $50-200/day
   - Total: ~$1000-3000 for 1M PDFs

**Which approach fits your timeline and budget?**