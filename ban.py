import discord
from settings import log_channel_id
from discord.ext import commands


class ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True) # permission check
    async def ban(self, ctx, member: discord.Member, reason="No reason provided"): # checking if a reason was provided for the ban
        log_channel = log_channel_id # log channel ID
        guild = ctx.guild 
        ban_embed = discord.Embed( # creating the embed
            description=f"{member.mention} has been banned",
            color=0xFFFFFF
        )
        ban_embed.add_field(name="Reason: ", value=reason, inline=False) # if reason was provided this checks
        ban_embed.set_thumbnail(url=f"{self.bot.icon}")
        await ctx.reply(embed=ban_embed)
        await log_channel.send(embed=ban_embed) # sends ban embed in the log channel
        await guild.ban(user=member) # bans user from the guild


def setup(bot):
    bot.add_cog(ban(bot))
