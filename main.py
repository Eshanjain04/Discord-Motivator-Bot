import os
import discord
import requests
import json
import random

client = discord.Client()

sad_words_list = ["lonely","heartbroken","sad","depressed","lost","misreable","unhappy","grieved","worried","anxious","nervous","panic","stress","annoyed","irritated","cheated"]

cheering_up =["You're strong on your own","Take Deep breath","Talk to your friend","Everything is going to be okay"]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return quote

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
my_secret = os.environ['Token']

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$inspire'):
        await message.channel.send(get_quote())
      
    if any(word in message.content for word in sad_words_list):
        await message.channel.send(random.choice(cheering_up))

client.run(my_secret)