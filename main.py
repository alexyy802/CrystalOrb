import nextcord as discord
from nextcord.ext import commands
import os

client = commands.Bot(command_prefix="mp!",help_command=False)

@client.event
async def on_ready():
  print('CrystalOrb Bot online.')

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
      client.load_extension(f"cogs.{filename[:-3]}")
print("All Cogs Loaded! 👍")

token = os.environ["TOKEN"]

client.run(token)
