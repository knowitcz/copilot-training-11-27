from typing import Protocol

class AmountValidator(Protocol):
    def __call__(self, amount: int) -> None:
        ...

def validate_maximum_cash_amount(amount: int) -> None:
    if amount > 10000:
        raise ValueError("Amount cannot exceed 10000.")

def validate_positive_amount(amount: int) -> None:
    if amount <= 0:
        raise ValueError("Amount must be positive.")
