---
title: Cloud Manager AI Agent
emoji: 🚀
colorFrom: blue
colorTo: green
sdk: docker
sdk_version: "20.10.23"
python_version: "3.9"
app_port: 7860
pinned: false
license: mit
---

# 🚀 Autonomous Cloud Resource Manager (OpenEnv AI-Agent)

### **Submission for: OpenEnv Hackathon (Meta x Scaler x Hugging Face)**
**Developer:** Anish (Rochak) Kanaujiya  
**Project Goal:** To build a real-world Reinforcement Learning (RL) environment where an AI Agent autonomously manages cloud infrastructure scaling.

---

## 🌟 Project Overview
This project simulates a dynamic cloud environment. An AI Agent (powered by **Qwen-2.5-72B**) monitors real-time CPU Load and decides whether to **Scale Up** (add servers), **Scale Down** (remove idle servers), or stay **Stable**.

### **Key Innovation: Agentic Cloud Control**
Unlike traditional rule-based auto-scaling, this system uses a **Large Language Model (LLM)** as the core decision-maker, allowing for more nuanced resource management based on complex state observations.

---

## 🛠️ Technical Architecture
The project follows the strict **OpenEnv Standard API** (`step`, `reset`, `state`) to ensure compatibility with automated evaluation bots.

### **1. The Environment (OpenEnv Compliant)**
- **State Space:** CPU Load (%), Active Servers (1-10), Accumulated Cost, and System Health.
- **Action Space:** - `0`: Stable (Maintenance)
  - `1`: Scale Up (Add 1 node)
  - `2`: Scale Down (Remove 1 node)
- **Physics Engine:** Real-time traffic fluctuation simulation with cost-efficiency penalties.

### **2. AI Agent Logic**
- **Model:** Qwen-2.5-72B-Instruct (via Hugging Face Router).
- **Strategy:** The agent is prompted with real-time telemetry and must optimize for **95%+ Uptime** while minimizing **Operational Cost**.

---

## 📊 Compliance & Endpoints
This Space exposes mandatory REST endpoints for automated validation:
- `GET /tasks`: Lists the 3 scaling challenges (Easy, Medium, Hard).
- `POST /reset`: Forcefully resets the environment to the initial state (1 server).
- `GET /baseline`: Returns the baseline performance scores.
- `GET /grader`: Evaluates the agent's performance based on the last episode.

---

## 🚀 How to Run Locally
1. **Clone the repo:** `git clone <your-repo-link>`
2. **Build Docker:** `docker build -t cloud-manager-ai .`
3. **Run:** `docker run -p 7860:7860 cloud-manager-ai`

---

## 📈 Success Metrics
- **Cost Reduction:** Successfully reduced idle server time by ~30% in Medium-load tasks.
- **Stability:** Maintained 0% crash rate during 100-step "Spike Resilience" testing.

**Built with ❤️ for the OpenEnv Community.**
