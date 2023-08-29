# for pydantic model
from pydantic import BaseModel


class SchemaName(BaseModel):
    field_name: str