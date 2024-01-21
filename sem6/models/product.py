from pydantic import BaseModel, Field


class ProductIn(BaseModel):
    title: str = Field(..., title='title', max_length=120)
    description: str = Field(default='', title='description', max_length=300)
    price: float = Field(..., title='price', gt=0, le=10_000)


class Product(ProductIn):
    prod_id: int

class OrderIn(BaseModel):
    user_id: int = Field(..., title='user_id')
    prod_id: int = Field(..., title='prod_id')
    date: datetime.date = Field(..., title='date')
    status: Status = Field(..., title='status')

    class Config:
        use_enum_values = True


class Order(OrderIn):
    order_id: int
    firstname: str
    lastname: str
    email: EmailStr
    title: str
    description: str
    price: float