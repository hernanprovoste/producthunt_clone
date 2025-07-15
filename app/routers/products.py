from fastapi import APIRouter
from .. import schemas

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.post("/", response_model=schemas.ProductBase)
def create_product(product: schemas.ProductBase):
    return product