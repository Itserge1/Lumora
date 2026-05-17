# What's Lumora

**Lumora** is an AI-powered financial intelligence platform designed to help investors cut through market noise and focus on what actually matters.

Every day, the market is flooded with headlines, opinions, earnings reports, economic updates, analyst reports, and breaking news. Most of it is overwhelming, time-consuming, or irrelevant. Important insights are often buried beneath long articles, sensational headlines, and endless streams of information.

Lumora solves this problem by collecting, analyzing, and simplifying financial information into clear, actionable intelligence. The platform tracks relevant news for specific ticker symbols, summarizes key developments using AI, and explains how those events may impact the market, sectors, or individual companies.

Instead of spending hours reading articles, monitoring social media, or analyzing reports manually, users can quickly understand the most important developments affecting a stock or the broader market in seconds.

The platform is built to help investors:

* Stay informed faster
* Understand why stocks move
* Discover meaningful market signals
* Monitor market-moving events in real time
* Reduce information overload
* Make smarter investment decisions with confidence

For example, if a stock suddenly jumps 7% in a single day, Lumora helps users instantly identify the catalyst behind the move — whether it’s earnings, breaking news, insider activity, analyst upgrades, macroeconomic events, or institutional buying.

---

# Core Features

## AI Financial News Summaries

Lumora gathers important news from across the financial world and transforms it into concise, high-signal summaries focused only on what matters most.

The AI filters out noise and highlights:

* Important developments
* Key market catalysts
* Company-specific events
* Sector trends
* Breaking financial news

Users can instantly understand the story behind the headlines without reading dozens of articles.

---

## “Why Is This Stock Moving?”

One of Lumora’s core experiences is explaining unusual stock movement in real time.

If a stock experiences major volatility, Lumora identifies:

* The likely catalyst
* Related news events
* Earnings reactions
* Analyst actions
* Economic reports
* Market sentiment shifts

This helps investors quickly understand market behavior and react faster.

---

## Fundamental & Technical Analysis

Users can explore both fundamental and technical insights for each stock, including:

### Fundamental Analysis

* Revenue growth
* Earnings performance
* Profit margins
* Valuation metrics
* Cash flow analysis
* Balance sheet strength
* Competitive positioning

### Technical Analysis

* Price action
* Trend analysis
* Support & resistance levels
* Volume analysis
* Momentum indicators
* Market sentiment

Lumora combines both perspectives to provide a more complete view of a company.

---

## AI Earnings Call Intelligence

Lumora automatically analyzes and summarizes earnings calls, highlighting:

* Key takeaways
* Revenue guidance
* Executive sentiment
* Risks and concerns
* Important quotes
* Analyst questions
* Bullish and bearish signals

Users can quickly understand what changed from previous quarters without listening to full earnings calls.

---

## AI-Powered Due Diligence

Lumora AI performs deep-dive analysis on companies by analyzing:

* Financial statements
* Earnings reports
* SEC filings
* Business fundamentals
* Industry positioning
* Competitive advantages
* Risk factors
* Management performance

The platform transforms complex financial data into readable insights, giving investors instant due diligence on any stock.

---

## Macro Economic Tracking

Lumora tracks major economic events and market-moving catalysts such as:

* CPI reports
* Federal Reserve meetings
* Interest rate decisions
* Elections
* GDP releases
* Employment reports
* Earnings seasons
* Geopolitical events

The platform explains how these events may impact sectors, stocks, and the overall market.

---

## Smart Market Alerts

Lumora delivers intelligent alerts beyond simple price notifications.

Examples include:

* Sudden insider buying
* Major institutional activity
* Unusual stock volatility
* Earnings surprises
* Breaking news
* Analyst upgrades or downgrades
* Important macroeconomic developments

Users receive high-signal alerts designed to surface meaningful opportunities and risks faster.

---

## Investor & Politician Portfolio Tracking

Lumora monitors trades and portfolio activity from influential investors and public figures, sending alerts when notable moves happen.

Examples include:

* Nancy Pelosi
* Chuck Schumer
* Warren Buffett

Users can track buying and selling activity to identify trends, monitor institutional sentiment, and discover potential investment opportunities.

---

## SEC Filing & Insider Activity Analysis

Lumora simplifies difficult financial filings and insider reports into understandable summaries.

The platform analyzes:

* 10-K filings
* 10-Q filings
* 8-K filings
* Insider transactions
* Institutional holdings
* Executive stock sales and purchases

This allows users to uncover insights hidden inside complex regulatory documents.

---

## Personalized AI Investment Feed

Every user receives a personalized experience based on:

* Watchlists
* Portfolio holdings
* Favorite sectors
* Trading behavior
* Market interests

Lumora continuously adapts to deliver the most relevant insights, news, and opportunities.

---

## Market Heatmaps & Trend Discovery

Lumora helps users visualize the market through:

* Sector heatmaps
* Trending stocks
* Market sentiment analysis
* Top gainers and losers
* Volume spikes
* Institutional flow tracking

This gives investors a fast overview of what is happening across the market in real time.

---

# Brand Vision

**Lumora’s mission is to shine a light on the market’s most important information.**

The platform is designed for modern investors who want clarity, speed, and actionable intelligence in a world overloaded with financial noise.

Rather than replacing investors, Lumora acts as an intelligent market copilot — helping users understand the market faster, discover opportunities earlier, and make more informed investment decisions with confidence.


## Sound Fun! Want to Join This Project?

I’m glad you’re interested! Shoot me a message on Instagram @realItserge with your GitHub's email, and I’ll send you an
invitation to join as a collaborator.

## Current Cloud Infrastructure

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

✅ This is basically the **“startup to small team” best practice**. Enterprises take it further (6–10+ accounts), but for
Lumora this is a clean starting point.

### 🏗️ AWS Organization Structure (Future Structure)

The structure bellow is how we plan to scale up our AWS cloud infrastructure later.

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

