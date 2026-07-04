from pydantic import BaseModel
class ConflictRequest(BaseModel):
    data : str

class ConflictResponse(BaseModel):
    data : str