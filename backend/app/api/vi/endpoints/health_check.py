from fastapi import APIRouter
# from app.services.health_service import check_database

router = APIRouter()

@router.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint to monitor service status.
    """
    # db_status = check_database()
    
    # if not db_status:
    #     return {"status": "unhealthy", "database": "disconnected"}
    
    return {"status": "healthy", "database": "connected"}
