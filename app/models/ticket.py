from app import db
import uuid
from datetime import datetime

class Ticket(db.Model):
    __tablename__ = 'tickets'

    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    event_name = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(120))
    time = db.Column(db.DateTime, nullable=False)
    is_used = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
