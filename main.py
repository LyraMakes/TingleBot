import discord
import os
import book_handler
import web_host


client = discord.Client()


@client.event
async def on_ready():
  web_host.set_num_servers(len(client.guilds))
  print('Successfully logged in as {0.user} on {1} server(s)'.format(client, len(client.guilds)))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$tingle'):
    await message.channel.send(book_handler.get_img())
  elif message.content.startswith('$update'):
    book_handler.update_imgs()
    await message.channel.send('Updated image directory to include {0} books'.format(len(book_handler.books)))
  elif message.content.startswith('$servers'):
    await message.channel.send('TingleBot is currently used in {0} server(s).'.format(web_host.get_num_servers()))


web_host.keep_alive()
# Runs the bot
client.run(os.getenv('TOKEN'))
