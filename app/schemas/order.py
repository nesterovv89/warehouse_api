from datetime import datetime
from enum import Enum, StrEnum
from typing import Optional

from pydantic import BaseModel, Field

from app.schemas.orderitem import OrderItem


class StatusChoice(StrEnum):
    CREATED = 'Создан'
    SEND = 'Отправлен'
    DELIVERED = 'Доставлен'


class OrderCreate(BaseModel):
    status: StatusChoice
    creation_date: datetime
    items: list[OrderItem]


class OrderUpdate(OrderCreate):
    status: Optional[StatusChoice]



class OrderDB(BaseModel):
    id: int
    status: StatusChoice
    creation_date: datetime
    

    class Config:
        orm_mode = True
