from flask import Blueprint,request,jsonify
from models.user_model import UserModel

auth_bp=Blueprint("auth",__name__)

@auth_bp.route("/register", methods=["POST"])
def register():

    name = request.form.get("name")
    email = request.form.get("email")
    mobile = request.form.get("mobile")
    password = request.form.get("password")

    UserModel.register(name,email,mobile,password)

    return jsonify({
        "status":"success",
        "message":"User Registered"
    })


@auth_bp.route("/login", methods=["POST"])
def login():

    email = request.form.get("email")
    password = request.form.get("password")

    user = UserModel.login(email, password)

    if user:
        return jsonify({
            "status": "success",
            "id": str(user["id"]),
            "name": user["name"],
            "email": user["email"],
            "mobile": user["mobile"]
        })

    return jsonify({
        "status": "error",
        "message": "Invalid Login"
    })

@auth_bp.route("/get_users", methods=["GET"])
def get_users():

    users = UserModel.get_all_users()

    return jsonify({
        "status": True,
        "data": users
    })