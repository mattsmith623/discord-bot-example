from os import environ

from discogs_client import Client as DiscogsClient
from discord import Embed, Message
from dotenv import load_dotenv


load_dotenv()
discogs_client = DiscogsClient('ExampleApplication/0.1', user_token=environ.get('DISCOGS_TOKEN'))


async def run_command(command_name: str, command_arguments: str, message: Message):
    command = command_name[1:]

    if command == 'echo':
        await run_echo_command(command_arguments, message)

    if command == 'search':
        await run_search_command(command_arguments, message)


async def run_echo_command(command_arguments: str, message: Message):
    await message.channel.send(command_arguments)


async def run_search_command(command_arguments, message):
    search_results = discogs_client.search(command_arguments, type='master').page(0)[0:10]
    listings = []

    for result in search_results:
        listings.append(f'[{result.id}: {result.title}](https://www.discogs.com{result.url})')

    embed = Embed(
        title=f'Search results for "{command_arguments}"',
        description="\n".join(listings)
    )

    await message.channel.send(embed=embed)
