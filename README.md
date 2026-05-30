# 📈 AlphaAgent — Multi-Agent Trading Web Application

[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Deployment - Render](https://img.shields.io/badge/Deploy-Render-46E3B7?style=flat-square&logo=render&logoColor=white)](https://render.com/)
[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)

**AlphaAgent** is a SaaS analytics platform for the financial market that implements a hierarchical, multi-agent AI architecture for technical analysis and automated investment decision-making. The system simulates an Investment Committee by dividing the cognitive load into specialized layers (Basic Analysis, Advanced Analysis, and Portfolio Management).
---

## 🔗 Project Links

* **GitHub Repository:** [multi-agent-trading-web-application-WebApp-](https://github.com/jwanxanqak/multi-agent-trading-web-application-WebApp-/tree/main)
* **Live Application (Frontend):** [AlphaAgent Web Dashboard](https://multi-agent-trading-web-application-c44n.onrender.com/)
* **Production Service (Backend API):** [AlphaAgent API Core](https://multi-agent-trading-web-application.onrender.com/)

---

## 🏗️ System Architecture and Agent Layers

The platform decentralizes the analytical workflow using three pre-processed logical entities in an optimized cache (`agent_cache.json`):

1. **Basic Analysis Agent:** Evaluates short-term trends (15-day windows), calculates average daily volatility ranges, and analyzes the correlation between price action and basic trading volume divergences.

2. **Advanced Analysis Agent:** Processes extended time windows and dynamically infers the behavior of standardized technical indicators such as simple moving averages (SMA_10, SMA_20) and the Relative Strength Index (RSI_14) to identify overbought or oversold zones.

3. **Portfolio Manager Agent (Consolidator):** Acts as the supervisory filter. It moderates analytical discrepancies between support agents and integrates corporate policies to issue a final unified recommendation (`BUY`, `HOLD`, `SELL`) with its due executive justification.
---

## ⚡ Key Features

* **Decoupled SaaS Architecture:** Backend built on a robust, asynchronous REST API with FastAPI, and a highly available, interactive frontend implemented with Streamlit.
* **Structured Technical Analysis:** Automated extraction of key metrics, detailed suggestions for generating charts (time series, volume histograms), and automated reports in JSON format.
* **Portfolio Monitoring Dashboard:** Dedicated frontend module for visually monitoring financial asset portfolio metrics (e.g., maximum exposure thresholds).
* **Interactive Chat Console:** Simulated interactive chat that allows you to dynamically query the technical criteria of the AI ​​agent committee for selected assets.

---

## 🛠️ Technology Stack

* **Backend:** Python 3.11, FastAPI, Pydantic v2 (Input data type validation).
* **Frontend:** Streamlit, Requests (Asynchronous consumption of microservices).
* **Analytics Persistence:** JSON structured cache optimized for eliminating token redundancies and inference latency.
* **DevOps / Infrastructure:** Render Blueprint Spec (render.yaml), Uvicorn (ASGI Web Server).
---

## 📁 Repository Structure

```text
├── agent_cache.json   # Structured knowledge base with pre-trained technical analyses.
├── app.py             # Interactive frontend built in Streamlit (Assets, Portfolio and Chat).
├── main.py            # Backend orchestrator (FastAPI Core) with signal routing and chat.
├── render.yaml        # Infrastructure as Code (IaC) for orchestrated cloud deployment.
└── requirements.txt   # Manifest of dependencies with versions set for production.

```  

## 🛠️ Local Setup and Installation Guide

Follow these detailed steps to clone, install, and run the complete **AlphaAgent** ecosystem in your local development environment using two separate terminals.

### 📋 Prerequisites
Ensure you have the following installed globally on your system:
* **Python 3.11** (or a stable version higher).

* **Git** for version control.

---
 

### Step 1: Clone the Repository
Open your terminal and download the project's source code:
```bash
git clone [https://github.com/jwanxanqak/multi-agent-trading-web-application-WebApp-.git](https://github.com/jwanxanqak/multi-agent-trading-web-application-WebApp-.git)
cd multi-agent-trading-web-application-WebApp-
```
### Step 2: Run the development backend
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
### Step 3: Run the development frontend
```bash
export BACKEND_URL="http://localhost:8000"
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
