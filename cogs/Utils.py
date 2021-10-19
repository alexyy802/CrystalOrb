import nextcord as discord
from nextcord.ext import commands
import asyncio
import aiohttp
from io import BytesIO

class Utils(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def emojiremove(self, ctx, emoji: discord.Emoji):
        guild = ctx.guild
        if ctx.author.guild_permissions.manage_emojis:
            await ctx.send(f'{emoji} Has been deleted')
            await emoji.delete()

    @commands.command()
    async def addemoji(sef,ctx,* ,url:str,name):
     guild = ctx.guild
     async with aiohttp.ClientSession() as ses:
       async with ses.get(url) as r:
         try:
          imgorgif = BytesIO(await r.read())
          evalue = imgorgif.getvalue()
          if r.status in range(200, 299):
            emoji = await guild.create_custom_emoji(image=evalue, name=name)
            await ctx.send('Emoji Added.')
            await ses.close()
          else:
            await ctx.send('Sorry, something went wrong while processing this emoji.')
         except discord.HTTPException:
          await ctx.send('The File seems to be too large :/')
