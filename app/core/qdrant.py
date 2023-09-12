from qdrant_client import QdrantClient
from .config import QDRANT_HOST, QDRANT_PORT


qdrant_client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)