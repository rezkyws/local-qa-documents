import uvicorn
from fastapi import FastAPI
from app.api.api_v1.router import router


API_VERSION = 1.0
app = FastAPI()
app.include_router(router)

# Default root path
@app.get('/')
async def root():

    message = {
        'message': f'This is [your api name] API v{API_VERSION}'
    }

    return message