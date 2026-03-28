from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, SessionLocal
import math

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

# Distance
def calc_distance(lat1, lon1, lat2, lon2):
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

# Nearby
@app.get("/nearby/")
def nearby(lat: float, lon: float, distance: float, db: Session = Depends(get_db)):
    data = crud.get_all(db)
    result = []

    for i in data:
        d = calc_distance(lat, lon, i.latitude, i.longitude)
        if d <= distance:
            result.append(i)

    return result

@app.put("/address/{id}")
def update(id: int, address: schemas.AddressUpdate, db: Session = Depends(get_db)):
    res = crud.update_address(db, id, address)
    if not res:
        raise HTTPException(status_code=404, detail="Not found")
    return res