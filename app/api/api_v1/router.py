# api core module for all endpoints
import os
import shutil
from fastapi import APIRouter, UploadFile
from datetime import datetime
from .endpoints.chat import Chat
from .endpoints.upload_docs import DocumentUploader
from .schemas.Prompt import Prompt

router = APIRouter(
    prefix='/api/v1',
    responses = {
        404: {'description': 'Not Found'}
    }
)

@router.post('/chat')
async def answer_question(prompt: Prompt):
    chat = Chat(prompt.question)
    result = chat.ask_chat_model()

    return result

@router.post("/upload-docs/")
async def create_upload_docs(files: list[UploadFile]):
    now = datetime.now()
    # get unique subfolder name
    dt_string = now.strftime("%d%m%Y%H%M%S")
    sub_dir = f"docs/{dt_string}"

    upload_dir = os.path.join(os.getcwd(), sub_dir)
    # Create the upload directory if it doesn't exist
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    # get the destination path
    for file in files:
        dest = os.path.join(upload_dir, file.filename)
        print(dest)

    # copy the file contents
    for file in files:
        with open(dest, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    docs_uploader = DocumentUploader()

    # either use sub_dir or upload_dir
    result = docs_uploader(sub_dir)

    return result