from fastapi import FastAPI
import uvicorn
from src.routers import transactions_router
from src.routers import users_roter
app = FastAPI()

app.include_router(transactions_router.router)
app.include_router(users_roter.router)


@app.get("/")
def root():
    return "server is up and running"


if __name__ == "__main__":
    uvicorn.run("server:app", host="localhost", port=8000, reload=True)
