import torch
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from ..load_models import models
from ....core.logging import logger
from .get_collection import CollectionGetter


PROMPT_TEMPLATE = """Don't use your existing knowledge to answer the question, only use the following pieces of context to answer the question. 
If the context doesn't provide information to answer the question, just say that you don't know, don't try to make up an answer. 
Keep the answer as concise as possible. 
You must answer the question in indonesian language. 
{context}
Question: {question}
Helpful Answer:"""

class ClearCache:
    def __enter__(self):
        torch.cuda.empty_cache()

    def __exit__(self, exc_type, exc_val, exc_tb):
        torch.cuda.empty_cache()

class QuestionAnswering:
    def __init__(self):
        self._qa_chain_prompt = PROMPT_TEMPLATE
        self._collection = CollectionGetter()

    def __call__(self, question, number_documents = 4):
        try:
            docs, status, error = self._collection.search_relevant_docs(query=question, total_sources=number_documents)
            if status:
                with ClearCache():
                    PROMPT = PromptTemplate(
                        template=self._qa_chain_prompt, input_variables=["context", "question"]
                    )
                    # PROMPT = PromptTemplate.from_template(prompt_template)
                    chain = load_qa_chain(models.llm_model, chain_type="stuff", prompt=PROMPT)
                    result = chain({"input_documents": docs, "question": question}, return_only_outputs=False)

                    return result, 1, None
            
            else:
                return None, 0, error
        
        except BaseException as e:
            logger.error("error while try to get the answer : ", e)

            return None, 0, e