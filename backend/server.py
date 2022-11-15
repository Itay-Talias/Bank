from fastapi import FastAPI
import uvicorn
from src.routers import transactions_router
from src.routers import users_roter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(transactions_router.router)
app.include_router(users_roter.router)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return "server is up and running"


if __name__ == "__main__":
    uvicorn.run("server:app", host="localhost", port=8000, reload=True)
