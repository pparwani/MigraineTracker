# app/main.py

from fastapi import FastAPI
from dotenv import load_dotenv
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

# It's a good practice to load environment variables right at the start
load_dotenv()  # Specify the environment-specific file if needed

import os
from app.api.api_v1.endpoints import user, migraine_routes, auth
from app.db.mongodb_utils import MongoDB
from app.core.config import settings




async def lifespan(app: FastAPI):
    # Connect to MongoDB
    await MongoDB.connect(
        uri=settings.mongo_connection_string, 
        dbname=settings.mongo_db
    )
    print("Connected to MongoDB")
    
    yield  # The app runs at this point

    # Close MongoDB connection
    await MongoDB.close()
    print("Disconnected from MongoDB")
    
app = FastAPI(title=os.getenv('APP_NAME', 'Migraine Tracker'), lifespan=lifespan)
# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.backend_cors_origins,  # Use the parsed list of origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)
# Include routers
app.include_router(user.router, prefix="/api/v1/users", tags=["users"])
app.include_router(migraine_routes.router, prefix="/api/v1/migraines", tags=["migraines"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["authentication", "login"])

if __name__=="__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8080)
    
    #to debug docker run --mount type=bind,source=$(pwd),target=/code -p 8199:8199 -p 8080:8080 migrainetracker
    # % python3 -m debugpy --listen 8199 --wait-for-client app/main.py        