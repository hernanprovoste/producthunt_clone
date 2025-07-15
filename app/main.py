from fastapi import FastAPI

app = FastAPI(
    title="ProductHunt Clone API",
    description="A simple API for ProductHunt clone",
    version="0.1.0"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to ProductHunt Clone API!"}