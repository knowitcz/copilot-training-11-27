from sqlmodel import Session, select
from app.models.client import Client

class ClientRepository:
    """Repository for database operations on Client entities."""
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[Client]:
        """Retrieves all clients from the database."""
        statement = select(Client)
        return list(self.session.exec(statement))

    def get_by_id(self, client_id: int) -> Client | None:
        """Retrieves a client by their ID from the database, returning None if not found."""
        statement = select(Client).where(Client.id == client_id)
        return self.session.exec(statement).first()
