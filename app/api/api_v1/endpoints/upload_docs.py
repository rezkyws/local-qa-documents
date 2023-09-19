import time
from ....core.logging import logger
from ....core.config import QDRANT_COLLECTION_NAME
from ..services.document_storing import DocumentStoring



class DocumentUploader:
    def __init__(self) -> None:
        pass

    def __call__(self, file_names):
        logger.info('storing files is on progress...')
        start = time.time()
        document_storing = DocumentStoring()
        status, error = document_storing(file_names, QDRANT_COLLECTION_NAME)
        running_time = time.time() - start

        if status:
            logger.info('storing files is finished!')

            return {"message": 'Storing docs is succeed', "status": 1, "running_time": running_time, "error": None}
        
        else:
            logger.error('storing files is failed : ', error)

            return {"message": 'Storing files is failed!', "status": 0, "running_time": running_time, "error": error}