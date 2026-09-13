<div align="center">

<img width="140" height="140" alt="image" src="https://github.com/user-attachments/assets/22507187-f45d-45b6-80e3-41f449ffe11d" />

# VerifiKa

</div>

<div align="center">

<strong>Track your finance. Control your transactions. Be safe at all time.</strong>

VerifiKa is a smart platform to detect risks and protect your cash flow with just one click.

</div>

---

## The problem


About 45% of SMEs in Mexico suffer financial fraud primarily in the areas of purchasing and payments to suppliers due to overbilling and fraudulent suppliers (KPGM, 2025). Operating with manual processes and without real-time monitoring of abnormal activity, these companies fail to detect these capital leaks in time, absorbing invisible financial losses that directly compromise their liquidity and reduce their chances of survival in their first five years. 

---

## Our solution

Approximately 45% of SMEs in Mexico suffer financial fraud due to overbilling and fraudulent suppliers (KPMG, 2025). Operating with processes that lack real-time monitoring of anomalous activities, these companies fail to detect these capital leaks in time, absorbing invisible financial losses that directly compromise their liquidity and reduce their chances of survival during their first five years. Who does an SME turn to when it loses money? Its bank.

---

## What makes us different

<strong>Substantiated Competitive Differentiation</strong>

1. VerifiKa serves as an intelligent cybersecurity extension within the bank's mobile app:

2. Heuristic Risk Engine: Evaluates transaction risk in real time based on timing, amounts, and frequency patterns.

3. Escrow Vault: Intercepts suspicious transactions and holds funds temporarily for review instead of triggering immediate, disruptive rejections.

4. Multi-Factor Authentication: Requires biometric confirmation and individual user access codes to authorize flagged movements.

5. Gemini AI Copilot & Shield Dashboard: Analyzes historical behavior, generates custom security reports, and gives SMEs direct control over rules and access levels.

---

## User Journey Map

VerifiKa creates a seamless interaction between commercial banks and SME users across five critical stages:


| Stage | Bank Action | SME Action | Pain Point Solved | Tech / AI Engine |
| :--- | :--- | :--- | :--- | :--- |
| **1. Acquisition** | Integrates White-Label API. | Activates Shield in app. | Eliminates 18-mo dev cycle. | REST API & Webhooks. |
| **2. Onboarding** | Deploys Security Plus. | Configures roles & Face ID. | 2-minute digital setup. | Gemini baseline model. |
| **3. Operations** | Monitors SPEI passively. | Executes daily payments. | Zero false-positive blocks. | Real-time heuristic scoring. |
| **4. Detection** | Ghost Escrow (Score ≥ 50). | Authorizes via Face ID. | 100% automated resolution. | Dynamic Risk Engine & Biometrics. |
| **5. Monetization**| Collects $15/mo net margin. | Reviews AI security reports.| Turns security into profit. | Adaptive fraud analytics. |


## Key Journey Highlights

* **For the Bank:** Transforms fraud protection from a costly operational burden (*OpEx*) into a net-income asset, automating 100% of incident resolutions without increasing support desk headcount.
* **For the SME:** Protects working capital in real time with zero-friction daily operations, ensuring flagged payments enter a temporary 24-hour review vault rather than facing flat, disruptive rejections.

---

## Core features


VerifiKa extends native commercial banking applications through four core integrated pillars:

| Feature Pillar | Description | SME Benefit | Bank Benefit |
| :--- | :--- | :--- | :--- |
| ** Native Integration** | Embedded white-label extension via RESTful APIs. | No third-party apps needed. | Fast 4-6 week integration without core changes. |
| ** Biometric Auth** | Device-native Face ID & dynamic 4-pin security. | Instant approval for flagged transfers. | Eliminates identity theft and credential leaks. |
| ** Gemini AI Engine** | Self-learning behavioral model tracking company budgets. | Audits operational leaks in real time. | Drastically reduces false-positive alerts. |
| ** Ghost Escrow Vault** | Real-time Risk Score (0-100) & 24h retention vault. | Immediate control over held funds. | 100% automated resolution; zero call-center burden. |


```mermaid
graph TD
    %% Node Styles
    classDef bank fill:#1e3a8a,stroke:#3b82f6,stroke-width:2px,color:#fff;
    classDef engine fill:#312e81,stroke:#6366f1,stroke-width:2px,color:#fff;
    classDef alert fill:#991b1b,stroke:#ef4444,stroke-width:2px,color:#fff;
    classDef success fill:#065f46,stroke:#10b981,stroke-width:2px,color:#fff;

    %% Main Flow
    A["📱 Banking App<br/>(SME Dashboard)"]:::bank --> B["SPEI Transfer"]:::bank
    B --> C["VerifiKa AI Engine<br/>(Risk Analysis)"]:::engine
    C --> D{"Risk Score"}:::engine

    %% Decision Branches
    D -- "Score < 50<br/>(Normal)" --> E["Successful Transaction"]:::success
    D -- "Score ≥ 50<br/>(Risk)" --> F["Ghost Escrow Vault<br/>(24h Pause)"]:::alert

    %% Authentication Process
    F --> G["Push Notification"]:::alert
    G --> H["Face ID / PIN"]:::bank
    H --> I{"SME Decision"}:::bank

    %% Final Outcome
    I -- "Approve" --> E
    I -- "Cancel" --> J["Funds Protected"]:::success
