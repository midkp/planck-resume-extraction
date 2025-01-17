from pydantic import BaseModel
 
class YearRequest(BaseModel):
    year: int

class StringRequest(BaseModel):
    string: str