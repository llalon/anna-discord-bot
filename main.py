#!/usr/bin/env python3
import discord
import os
import APIKEY

### Some Constants
# Which discord channel to mo
MONITOR_CHANNEL = 'debug'
TOKEN = 'discord token'

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$inspire'):
    msg = "testmsg"
    await message.channel.send(quote)

#client.run(APIKEY.TOKEN)

if __name__ == "__main__":
    print(MONITOR_CHANNEL)
    print(APIKEY.TOKEN)
