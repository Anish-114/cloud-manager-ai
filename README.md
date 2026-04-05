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

# 🚀 Autonomous Cloud Resource Manager (OpenEnv AI)

**Developer:** Anish (Rochak) Kanaujiya  
**College:** Bansal Institute of Engineering and Technology (BIET)  
**Hackathon:** Meta x Scaler x Hugging Face

---

### 🔍 Project Architecture
This AI Agent is built to handle dynamic cloud scaling. It uses **Qwen-2.5-72B** to process real-time CPU telemetry and optimize server counts.

- **FastAPI Endpoints:** Fully compliant with `/tasks`, `/reset`, and `/grader`.
- **Logging:** Structured **START/STEP/END** logs are printed to `stdout` for real-time validation.
- **Root Files:** Repository includes `uv.lock`, `pyproject.toml`, and `server/app.py`.

### 🛠️ Technical Stack
- **Framework:** FastAPI & Gradio
- **Orchestration:** Docker (Hugging Face Spaces)
- **AI Logic:** OpenAI SDK with Qwen LLM
- **Package Manager:** `uv` (Fast & Efficient)

---
*Last Sync: April 5, 2026 - All systems operational.*
