# Billy — Smart CRM & AI Assistant for Small Businesses

> **A smart CRM that combines powerful analytics, intuitive operational management, and a context-aware AI assistant designed to understand everyday business conversations.**

---

## Executive Summary

Billy bridges the gap between fragmented business tools (spreadsheets, manual tracking) and enterprise-grade intelligence. By combining structured operational data with a locally deployed conversational AI, Billy allows small business owners to manage sales, inventory, and analytics as naturally as talking to a teammate.

---

## Rubric Breakdown

### 1. Originality (30%)

* **Substantiated Competitive Differentiation (10%)**: Unlike static CRMs or basic spreadsheets that require manual entry and complex navigation, Billy introduces a conversational interface that converts everyday language and unstructured team chats into structured operational insights.
* **Identification of Market Gap (10%)**: Solves the fragmented tool landscape faced by small businesses—who often juggle disparate systems for inventory, sales, and financial tracking—by centralizing operations into one approachable platform.
* **Non-Trivial Solution (10%)**: Merges structured Relational Database Management (MySQL) with local Large Language Models (`LocalAI`/`Ollama`). Employs dynamic conversation pruning, real-time context management, and custom prompt engineering to keep the AI business-aware without incurring external API costs.

---

### 2. Technical Depth (25%)

* **Data Foundation (6%)**: Utilizes a structured MySQL database to manage real-time business data, sales records, customer interactions, inventory tracking, and analytical metrics.
* **Algorithmic Logic / Intelligence (9%)**: Leverages locally hosted LLMs (`LocalAI`/`Ollama`) configured for domain-specific text understanding, automated summarization, and contextual decision support.
* **System Design (5%)**: Multi-service microservices architecture:
  * **Frontend**: React + TypeScript + Tailwind CSS + shadcn/ui.
  * **Web API**: Node.js + Express + MySQL (data, session, and analytics management).
  * **AI API**: Independent service orchestrating local LLM inference and context retention.
* **Quality & Functional Demo (5%)**: Fully integrated end-to-end ecosystem demonstrating concurrent API synchronization, responsive dashboard analytics, and real-time conversational AI interactions.

---

### 3. Impact & Feasibility (25%)

* **Substantiated Business Model (10%)**: Democratizes enterprise-grade management technology for small businesses, drastically reducing operational overhead, manual data entry errors, and SaaS subscription fatigue.
* **Market Size (TAM/SAM/SOM) (5%)**: Targets small-to-medium enterprises (SMEs), local merchants, and non-technical business owners looking to modernize sales and inventory workflows.
* **Regulatory & Operational Feasibility (5%)**: High privacy and operational stability achieved through local AI deployment (`Ollama`/`LocalAI`), ensuring sensitive customer and financial data never leave the business's private infrastructure.
* **Adoption Strategy (Go-To-Market) (5%)**: Designed with an ultra-low learning curve, allowing non-technical teams to onboard instantly using an intuitive UI and natural language prompts.

---

### 4. Design & Experience (20%)

* **Specific User Persona (7%)**: Built explicitly for small business owners and managers who are non-technical, overloaded with manual processes, and need quick, actionable business insights without navigating complex software.
* **Structured User Journey Map (7%)**:
  1. **Centralized Overview**: Monitor real-time sales, inventory, and metrics via interactive dashboards.
  2. **Natural Interaction**: Ask the AI assistant questions about business trends, inventory status, or daily summary in plain text.
  3. **Data Synthesis**: The system processes the request, syncs backend metrics with LLM logic, and updates operational records.
  4. **Actionable Insights**: Receive instant, structured recommendations and summaries to drive daily decision-making.
* **Pitch (6%)**: High-impact value proposition: "Making small business management as intuitive, effortless, and powerful as talking to a teammate."

---

## Tech Stack Summary

| Layer | Technologies |
| :--- | :--- |
| **Frontend** | React, TypeScript, Tailwind CSS, shadcn/ui |
| **Backend Web API** | Node.js, Express, MySQL |
| **AI / Intelligence** | LocalAI, Ollama (Locally deployed LLMs) |
| **Architecture** | Decoupled Microservices / Multi-API Orchestration |
