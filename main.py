from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from model.User import User
from body.User import UserBody
from typing import List

# fast api app
app = FastAPI()  # Create app instance


# on start server
@app.on_event("startup")
async def init():
    # database connection
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    await init_beanie(database=client.seedzero, document_models=[User])


@app.get("/")  # Define endpoint use GET method
def hello_world() -> dict:
    return {"msg": "hello world"}


@app.get("/users")
async def getUsers() -> List[User]:
    users = await User.find().to_list()
    return users


@app.get("/users/{id}")
async def getUser(id: str) -> User:
    users = await User.get(id)
    return users


@app.post("/users")
async def createUser(body: UserBody) -> User:
    user = User(**body.model_dump())
    await user.insert()
    return user


@app.delete("/users/{id}")
async def deleteUser(id) -> dict:
    user = await User.get(id)
    await user.delete()
    return {"msg": "delete user successfully"}


@app.put("/users/{id}")
async def updateUser(id: str, body: UserBody) -> User:
    user = await User.get(id)
    user.name = body.name
    user.age = body.age
    user.marry = body.marry
    await user.save()
    return user


# def
