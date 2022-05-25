# ก่อนอื่นให้ install flask ด้วยคำสั่ง 
# pip install flask
# or
# pip3 install flask (สำหรับคนที่ติดตั้ง python version3)

from flask import Flask, request

# สร้างข้อมูลตั้งต้น
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

# สร้างตัวแปล app สำหรับเตรียมกำหนดค่าเริ่มต้นของ server
app = Flask(__name__)

# Method GET return ค่าข้อมูลของ user
@app.route('/user', methods=['GET'])
def getUsers():
    id = request.args.get('id')
    #return {'id': id}, 200
   
    if (id is None):
        return { "users": users }, 200
    else:
        for u in users:
            if (u["id"] == id):
                return { "user": u }, 200

    return { "message": "not found"}, 400
    
# Method POST เพิ่มข้อมูล user
@app.route('/user', methods=['POST'])
def createUser():
    # หา id ล่าสุด
    for u in users:
        id = u["id"]

    idStr = str(int(id)+1)

    # ดึงค่าออกจาก body request ที่ส่งเข้ามา
    body = request.get_json()
    try:
        user = {
            "id": idStr,
            "name": body["name"],
            "age": body["age"]
        }
    except:
        return { "message": "bad request" }, 400

    users.append(user)
    return { "message": "success" }, 200

# Method PUT แก้ไขข้อมูล user ที่ id ตรงกับที่กำหนด
@app.route('/user', methods=['PUT'])
def editUser():
    body = request.get_json()
    for i, user in enumerate(users):
        if user["id"] == request.args.get('id'):
            try:
                users[i]["name"] = body["name"]
                users[i]["age"] = body["age"]
                return { "message": "success" }, 200
            except:
                return { "message": "bad request" }, 400
    return { "message": "id not found" }, 202

# Method DELETE ลบข้อมูล user ที่ id ตรงตามที่กำหนด
@app.route('/user', methods=['DELETE'])
def deleteUser():
    for i, user in enumerate(users):
        if user["id"] == request.args.get('id'):
            users.pop(i)
            return { "message": "success" }, 200
    return { "message": "id not found" }, 202

### Cal age average ###
@app.route('/user/avg', methods=['GET'])
def calAvg():
    sum_age = 0
    total_user = 0
    for i, user in enumerate(users):
        sum_age += user["age"]
        total_user = i+1

    avg_result = sum_age / total_user
    return { "อายุรวม": sum_age, "user ทั้งหมด": total_user, "อายุเฉลี่ย": avg_result }, 200


if __name__ == "__main__":
    app.run(debug=True)
