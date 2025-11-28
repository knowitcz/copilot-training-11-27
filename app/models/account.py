from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.client import Client

class Account(SQLModel, table=True):
    """Database model representing a bank account."""
    id: int | None = Field(default=None, primary_key=True)
    name: str
    balance: int
    type: str
    client_id: int | None = Field(default=None, foreign_key="client.id")
    client: "Client" = Relationship(back_populates="accounts")
