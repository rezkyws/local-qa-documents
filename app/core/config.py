import os
from dotenv import load_dotenv


CWD = os.getcwd()

load_dotenv(dotenv_path=f'{CWD}/.env')

EMBEDDING_MODEL_DEVICE = os.getenv('EMBEDDING_MODEL_DEVICE')
LLM_MODEL_DEVICE = os.getenv('LLM_MODEL_DEVICE')
APP_PORT = os.getenv('APP_PORT')
QDRANT_HOST = os.getenv('QDRANT_HOST')
QDRANT_PORT = os.getenv('QDRANT_PORT')
QDRANT_COLLECTION_NAME = os.getenv('QDRANT_COLLECTION_NAME')