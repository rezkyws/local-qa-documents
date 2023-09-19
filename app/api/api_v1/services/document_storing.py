from langchain.document_loaders import DirectoryLoader, UnstructuredPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from ..load_models import models
from ..services.get_collection import CollectionGetter


class DocumentStoring:
    def __init__(self) -> None:
        pass

    def __call__(self, folder_name, collection_name):
        try:
            loader = DirectoryLoader(folder_name, glob="**/*.pdf", 
                            show_progress=True, 
                            use_multithreading=True,
                            loader_cls=UnstructuredPDFLoader)
        

            docs = loader.load()

            text_splitter = RecursiveCharacterTextSplitter(
                # Set a really small chunk size, just to show.
                chunk_size = 512,
                chunk_overlap  = 20,
                length_function = len,
                add_start_index = True,
            )

            all_splits = text_splitter.split_documents(docs)

            collection_getter = CollectionGetter()

            vector_db = collection_getter()

            vector_db.from_documents(
                all_splits,
                models.embedding_model,
                collection_name=collection_name,
            )

            return 1, None
        
        except BaseException as e:
            
            return 0, e