from flask import Blueprint,request,jsonify
from models.sos_model import SOSModel

sos_bp=Blueprint("sos",__name__)

@sos_bp.route("/send_sos",methods=["POST"])
def send_sos():

    data=request.get_json(silent=True) or request.form

    sos_id=SOSModel.send_sos(
        data["user_id"],
        data["latitude"],
        data["longitude"]
    )

    return jsonify({
        "status":True,
        "sos_id":sos_id
    })


@sos_bp.route("/update_location",methods=["POST"])
def update_location():

    data=request.get_json(silent=True) or request.form
    print("TRACK HIT:", data)

    SOSModel.update_location(
        data["sos_id"],
        data["latitude"],
        data["longitude"]
    )

    return jsonify({"status":True})


@sos_bp.route("/stop_sos",methods=["POST"])
def stop_sos():

    data=request.get_json(silent=True) or request.form

    SOSModel.stop_sos(data["sos_id"])

    return jsonify({"status":True})


@sos_bp.route("/active_sos")
def active_sos():

    sos=SOSModel.get_active_sos()

    return jsonify({"status":True,"data":sos})

@sos_bp.route("/get_tracking/<sos_id>")
def get_tracking(sos_id):

    data = SOSModel.get_tracking(sos_id)

    return jsonify({"status":True,"data":data})

@sos_bp.route("/user_sos/<user_id>")
def user_sos(user_id):

    data = SOSModel.get_user_sos(user_id)

    return jsonify({"status":True,"data":data})

@sos_bp.route("/pause_sos", methods=["POST"])
def pause_sos():
    data = request.form
    SOSModel.pause_sos(data["sos_id"])
    return jsonify({"status": True})

@sos_bp.route("/resume_sos", methods=["POST"])
def resume_sos():
    data = request.form
    SOSModel.resume_sos(data["sos_id"])
    return jsonify({"status": True})