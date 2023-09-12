# api core module for all endpoints
from fastapi import APIRouter
from .endpoints.chat import Chat
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