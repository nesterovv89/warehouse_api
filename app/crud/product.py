from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.product import Product


class CRUDProduct(CRUDBase):

    async def get_product_id_by_name(
            self,
            product_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        db_product_id = await session.execute(
            select(Product.id).where(
                Product.name == product_name
            )
        )
        db_product_id = db_product_id.scalars().first()
        return db_product_id

product_crud = CRUDProduct(Product) 