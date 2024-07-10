from fastapi import Depends, FastAPI
from deps.authentication import authenticate
from routes.scrape import router as scrape_router
from routes.products import router as products_router

server = FastAPI(docs=True, dependencies=[Depends(authenticate)])
server.include_router(scrape_router, prefix="/scrape", tags=["scrape"])
server.include_router(products_router, prefix="/products", tags=["products"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:server", host="0.0.0.0", port=8000, reload=True)

