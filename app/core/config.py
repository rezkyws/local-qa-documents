import os
from dotenv import load_dotenv

CWD = os.getcwd()

load_dotenv(dotenv_path=f'{CWD}/.env')

EMBEDDING_MODEL_DEVICE = os.getenv('EMBEDDING_MODEL_DEVICE')
LLM_MODEL_DEVICE = os.getenv('LLM_MODEL_DEVICE')
APP_PORT = os.getenv('APP_PORT')