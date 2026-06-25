from fastapi import FastAPI

app = FastAPI(
    title="Vlineups"
)


@app.get("/")
async def root():
    return {"message": "Hello World"}
