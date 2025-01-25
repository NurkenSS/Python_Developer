from fastapi import FastAPI
from app.routes import tweets, users, media, likes, root

app = FastAPI()

for route in [tweets, users, media, likes, root]:
    app.include_router(route.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the microblog service!"}
