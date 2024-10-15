"""Models to Alembic"""
from app.core.db import Base, SQLALCHEMY_DATABASE_URL # noqa
from app.models.product import Product # noqa
from app.models.order import Order # noqa
from app.models.orderitem import OrderItem # noqa
