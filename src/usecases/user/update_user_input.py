from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Annotated
from datetime import date

class UpdateUserInput(BaseModel):
    name: Optional[Annotated[str, Field(min_length=1, max_length=100)]] = None
    email: Optional[EmailStr] = None
    password: Optional[Annotated[str, Field(min_length=6)]] = None
    phone: Optional[str] = None
    date_of_birth: Optional[date] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    zip_code: Optional[str] = None

    class Config:
        frozen = True
