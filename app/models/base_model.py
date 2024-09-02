# app/models/base_model.py

from pydantic import BaseModel

class MongoModel(BaseModel):
    class Config:
        orm_mode = True
        anystr_strip_whitespace = True
        use_enum_values = True
        allow_population_by_field_name = True