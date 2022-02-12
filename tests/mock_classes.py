class Client:
    def __init__(self, user_id: str):
        self.user = User(user_id)


class Message:
    def __init__(self, message_text: str = None, user_id: str = None):
        if message_text is not None:
            self.content = message_text

        if user_id is not None:
            self.author = User(user_id)


class User:
    def __init__(self, user_id: str):
        self.id = user_id
