# ก่อนอื่นให้ install flask ด้วยคำสั่ง 
# pip install flask
# or
# pip3 install flask (สำหรับคนที่ติดตั้ง python version3)

from flask import Flask, request
import service.user as userService

# สร้างตัวแปล app สำหรับเตรียมกำหนดค่าเริ่มต้นของ server
app = Flask(__name__)

# Method GET return ค่าข้อมูลของ user
@app.route('/user', methods=['GET'])
def getUser():
    id = request.args.get('id')
    return userService.getUsers(id)
    
# Method POST เพิ่มข้อมูล user
@app.route('/user', methods=['POST'])
def createUser():
    body = request.get_json()
    return userService.createUser(body)

# Method PUT แก้ไขข้อมูล user ที่ id ตรงกับที่กำหนด
@app.route('/user', methods=['PUT'])
def editUser():
    body = request.get_json()
    id = request.args.get('id')
    return userService.editUser(body, id)

# Method DELETE ลบข้อมูล user ที่ id ตรงตามที่กำหนด
@app.route('/user', methods=['DELETE'])
def deleteUser():
    id = request.args.get('id')
    return userService.deleteUser(id)

### Cal age average ###
@app.route('/user/avg', methods=['GET'])
def calAvg():
   return userService.calAvg()


if __name__ == "__main__":
    app.run(debug=True)
