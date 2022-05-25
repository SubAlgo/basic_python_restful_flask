# ก่อนอื่นให้ install flask ด้วยคำสั่ง 
# pip install flask
# or
# pip3 install flask (สำหรับคนที่ติดตั้ง python version3)

from flask import Flask, request
import service.user as userService

# สร้างตัวแปล app สำหรับเตรียมกำหนดค่าเริ่มต้นของ server
app = Flask(__name__)

# Method GET return ค่าข้อมูลของ user
@app.route('/user', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handler_user():
    if request.method == 'GET':
        id = request.args.get('id')
        return userService.getUsers(id)
    
    if request.method == 'POST':
        body = request.get_json()
        return userService.createUser(body)

    if request.method == 'PUT':
        body = request.get_json()
        id = request.args.get('id')
        return userService.editUser(body, id)

    if request.method == 'DELETE':
        id = request.args.get('id')
        return userService.deleteUser(id)


### Cal age average ###
@app.route('/user/avg', methods=['GET'])
def handler_calculate_average_age():
   return userService.calAvg()


if __name__ == "__main__":
    app.run(debug=True)
