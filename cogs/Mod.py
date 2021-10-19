import nextcord as discord
from nextcord.ext import commands
import asyncio

class Moderation(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def ban(self,ctx,* ,user:discord.Member):
      if user == None:
        await ctx.send('Mention a member before using this command to ban someone!')
      if user == self.bot:
        await ctx.send('Whai u try to ban me :((')
      else:
        try:
          await user.ban()
          await ctx.send(f'{user} has been banned.')
          await user.send(f'You were banned for {ctx.guild}')
        except:
          await ctx.send('Couldnt ban that member...')
    
    @commands.command()
    async def kick(self,ctx,* ,user:discord.Member):
      if user == None:
        await ctx.send('Mention a member before using this command to ban someone!')
      if user == self.bot:
        await ctx.send('Whai u try to ban me :((')
      else:
        try:
          await user.ban()
          await ctx.send(f'{user} has been banned.')
          await user.send(f'You were banned for {ctx.guild}')
        except:
          await ctx.send('Couldnt ban that member...')
    
    @commands.command()
    async def lock(self,ctx,* ,channel : discord.TextChannel=None):
      channel = channel or ctx.channel
      overwrite = channel.overwrites_for(ctx.guild.default_role)
      overwrite.send_messages = False
      await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
      await ctx.send('Channel locked. :lock:')

    @commands.command()
    async def unlock(self,ctx,* ,channel:discord.TextChannel=None):
      channel = channel or ctx.channel
      overwrite = channel.overwrites_for(ctx.guild.default_role)
      overwrite.send_messages = True
      await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
      await ctx.send('Channel unlocked. :unlock:')
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, id: int):
      try:
        user = await self.client.fetch_user(id)
        await ctx.guild.unban(user)
        await ctx.send(f'{user} has been unbanned.')
      except:
        await ctx.send('Couldnt unban that member.')
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=10):
        amount = amount + 1
        if amount > 101:
            return await ctx.send(':warning: You have exedeed the purge limit.')
        else:
            await ctx.channel.purge(limit=amount)
            msg = await ctx.send("Cleared Messages")
            asyncio.sleep(10)
            await msg.delete()
