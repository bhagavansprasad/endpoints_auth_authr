from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from app.config import load_clients
from app.logging_config import setup_logging
from app.routers import auth, users
import logging

# Setup logging
setup_logging()

# Define the FastAPI app instance at the module level
app = FastAPI()

class ContentSecurityPolicyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        logging.debug("Applying Content-Security-Policy middleware")
        response = await call_next(request)
        response.headers["Content-Security-Policy"] = "upgrade-insecure-requests;"
        return response

app.add_middleware(ContentSecurityPolicyMiddleware)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Load client configurations
CONFIG_FILE = "app/config/clients.json"
clients = load_clients(CONFIG_FILE)

# Optional: Define a startup event to log clients or other initialization tasks
@app.on_event("startup")
async def startup_event():
    print(f"Loaded clients: {clients}")

# Include routers
app.include_router(auth.router)
app.include_router(users.router)
logging.debug("Debugging initialized")
