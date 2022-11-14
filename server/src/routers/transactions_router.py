from fastapi import APIRouter


router = APIRouter()


@router.get("/transactions", status_code=200)
def get_all_transactions():
    pass


@router.post("/transactions", status_code=201)
def add_transactions():
    pass


@router.delete("/transactions", status_code=204)
def add_transactions():
    pass
