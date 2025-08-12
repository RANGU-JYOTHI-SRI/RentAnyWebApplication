from django.test import TestCase
from .models import UserRegistration
def test_should_create_user_with_username() -> None:
    user = UserRegistration.objects.create_user("Haki","abc@gmail.com","1234")
    assert user.username == "Haki"


