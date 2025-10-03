# What's Lumora

Lumora is a financial news summarizer that collects relevant news for different ticker symbols and provides concise
summaries, so you can quickly grasp the most important information.

In today’s fast-paced market, news is everywhere—but most of it is noise. Headlines are flashy, stories are long, and
the real insights are buried.

Some news could even explain sudden market movements, like your favorite stock jumping 7% in a single day.

Lumora cuts through the clutter, delivering only the news that truly matters—so you can act fast, stay informed, and
make smarter investment decisions.

**Lumora** Main goals is to Shine a light on the market’s most important news

## Sound Fun! Want to Join This Project?

I’m glad you’re interested! Shoot me a message on Instagram @realItserge with your GitHub's email, and I’ll send you an
invitation to join as a collaborator.


## Infrastructure Later for scaling
Exactly ✅ — in **AWS Organizations**, the **OU is just a container**.
The **real isolation** comes from **accounts**.

So yes — in a **production-grade setup**, you would actually **create separate accounts** for each concern:

## current Infrastructure

This is a design off a **lean but production-friendly AWS Org structure** for Lumora with **3 accounts**.


### 🏗️ AWS Organization Structure (Minimal Starter)

```
Root
├── Infrastructure OU
│   └── SharedServices Account
│       - AWS Client VPN
│       - ECR (Docker images for Lumora)
│       - CI/CD (CodePipeline, CodeBuild, or GitHub Actions runners)
│       - IAM Identity Center (SSO for team)
│
├── Workloads OU
│   ├── DevTest Account
│   │   - VPC (dev + test subnets)
│   │   - ECS/EKS cluster for Lumora Dev + Staging
│   │   - RDS (small/cheap instance for testing)
│   │   - CloudWatch logs/alarms for Dev
│   │
│   └── Prod Account
│       - VPC (prod subnets)
│       - ECS/EKS cluster for Lumora Prod
│       - RDS (multi-AZ, backups enabled)
│       - ALB for public access
│       - CloudWatch monitoring + alarms
│       - GuardDuty (enabled org-wide, reports back to this or SharedServices)
```

### 🔑 Key Points

* **OU separation**

    * `Infrastructure OU` → things shared across environments.
    * `Workloads OU` → environments (Dev/Test + Prod).

* **Accounts**

    * **SharedServices Account** → CI/CD pipeline, container registry, VPN/identity.
    * **DevTest Account** → all non-production workloads. Small/cheap RDS + ECS.
    * **Prod Account** → production-only. Tight IAM controls, multi-AZ DB, alarms.

* **IAM / Access Control**

    * Use **IAM Identity Center** in SharedServices.
    * Assign devs **full access** in DevTest, but **read-only / limited deploy rights** in Prod.

* **Security / Logging**

    * CloudTrail can be **org-wide** (logs delivered to SharedServices S3 bucket).
    * GuardDuty can be **org-wide** (findings forwarded to SharedServices or Prod).


### ⚖️ Why this works well

* Keeps **cost low** → only 3 accounts.
* Still gives you **proper separation** → Dev mistakes don’t kill Prod.
* Allows growth → later you can add:

    * `Security OU` with LogArchive/Security accounts.
    * Split `Dev` and `Staging` into separate accounts if needed.


✅ This is basically the **“startup to small team” best practice**. Enterprises take it further (6–10+ accounts), but for Lumora this is a clean starting point.



### 🏗️ AWS Organization Structure (Future Structure)

```
Root
├── Security OU
│   ├── Security Account       # GuardDuty, Security Hub, IAM Analyzer
│   ├── Log Archive Account    # All CloudTrail, Config, VPC Flow logs
│
├── Infrastructure OU
│   ├── Networking Account     # VPC, Transit Gateway, VPN
│   ├── Shared Services Account# ECR, CI/CD (CodePipeline, Jenkins, GitHub Actions runners)
│
├── Workloads OU
│   ├── Dev Account            # Lumora dev environment (ECS/EKS, RDS dev, S3 dev)
│   ├── Staging Account        # Pre-prod mirror of prod
│   ├── Prod Account           # Production workloads only
│
└── Sandbox OU
    ├── Dev1 Sandbox           # Personal playground
    ├── Dev2 Sandbox
```

---

## 🔑 Why separate accounts?

* **Blast radius**: If someone breaks Dev, Prod isn’t touched.
* **Security**: Prod has tighter SCPs, monitoring, MFA enforcement.
* **Billing**: Costs are separated per account, rolled up at Org level.
* **Access control**: Easy to give devs full rights in Dev but read-only in Prod.
* **Shared infra**: Networking/ECR/CI/CD accounts provide services to all workloads.

