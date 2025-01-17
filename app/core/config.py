from fastapi import FastAPI
from pydantic import BaseModel



class YearRequest(BaseModel):
    year: int

class StringRequest(BaseModel):
   string: str
   # TODO payload for each router should be designed here