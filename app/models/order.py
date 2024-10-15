from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship

from app.core.db import Base


class Order(Base):
    creation_date = Column(DateTime)
    status = Column(String(20), nullable=False)
    #items = relationship('OrderItem', cascade='delete')
    items = relationship('OrderItem', back_populates='order', overlaps="orderitem", cascade='delete')