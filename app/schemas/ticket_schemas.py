from app import ma
from app.models.ticket import Ticket

class TicketSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Ticket
        load_instance = True

    id = ma.auto_field()
    event_name = ma.auto_field(required=True)
    location = ma.auto_field()
    time = ma.auto_field(required=True)
    is_used = ma.auto_field()
    created_at = ma.auto_field(dump_only=True)
