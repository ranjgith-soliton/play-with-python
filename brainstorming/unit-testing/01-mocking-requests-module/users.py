import requests


class User:
    def __init__(self, source="randomuser.me"):
        """
        Initializes a User object.

        Args:
            source (str, optional): The source of the user data. Defaults to 'randomuser.me'.
        """
        self.url = f"https://{source}/api/"

    def get_user(self):
        """
        Retrieves a user from the specified source.

        Returns:
            dict: The user data in JSON format.
        """
        response = requests.get(self.url)
        return response.json()
