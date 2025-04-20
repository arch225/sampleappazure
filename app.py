from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Sab bhagte phire aur main le ra maje",
            "author": "Neeraj Pepsu Dil me base"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)