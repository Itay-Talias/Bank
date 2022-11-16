from fastapi import FastAPI
import uvicorn
from src.routers import transactions_router
from src.routers import users_roter
from src.routers import categories_roter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(transactions_router.router)
app.include_router(users_roter.router)
app.include_router(categories_roter.router)


origins = [
    "http://localhost",
    "http://localhost:3000",
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
    uvicorn.run("server:app", host="localhost", port=8080, reload=True)
