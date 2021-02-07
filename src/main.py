#!/usr/bin/env python3
import discord
import os
import settings
import func

# Command delcarations
commands = {
    'help': func.show_help,
    'request': func.request,
    'invite': func.invite,
    'issue': func.send_feedback,
    'search': func.search
}

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Parse commands
    for c in commands:
        if (message.content.startswith('!' + c)):
            msg = commands[c](message)
            await message.channel.send(msg)


def init_anna():
    client.run(settings.DISCORD_TOKEN)


if __name__ == "__main__":
    init_anna()
