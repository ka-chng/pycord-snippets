import discord
from discord.ext import commands
from discord.commands import slash_command

class GetMembers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='get_members', description="gets guild members", guild_ids=[1128455366997463101, 1005266020400902305])
    async def get_members(self, ctx):
        async for member in ctx.guild.fetch_members(limit=None):
            if not member.bot:
                with open('members.txt', 'a') as f:
                    f.write(member.name + '\n')

        await ctx.send('All members have been written to members.txt')

def setup(bot):
    bot.add_cog(GetMembers(bot))