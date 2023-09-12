# for load machine learning models
import os
from ...core.logging import logger
from transformers import AutoTokenizer, pipeline
from langchain.llms import HuggingFacePipeline
from auto_gptq import AutoGPTQForCausalLM
from langchain.embeddings import HuggingFaceEmbeddings
# from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from ...core.config import EMBEDDING_MODEL_DEVICE, LLM_MODEL_DEVICE


CWD = os.getcwd()

class Models:
    def __init__(self):
        self.embedding_model = self.load_embedding_models()
        self.llm_model = self.load_llm_models()

    def load_llm_models(self):
        try:
            logger.info('load llm model is on progress...')
            model_name_or_path = f'{CWD}/ml-models/TheBloke--Llama-2-13B-chat-GPTQ/'
            model_basename = "model"
            use_triton = False
            tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, use_fast=True)
            model = AutoGPTQForCausalLM.from_quantized(
                model_name_or_path,
                model_basename=model_basename,
                use_safetensors=True,
                trust_remote_code=True,
                device=LLM_MODEL_DEVICE,
                # streaming=True,
                # callbacks=[StreamingStdOutCallbackHandler()],
                use_triton=use_triton,
                quantize_config=None
            )

            transformer_pipeline = pipeline(
                "text-generation",
                model=model,
                tokenizer=tokenizer,
                max_new_tokens=512,
                temperature=0,
                top_p=0.95,
                repetition_penalty=1.15
            )

            llm = HuggingFacePipeline(pipeline=transformer_pipeline)
            
            logger.info('load llm model is finished!')
            
            return llm

        except Exception as e:
            logger.error('error when load llm model :', e)
            quit()

    def load_embedding_models(self):
        try:
            logger.info('load text embedding model is on progress...')
            model_name_or_path = f'{CWD}/ml-models/multilingual-e5-large/'
            # model_name = "intfloat/multilingual-e5-large"
            model_kwargs = {'device': EMBEDDING_MODEL_DEVICE}
            encode_kwargs = {'normalize_embeddings': False}
            encoder = HuggingFaceEmbeddings(
                model_name=model_name_or_path,
                model_kwargs=model_kwargs,
                encode_kwargs=encode_kwargs
            )
            logger.info('load text embedding model is finished!')
            
            return encoder

        except Exception as e:
            logger.error('error when load text embedding :', e)
            quit()
           
models = Models()