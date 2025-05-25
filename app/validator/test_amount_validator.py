import pytest
from app.validator.amount_validator import validate_maximum_cash_amount, validate_positive_amount

def test_amount_validator_raises_on_too_large():
    with pytest.raises(ValueError, match="exceed 10000"):
        validate_maximum_cash_amount(20000)

def test_amount_validator_ok():
    validate_maximum_cash_amount(5000)

def test_positive_amount_validator_raises_on_zero():
    with pytest.raises(ValueError, match="be positive"):
        validate_positive_amount(0)

def test_positive_amount_validator_raises_on_negative():
    with pytest.raises(ValueError, match="be positive"):
        validate_positive_amount(-5)

def test_positive_amount_validator_ok():
    validate_positive_amount(10)
