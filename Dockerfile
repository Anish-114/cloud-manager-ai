# 1. Base Image: Python ka slim version jo fast aur light hota hai
FROM python:3.9-slim

# 2. Metadata: Project aur Developer ki jankari
LABEL maintainer="Anish  Kanaujiya"
LABEL college="Bansal Institute of Engineering and Technology"

# 3. Environment Variables: Python output ko turant terminal par dikhane ke liye
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# --- CRITICAL: CACHE BUSTER ---
# Is line ko badalne se Hugging Face purana 1555 servers wala data clear kar dega
ENV REFRESH_DATE="2026-03-26_v2"

# 4. Working directory set karein
WORKDIR /app

# 5. Requirements copy aur install karein (Optimization ke liye pehle requirements)
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 6. Ab baaki saara code copy karein (env, tasks, inference.py, etc.)
COPY . .

# 7. Dashboard Port (Hugging Face default port)
EXPOSE 7860

# 8. Application start command
# Jab container chalega, toh ye AI Agent aur Dashboard shuru kar dega
CMD ["python", "inference.py"]
