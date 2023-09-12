from langchain.vectorstores import Qdrant
from ..load_models import models
from ....core.config import QDRANT_COLLECTION_NAME
from ....core.logging import logger
from ....core.qdrant import qdrant_client


class GetCollection:
    def __init__(self):
        self.vector_db = Qdrant(
                client=qdrant_client,
                collection_name=QDRANT_COLLECTION_NAME,
                embeddings=models.embedding_model
            )

    def get_docs_vector(self, query, total_sources):
        try:
            docs = self.vector_db.similarity_search(query, k=total_sources)

            return docs, 1, None
        
        except Exception as e:
            logger.error('error while getting source documents :', e, 'with input :', query)

            return '', 0, f'{e}'