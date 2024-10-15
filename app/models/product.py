from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.core.db import Base


class Product(Base):
    name = Column(String(50), nullable=False)
    description = Column(Text)
    price = Column(Integer, nullable=False, default=0)
    quantity = Column(Integer, nullable=False, default=0)
    #orders = relationship('OrderItem', cascade='delete')
    order_items = relationship('OrderItem', back_populates='product', overlaps="orderitem", cascade='delete')
    