from flask import Blueprint,request,jsonify
from models.contact_model import ContactModel

contact_bp=Blueprint("contact",__name__)

@contact_bp.route("/add_contact",methods=["POST"])
def add_contact():

    data = request.get_json(silent=True) or request.form

    ContactModel.add_contact(
        data["user_id"],
        data["name"],
        data["mobile"],
        data["relation"]
    )

    return jsonify({"status":True})


@contact_bp.route("/get_contacts/<user_id>")
def get_contacts(user_id):

    contacts=ContactModel.get_contacts(user_id)

    return jsonify({"status":True,"contacts":contacts})


@contact_bp.route("/delete_contact/<contact_id>",methods=["DELETE"])
def delete_contact(contact_id):

    ContactModel.delete_contact(contact_id)

    return jsonify({"status":True})

@contact_bp.route("/update_contact/<contact_id>", methods=["PUT"])
def update_contact(contact_id):

    data = request.get_json(silent=True) or request.form

    ContactModel.update_contact(
        contact_id,
        data["name"],
        data["mobile"],
        data["relation"]
    )

    return jsonify({"status":True})