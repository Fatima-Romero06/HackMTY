# Smart Wallet — Your Personal Finance Advisor

> **An optimizer-first debt coach that turns your budget into exact per-card payments, cutting interest, lowering utilization, and guiding smarter financial decisions every month.**

**Authors:** Hildegard Zerrweck, Cyrce Danae Salinas & Israel Booz Rodríguez

---

## Executive Summary

Smart Wallet addresses a critical problem in personal finance: deciding exactly how much to pay on each credit card to minimize interest and maintain healthy credit utilization. By combining mathematical optimization with AI-driven explanations, the system transforms complex financial planning into clear, actionable decisions.

---

## Rubric Breakdown

### 1. Originality (30%)

* **Substantiated Competitive Differentiation (10%)**: Unlike traditional budgeting apps that only track expenses, Smart Wallet is an *optimizer-first* debt coach. It mathematically calculates exact per-card payments and leverages LLMs to deliver personalized, plain-language guidance.
* **Identification of Market Gap (10%)**: Bridges the gap between complex financial calculations (APR rates, billing cycles, pay-no-interest thresholds, utilization limits) and the user's need for actionable monthly payment decisions.
* **Non-Trivial Solution (10%)**: Replaces basic static rules with a compound interest optimization engine (`cvxpy`). It dynamically solves for multiple constraints simultaneously: APR, total budget, liquidity preservation (30%), minimum payments, and credit score optimization (keeping card utilization $< 30\%$).

---

### 2. Technical Depth (25%)

* **Data Foundation (6%)**: Automatically ingests and parses statement fields (PDF/Image) including balances, limits, APRs, due dates, minimum payments, and installment thresholds. Supports synthetic account/transaction integration via the Capital One "Nessie" (`nessieisreal`) sandbox API.
* **Algorithmic Logic / Intelligence (9%)**: Evaluates debt reduction using compound interest functions. Integrates Google's Gemini API and Anthropic's Claude to translate numerical outputs into clear human advice.
* **System Design (5%)**: Modular architecture featuring:
  * **Backend**: Python (pandas, cvxpy) + FastAPI.
  * **Frontend**: Vite, TypeScript, and TailwindCSS.
  * **AI/LLMs**: Gemini API & Anthropic.
  * **Voice (Optional)**: ElevenLabs API for text-to-speech feedback.
* **Quality & Functional Demo (5%)**: Delivers a full end-to-end pipeline: secure login, statement parsing, data verification, real-time optimal plan generation, and interactive audio/text feedback.

---

### 3. Impact & Feasibility (25%)

* **Substantiated Business Model (10%)**: High-value consumer tool focused on direct financial savings. Helps users avoid compound interest traps and lowers total debt overhead as an automated advisor.
* **Market Size (TAM/SAM/SOM) (5%)**: Targets credit card holders managing multiple accounts, high utilization rates, or limited monthly liquidity seeking optimized payoff routes.
* **Regulatory & Operational Feasibility (5%)**: Enforces strict data segregation between public issuer data and user data. Ensures full encryption, backend environment isolation for API keys, and adherence to privacy best practices.
* **Adoption Strategy (Go-To-Market) (5%)**: Frictionless user onboarding: upload statements $\rightarrow$ verify data $\rightarrow$ receive instant, step-by-step payoff plans that save money from day one.

---

### 4. Design & Experience (20%)

* **Specific User Persona (7%)**: Designed for everyday credit card users balancing multiple debt lines and tight monthly budgets who need exact, stress-free instructions to pay off debt efficiently.
* **Structured User Journey Map (7%)**:
  1. **Authentication & Upload**: Upload credit card statements (PDF/Image).
  2. **Verification**: Confirm and adjust extracted balances, APRs, and due dates.
  3. **Optimization Setup**: Input total monthly budget and execute optimization engine.
  4. **Action & Guidance**: Review exact per-card payment amounts, calculated interest savings, and read/listen to AI financial advice.
* **Pitch (6%)**: Clear, high-impact value proposition: Converts financial anxiety into optimized execution by driving cycle interest down to zero whenever budget thresholds permit.

---

## Tech Stack Summary

| Layer | Technologies |
| :--- | :--- |
| **Backend** | Python, FastAPI, pandas, cvxpy |
| **Frontend** | Vite, TypeScript, TailwindCSS |
| **AI / LLM** | Gemini API, Anthropic (Claude) |
| **Voice / Speech** | ElevenLabs API |
| **Sandbox Data** | Capital One "Nessie" API (`nessieisreal`) |
