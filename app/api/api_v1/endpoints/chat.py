# module of an endpoint
import time
from ..services.question_answering import QuestionAnswering
from ....core.logging import logger


class Chat:
    def __init__(self, input):
        self._input = input
        self._question_answering = QuestionAnswering()

    def ask_chat_model(self):
        logger.info('get answer is on progress...')
        start = time.time()
        raw_result, status, error = self._question_answering(self._input)
        running_time = time.time() - start

        if status:
            result = self.formatter(raw_result)
            logger.info('get answer is finished!')

            return {"result": result, "status": status, "running_time": running_time, "error": error}

        else:
            logger.info('get answer is failed!')

            return {"result": '', "status": status, "running_time": running_time, "error": error}
    
    def formatter(self, raw_result):
        formatted_result = {
            "answer": raw_result['output_text'],
            "source_docs": raw_result['input_documents'],
        }
        

        return formatted_result