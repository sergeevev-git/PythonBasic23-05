from fastapi import FastAPI, status
import uvicorn

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello index"}


@app.get("/ping/", status_code=status.HTTP_200_OK)
def ping():
    return {"message": "pong"}


if __name__ == "__main__":
    # uvicorn.run(app)
    uvicorn.run("main:app", reload=True)
