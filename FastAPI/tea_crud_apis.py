from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Tea(BaseModel):
    id:int
    name:str
    origin:str
    
teas : List[Tea] = []

# Sample data
teas.append(Tea(id=1, name="Green Tea", origin="China"))
teas.append(Tea(id=2, name="Earl Grey", origin="England"))

# Root endpoint
@app.get("/")
def read_root():
    return {"message" : "Welcome to chai code"}

# CRUD operations for Tea
# Get all teas
@app.get("/teas", response_model=List[Tea])
def get_teas():
    return teas

# Create a new tea
@app.post("/teas", response_model=Tea)
def create_tea(tea: Tea):
    teas.append(tea)
    return tea

# Update an existing tea
@app.put("/teas/{tea_id}", response_model=Tea)
def update_tea(tea_id: int, tea: Tea):
    for index, t in enumerate(teas):
        if t.id == tea_id:
            teas[index] = tea
            return tea
    return {"error": "Tea not found"}

# Delete a tea
@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    global teas
    teas = [t for t in teas if t.id != tea_id]
    return {"message": "Tea deleted successfully"}

# Get a specific tea by ID
@app.get("/teas/{tea_id}", response_model=Tea)
def get_tea(tea_id: int):
    for tea in teas:
        if tea.id == tea_id:
            return tea
    return {"error": "Tea not found"}