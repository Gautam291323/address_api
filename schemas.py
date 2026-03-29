from pydantic import BaseModel

class AddressCreate(BaseModel):
    name: str
    phone: str
    address: str

class AddressUpdate(BaseModel):
    name: str | None = None
    phone: str | None = None
    address: str | None = None
