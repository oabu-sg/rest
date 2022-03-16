from flask import Flask, request, jsonify

flask_object = Flask(__name__)

#   http://127.0.0.1:5000
@flask_object.route('/', methods = ["GET"])
def home_page():
    return "Welcome to DevOps Server"


#   http://127.0.0.1:5000/hello
@flask_object.route('/hello', methods = ["GET"])
def say_hi():
    return "Hello"

#  http://127.0.0.1:5000/echo?name=daniel&position=manager
@flask_object.route('/echo', methods = ['GET'])
def echo_func():
    name_var = request.args.get("name")
    positon_var = request.args.get("position")
    return f"Echo Reply to the user: {name_var} - Position is: {positon_var}"


#   http://127.0.0.1:5000/employee/1
@flask_object.route('/employee/<employee_id>', methods = ['GET'])
def employee_getter(employee_id):
    return f"You're asking for information about Employee ID: {employee_id}"

#   http://127.0.0.1:5000/employee_record/1
@flask_object.route('/employee_record/<employee_id>', methods = ['GET'])
def employee_record_getter(employee_id):
    # Check the database, read from a file, etc
    data = jsonify(id = employee_id, name = "John", position = "Manager")
    return data

@flask_object.route('/employee_add', methods = ['POST'])
def add_employee():
    employee_data = request.json
    emp_id = employee_data['e_id']
    first_name = employee_data['f_name']
    last_name  = employee_data['l_name']
    #   Cal the method that will create the employee record
    return f"The employee ({emp_id}: {first_name} - {last_name}) will be added to the database"

if __name__ == "__main__":
    flask_object.run(debug=True)