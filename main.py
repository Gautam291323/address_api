from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# DB connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create
@app.post("/address/")
def create(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    return crud.create_address(db, address)

# Get all
@app.get("/address/")
def get_all(db: Session = Depends(get_db)):
    return crud.get_all(db)

# Delete
@app.delete("/address/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    res = crud.delete_address(db, id)
    if not res:
        raise HTTPException(status_code=404, detail="Not found")
    return {"message": "Deleted"}


@app.put("/address/{id}")
def update(id: int, address: schemas.AddressUpdate, db: Session = Depends(get_db)):
    res = crud.update_address(db, id, address)
    if not res:
        raise HTTPException(status_code=404, detail="Not found")
    return {"message": "Updated successfully"}
