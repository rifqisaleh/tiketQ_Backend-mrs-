from app import db
from app.models.ticket import Ticket

def save_ticket(ticket: Ticket):
    db.session.add(ticket)
    db.session.commit()
    return ticket

def get_all_tickets():
    return Ticket.query.all()

def get_ticket_by_id(ticket_id: str):
    return db.session.get(Ticket, ticket_id)


def update_ticket(ticket):
    db.session.commit()
    return ticket

def delete_ticket(ticket):
    db.session.delete(ticket)
    db.session.commit()
