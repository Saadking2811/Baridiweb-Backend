from fastapi import FastAPI
from config.database import Base, engine  # Import the database setup
from routers.auth import authRouter  # Import the authentication routes
from routers.ocr import ocrRoute
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Create database tables (uncomment this line to create tables in the database)
Base.metadata.create_all(bind=engine)

# Include routes
# auth route

# Define the allowed origins
origins = [
    "http://localhost:3000",  # For local development with a React frontend
    "http://example.com",     # Add your frontend domain
    "https://example.com",    # For secure connections
    "*",                      # Allow all origins (not recommended for production)
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,              # Allow specific origins
    allow_credentials=True,             # Allow credentials (e.g., cookies)
    allow_methods=["*"],                # Allow all HTTP methods
    allow_headers=["*"],                # Allow all headers
)

app.include_router(authRouter, prefix="/auth")

# ocr route
app.include_router(ocrRoute, prefix="/ocr")
