users = [
    {
        "id": "1",
        "name": "Mary",
        "age": 18
    },
    {
        "id": "2",
        "name": "John",
        "age": 20
    }
]

def getUsers(id):
    if (id is None):
        return { "users": users }, 200
    else:
        for u in users:
            if (u["id"] == id):
                return { "user": u }, 200

    return { "message": "not found"}, 400

def createUser(req):
    # หา id ล่าสุด
    for u in users:
        id = u["id"]

    idStr = str(int(id)+1)

    try:
        user = {
            "id": idStr,
            "name": req["name"],
            "age": req["age"]
        }
    except:
        return { "message": "bad request" }, 400

    users.append(user)
    return { "message": "success" }, 200

def editUser(req, id):
    for i, user in enumerate(users):
        if user["id"] == id:
            try:
                users[i]["name"] = req["name"]
                users[i]["age"] = req["age"]
                return { "message": "success" }, 200
            except:
                return { "message": "bad request" }, 400
    return { "message": "id not found" }, 202

def deleteUser(id):
    for i, user in enumerate(users):
        if user["id"] == id:
            users.pop(i)
            return { "message": "success" }, 200
    return { "message": "id not found" }, 202

def calAvg():
    sum_age = 0
    total_user = 0
    for i, user in enumerate(users):
        sum_age += user["age"]
        total_user = i+1

    avg_result = sum_age / total_user
    return { "อายุรวม": sum_age, "user ทั้งหมด": total_user, "อายุเฉลี่ย": avg_result }, 200