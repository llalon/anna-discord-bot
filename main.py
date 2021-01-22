#!/usr/bin/env python3
import discord
import os
import APIKEY
import func


# Command delcarations
commands = {
    'help': func.show_help,
    'request': func.request,
    'invite': func.invite
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
            msg_arg = " ".join(str(message.content).split()[1:])
            msg = commands[c](msg_arg)
            
            await message.channel.send(msg)


if __name__ == "__main__":
    client.run(APIKEY.TOKEN)
