from flask import Blueprint, request, jsonify
from app.models.ticket import Ticket
from app.schemas.ticket_schemas import TicketSchema
from app import db
from marshmallow import ValidationError
from datetime import datetime
from app.services.ticket_services import (
    create_ticket,
    fetch_all_tickets,     
    fetch_ticket_by_id,
    mark_ticket_as_used,   
    remove_ticket          
)

ticket_bp = Blueprint("ticket_bp", __name__)
ticket_schema = TicketSchema()
tickets_schema = TicketSchema(many=True)


@ticket_bp.route("/ping", methods=["GET"])
def health_check():
    return {"message": "Ticket API is running"}

@ticket_bp.route("/", methods=["POST"])
def post_ticket():
    try:
        ticket = ticket_schema.load(request.json) 
        new_ticket = create_ticket(ticket)
        return ticket_schema.dump(new_ticket), 201

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    except Exception as e:
        return jsonify({"message": "Internal Server Error", "error": str(e)}), 500
    
@ticket_bp.route("/", methods=["GET"])
def get_all():
    try:
        tickets = fetch_all_tickets()
        return jsonify(tickets), 200
    except Exception as e:
        return jsonify({"message": "Internal Server Error", "error": str(e)}), 500 

@ticket_bp.route("/<ticket_id>", methods=["GET"])
def get_one(ticket_id):
    ticket = fetch_ticket_by_id(ticket_id)
    return jsonify(ticket), 200

    
@ticket_bp.route("/<ticket_id>", methods=["PATCH"])
def patch_ticket(ticket_id):
    ticket = mark_ticket_as_used(ticket_id)
    return jsonify(ticket), 200

@ticket_bp.route("/<ticket_id>", methods=["DELETE"])
def delete_ticket_route(ticket_id):
    result = remove_ticket(ticket_id)
    return jsonify(result), 200


