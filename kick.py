import discord
from settings import log_channel_id
from discord.ext import commands


class kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True) # permission check
    async def kick(self, ctx, member: discord.Member, reason="No reason provided"): # checking if a reason was provided for the kick
        log_channel = log_channel_id # log channel ID
        guild = ctx.guild 
        kick_embed = discord.Embed( # creating the embed
            description=f"{member.mention} has been kicked",
            color=0xFFFFFF
        )
        kick_embed.add_field(name="Reason: ", value=reason, inline=False) # if reason was provided this checks
        kick_embed.set_thumbnail(url=f"{self.bot.icon}")
        await ctx.reply(embed=kick_embed)
        await log_channel.send(embed=kick_embed) # sends kick embed in the log channel
        await guild.kick(user=member) # kicks user from the guild


def setup(bot):
    bot.add_cog(kick(bot))
