from pydantic import BaseModel
import json 


class ApiResponse(BaseModel):
    production_url : str
    search_text: str 
    source_website : str
