from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.core.db import Base


class OrderItem(Base):
    order_id = Column(Integer, ForeignKey('order.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    quantity = Column(Integer)
    order = relationship('Order', back_populates='items', overlaps="orderitem")
    product = relationship('Product', back_populates='order_items', overlaps="orderitem")
    #order = relationship('Order', back_populates='items')
    #product = relationship('Product', back_populates='order_items')
