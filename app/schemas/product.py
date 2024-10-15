from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    name: str = Field(..., max_length=50)
    description: Optional[str] = Field(max_length=300)
    price: Optional[int] = Field(default=0)
    quantity: Optional[int] = Field(default=0)

    class Config:
        min_anystr_length = 2


class ProductUpdate(ProductCreate):
    name: Optional[str] = Field(..., max_length=50)


class ProductDB(ProductCreate):
    id: int

    class Config:
        orm_mode = True