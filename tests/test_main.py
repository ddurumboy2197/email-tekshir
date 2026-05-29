# test_email.py
import pytest
from email_validator import validate_email, EmailNotValidError

def email_has_at(email):
    return '@' in email

def test_email_has_at():
    assert email_has_at('test@example.com') == True
    assert email_has_at('test@example') == False

def test_email_validator():
    try:
        validate_email('test@example.com')
        assert True
    except EmailNotValidError:
        assert False

def test_email_validator_invalid():
    with pytest.raises(EmailNotValidError):
        validate_email('test@example')
