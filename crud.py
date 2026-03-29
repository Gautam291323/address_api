from sqlalchemy.orm import Session
import models

def create_address(db: Session, address):
    data = models.Address(**address.dict())
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

def get_all(db: Session):
    return db.query(models.Address).all()

def delete_address(db: Session, id: int):
    obj = db.query(models.Address).filter(models.Address.id == id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj

def update_address(db, id, address):
    obj = db.query(models.Address).filter(models.Address.id == id).first()
    if not obj:
        return None

    if address.name is not None:
        obj.name = address.name
    if address.phone is not None:
        obj.phone = address.phone
    if address.address is not None:
        obj.address = address.address

    db.commit()
    db.refresh(obj)
    return obj
