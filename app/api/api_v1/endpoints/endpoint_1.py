# module of an endpoint
import time
from ..services.service_1 import ServiceOne
from ....core.logging import logger


class ClassName:
    def __init__(self, input):
        self._input = input

    def get_inference(self):
        logger.info('get something is on progress...')
        start = time.time()
        service_one = ServiceOne()
        raw_result, status, error = service_one.get_inference(self._input)
        running_time = time.time() - start

        if status:
            result = self.formatter(raw_result)
            logger.info('get something is finished!')

            return {"result": result, "status": status, "running_time": running_time, "error": error}

        else:
            logger.info('get something is failed!')

            return {"result": '', "status": status, "running_time": running_time, "error": error}
    
    def formatter(self, raw_result):
        formatted_result = {
            "label": raw_result[0],
            "confidence_score": raw_result[1],
        }
        

        return formatted_result