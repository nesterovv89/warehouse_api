from pydantic import BaseModel



class OrderItem(BaseModel):
    quantity: int
    product_id: int
    
    


class OrderItemDB(OrderItem):
    id: int 

    class Config:
        orm_mode = True