from app.models.client import Client
from app.repository.client_repository import ClientRepository

class ClientService:
    """Service layer for client-related business logic."""
    def __init__(self, client_repository: ClientRepository):
        self.client_repository = client_repository

    def get_all_clients(self) -> list[Client]:
        """Retrieves all clients from the repository."""
        return self.client_repository.get_all()

    def get_client_by_id(self, client_id: int) -> Client | None:
        """Retrieves a client by their ID, returning None if not found."""
        return self.client_repository.get_by_id(client_id)
