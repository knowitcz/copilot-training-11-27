from sqlmodel import SQLModel, Field, Relationship
from typing import List

class Client(SQLModel, table=True):
    """Database model representing a client with their personal information and associated accounts."""
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    national_id: str = Field(unique=True, index=True)
    accounts: List["Account"] = Relationship(back_populates="client")
