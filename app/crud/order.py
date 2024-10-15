from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.crud.base import CRUDBase
from app.models.order import Order
from app.api.validators import check_quantity
from app.schemas.order import OrderCreate, OrderUpdate
from app.models.orderitem import OrderItem
import logging

   
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CRUDOrder(CRUDBase):
    async def create_order(self, db: AsyncSession, obj_in: OrderCreate) -> Order:
        db_obj = Order(
            creation_date=obj_in.creation_date,
            status=obj_in.status,
        )
        try:
            logger.info("Старт создания заказа")
            db.add(db_obj)
            for item in obj_in.items:
                db_order_item = OrderItem(
                    order_id=db_obj.id,
                    product_id=item.product_id,
                    quantity=item.quantity,
                )
                await check_quantity(db_order_item.product_id, db_order_item.quantity, db)
                db.add(db_order_item)
            await db.commit()
            await db.refresh(db_obj)
            return db_obj

        except Exception as e:
            logger.error("Ошибка при создании заказа: %s", e)
            await db.rollback()
            raise e
    

    async def get_order_items(self, db: AsyncSession, order_id: int):
        result = await db.execute(select(OrderItem).where(OrderItem.order_id == order_id))
        order_items = result.scalars().all()
        return order_items

    

order_crud = CRUDOrder(Order) 