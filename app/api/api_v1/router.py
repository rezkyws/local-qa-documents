# api core module for all endpoints
from fastapi import APIRouter
from .endpoints.endpoint_1 import ClassName
from .schemas.schema_1 import SchemaName

router = APIRouter(
    prefix='/api/v1',
    responses = {
        404: {'description': 'Not Found'}
    }
)

@router.post('/endpoint-name')
async def func_name(schema_name: SchemaName):
    class_name = ClassName(schema_name.field_name)
    result = class_name.get_inference()

    return result