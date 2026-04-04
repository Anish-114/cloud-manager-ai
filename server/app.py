import uvicorn
import sys
import os

# Root directory setup
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from inference import app

def main():
    """MANDATORY: Scaler Validator Entry Point"""
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
