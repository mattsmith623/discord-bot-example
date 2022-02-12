from re import match

from discord import Client, Message


def is_bot_message(client: Client, message: Message) -> bool:
    return client.user.id == message.author.id


def is_command(message: Message) -> bool:
    return match('![a-zA-Z]', message.content) is not None


def parse_command(message: Message) -> list[str]:
    return message.content.split(maxsplit=1)
