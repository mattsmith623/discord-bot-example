from os import environ

from discord import Client as DiscordClient
from dotenv import load_dotenv

from message_parser import is_bot_message, is_command, parse_command
from command_runner import run_command


class DiscordBot(DiscordClient):
    async def on_ready(self):
        print(f'Logged on as {self.user}')

    async def on_message(self, message):
        if is_bot_message(self, message) or not is_command(message):
            return

        command_name, command_arguments = parse_command(message)

        await run_command(command_name, command_arguments, message)


load_dotenv()

discord_client = DiscordBot()
discord_client.run(environ.get('DISCORD_TOKEN'))
