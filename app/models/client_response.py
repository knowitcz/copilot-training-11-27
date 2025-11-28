from pydantic import BaseModel
from typing import List
from app.models.account import Account

class AccountResponse(BaseModel):
    """Response model for account information."""
    id: int
    name: str
    balance: int
    type: str

class ClientResponse(BaseModel):
    """Response model for basic client information."""
    id: int
    name: str
    national_id: str

class ClientDetailResponse(ClientResponse):
    """Detailed response model for client information including their accounts."""
    accounts: List[AccountResponse] = []
