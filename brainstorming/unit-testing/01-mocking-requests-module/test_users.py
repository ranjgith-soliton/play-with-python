from unittest import mock

import pytest
from users import User


class TestUser:
    @pytest.fixture
    @mock.patch("users.requests.get")
    def get_user(self, mock_requests_get, user):
        """
        Fixture that mocks the requests.get method and returns a user object.

        Args:
            mock_requests_get: Mock object for requests.get method.
            user: User object.

        Returns:
            User object.
        """
        mock_requests_get.return_value.json.return_value = user
        return User("randomuser.me").get_user()

    @pytest.mark.parametrize(
        "user",
        [
            {"name": "John Doe", "email": "me@johndoe.com"},
            {"name": "Jane Doe", "email": "me@janedoe.com"},
        ],
    )
    def test_get_user(self, get_user, user):
        """
        Test case to verify the get_user method of User class.

        Args:
            get_user: User object returned by the fixture.
            user: Expected user object.
        """
        assert get_user == user
