import uvicorn
from fastapi import FastAPI
from typing import Annotated
from fastapi import Path
from items_views import router as items_router
from users.views import router as user_router

app = FastAPI()
app.include_router(items_router)
app.include_router(user_router)


@app.get("/")
def hello_index():
    return {"message": "Hello world!"}


@app.post("/api/v1/post/{post_id1}")
def post_data(post_id1: Annotated[int, Path(ge=1, lt=100000)]):
    return {"message": post_id1}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
