from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
import uvicorn
from models import User, Role, Gender, UserUpdateRequest

app = FastAPI()

# user_info = User()
#
# a = user_info.first_name = "mohit"
# db: list[User] = []
#
# a = User()
# a.first_name = "Mohit"
# a.last_name = "Shrestha"
# a.gender = "Male"
# a.middle_name = "BDR"
# # a.id = uuid4()
# db.append(a)
#
# data_base = []


db: List[User] = [
    User(
        id=uuid4(),
        # id=UUID("22a260f0-57dc-4dfa-ac0f-903c98f44662"),
        first_name="Ram",
        last_name="shrestha",
        middle_name="bdr",
        gender=Gender.male,
        roles=[Role.student]
    ),
    User(
        id=uuid4(),
        first_name="shani",
        last_name="Shakha",
        gender=Gender.female,
        roles=[Role.admin, Role.user]
    ),
    User(
        id=uuid4(),
        first_name="sajam",
        last_name="roniyar",
        gender=Gender.others,
        roles=[Role.user]
    )
]


@app.get("/")
async def root():
    return {"message": "Hello Mohit"}


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exists"
    )


@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                            user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                            user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                            user.roles  = user_update.roles
            return
        raise HTTPException(
            status_code=404,
            detail=f"user with id: {user_id} does not exists"
        )


# @app.post("/add_user/")
# async def add_user(data: User):
#     id_ = uuid4()
#     first_name = data.first_name
#     last_name = data.last_name
#     middle_name = data.middle_name
#     gender = data.gender
#     role = data.roles
#
#     new_user = {'id': id_, 'first_name': first_name, 'last_name': last_name,
#                 'gender': gender, 'middle_name': middle_name, "role": role}
#     data_base.append(new_user)
#     return f"User added with the id {id_}"


if __name__ == "__main__":
    uvicorn.run("fastapi1:app", host="127.0.0.1", port=8000, reload=True)
