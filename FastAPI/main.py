from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional, Annotated
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

# MongoDB connection from environment variable
MONGODB_URL = os.getenv("MONGODB_URI")
if not MONGODB_URL:
    raise ValueError("MONGODB_URI environment variable is required. Please set it in your .env file.")

DATABASE_NAME = os.getenv("DATABASE_NAME", "tea_database")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "teas")

client = AsyncIOMotorClient(MONGODB_URL)
database = client[DATABASE_NAME]
tea_collection = database[COLLECTION_NAME]

class Tea(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True
    )
    
    id: Optional[str] = Field(default=None, alias="_id")
    name: str
    origin: str

class TeaCreate(BaseModel):
    name: str
    origin: str

class TeaUpdate(BaseModel):
    name: Optional[str] = None
    origin: Optional[str] = None

# Root endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to chai code with MongoDB"}

# CRUD operations for Tea
# Get all teas
@app.get("/teas", response_model=List[Tea])
async def get_teas():
    teas = []
    async for tea_doc in tea_collection.find():
        tea_doc["_id"] = str(tea_doc["_id"])
        teas.append(Tea(**tea_doc))
    return teas

# Create a new tea
@app.post("/teas", response_model=Tea)
async def create_tea(tea: TeaCreate):
    tea_dict = tea.dict()
    result = await tea_collection.insert_one(tea_dict)
    created_tea = await tea_collection.find_one({"_id": result.inserted_id})
    created_tea["_id"] = str(created_tea["_id"])
    return Tea(**created_tea)

# Update an existing tea
@app.put("/teas/{tea_id}", response_model=Tea)
async def update_tea(tea_id: str, tea: TeaUpdate):
    if not ObjectId.is_valid(tea_id):
        raise HTTPException(status_code=400, detail="Invalid tea ID")
    
    update_data = {k: v for k, v in tea.dict().items() if v is not None}
    
    if not update_data:
        raise HTTPException(status_code=400, detail="No valid fields to update")
    
    result = await tea_collection.update_one(
        {"_id": ObjectId(tea_id)}, 
        {"$set": update_data}
    )
    
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Tea not found")
    
    updated_tea = await tea_collection.find_one({"_id": ObjectId(tea_id)})
    updated_tea["_id"] = str(updated_tea["_id"])
    return Tea(**updated_tea)

# Delete a tea
@app.delete("/teas/{tea_id}")
async def delete_tea(tea_id: str):
    if not ObjectId.is_valid(tea_id):
        raise HTTPException(status_code=400, detail="Invalid tea ID")
    
    result = await tea_collection.delete_one({"_id": ObjectId(tea_id)})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Tea not found")
    
    return {"message": "Tea deleted successfully"}

# Get a specific tea by ID
@app.get("/teas/{tea_id}", response_model=Tea)
async def get_tea(tea_id: str):
    if not ObjectId.is_valid(tea_id):
        raise HTTPException(status_code=400, detail="Invalid tea ID")
    
    tea = await tea_collection.find_one({"_id": ObjectId(tea_id)})
    
    if tea is None:
        raise HTTPException(status_code=404, detail="Tea not found")
    
    tea["_id"] = str(tea["_id"])
    return Tea(**tea)

# Get teas by origin
@app.get("/teas/origin/{origin}", response_model=List[Tea])
async def get_teas_by_origin(origin: str):
    teas = []
    async for tea_doc in tea_collection.find({"origin": origin}):
        tea_doc["_id"] = str(tea_doc["_id"])
        teas.append(Tea(**tea_doc))
    return teas
