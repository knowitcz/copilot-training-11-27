from fastapi import APIRouter, Depends, HTTPException
from app.api.dependencies import get_client_service
from app.models.client_response import ClientResponse, ClientDetailResponse, AccountResponse
from app.services.client_service import ClientService

router = APIRouter()

@router.get("/client", response_model=list[ClientResponse])
def list_clients(client_service: ClientService = Depends(get_client_service)):
    """Retrieves a list of all clients."""
    clients = client_service.get_all_clients()
    return [ClientResponse(id=c.id, name=c.name, national_id=c.national_id) for c in clients]

@router.get("/client/{id}", response_model=ClientDetailResponse)
def get_client_detail(id: int, client_service: ClientService = Depends(get_client_service)):
    """Retrieves detailed information for a specific client, including their accounts."""
    client = client_service.get_client_by_id(id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    accounts = [AccountResponse(id=a.id, name=a.name, balance=a.balance, type=a.type) for a in client.accounts]
    return ClientDetailResponse(id=client.id, name=client.name, national_id=client.national_id, accounts=accounts)
