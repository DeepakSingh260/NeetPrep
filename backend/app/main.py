from fastapi import FastAPI
from app.api.vi.endpoints import ocr,health_check
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(
    title="OCR Backend",
    description="Backend for OCR processing of uploaded PDFs",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all domains. Use specific domains in production.
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Include routes
app.include_router(ocr.router, prefix="/api/v1", tags=["OCR"])
app.include_router(health_check.router, prefix="/api/v1", tags=["health"])
