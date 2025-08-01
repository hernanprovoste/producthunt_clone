from fastapi import FastAPI
from .routers import products, auth

app = FastAPI(
    title="ProductHunt Clone API",
    description="A simple API for ProductHunt clone",
    version="0.1.0"
)

app.include_router(products.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to ProductHunt Clone API!"}
