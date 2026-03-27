from pydantic import BaseModel

class AddressCreate(BaseModel):
    name: str
    phone: str
    address: str
    latitude: float
    longitude: float

class AddressOut(AddressCreate):
    id: int

    class Config:
        from_attributes = True