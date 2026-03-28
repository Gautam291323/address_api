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

def update_address(db: Session, id: int, address_update):
    obj = db.query(models.Address).filter(models.Address.id == id).first()
    if obj:
        for key, value in address_update.dict(exclude_unset=True).items():
            setattr(obj, key, value)
        db.commit()
        db.refresh(obj)
    return obj