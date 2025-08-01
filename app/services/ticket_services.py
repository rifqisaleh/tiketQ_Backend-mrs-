from flask import abort
from app.models.ticket import Ticket
from app.schemas.ticket_schemas import TicketSchema
from app.repo.ticket_repo import save_ticket, get_ticket_by_id, update_ticket, delete_ticket
from app.repo.ticket_repo import get_all_tickets as get_all
from datetime import datetime

ticket_schema = TicketSchema()
tickets_schema = TicketSchema(many=True)

def create_ticket(ticket: Ticket) -> Ticket:
    return save_ticket(ticket)

def fetch_all_tickets():
    tickets = get_all()
    return tickets_schema.dump(tickets)

def fetch_ticket_by_id(ticket_id):
    ticket = get_ticket_by_id(ticket_id)
    if not ticket:
        abort(404, description="Ticket not found")
    return ticket_schema.dump(ticket)

def mark_ticket_as_used(ticket_id):
    ticket = get_ticket_by_id(ticket_id)
    if not ticket:
        abort(404, description="Ticket not found")    

    ticket.is_used = True
    update = update_ticket(ticket)
    
    return {
        "message": "Ticket marked as used",
        "data": ticket_schema.dump(update)
    }

def remove_ticket(ticket_id):
    ticket = get_ticket_by_id(ticket_id)
    if not ticket:
        abort(404, description="Ticket not found")

    delete_ticket(ticket)
    return {"message": "Ticket deleted successfully"}