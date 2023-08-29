# for load machine learning models
import os
from ...core.logging import logger


CWD = os.getcwd()

class Models:
    def __init__(self):
        self.the_model = self.load_models()

    def load_models(self):
        try:
            logger.info('load model is on progress...')
            model_folder = f'{CWD}/ml-models/model.pkl/'
            # do something to load your model here
            logger.info('load model is finished!')
            
            return model_folder

        except Exception as e:
            logger.error('error when load the model :', e)
            quit()
           
models = Models()