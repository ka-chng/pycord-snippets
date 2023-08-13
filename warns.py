import discord
from discord.ext import commands
from discord.commands import slash_command
from datetime import datetime

class Warns(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.warnings = {} 

    @slash_command(name='warn', description='Warn a member', guild_ids=[1128455366997463101, 1005266020400902305])
    @commands.has_permissions(manage_messages=True)
    async def warn(self, ctx, member: discord.Member, *, reason: str):
        guild_id = str(ctx.guild.id)
        member_id = str(member.id)
        if guild_id not in self.warnings:
            self.warnings[guild_id] = {}
        if member_id not in self.warnings[guild_id]:
            self.warnings[guild_id][member_id] = []

        self.warnings[guild_id][member_id].append((reason, ctx.author.id, datetime.utcnow()))

        warn_embed = discord.Embed(title=f"Warned {member.name}", description=f"Reason: {reason}", color=0xFFFFFF)
        await ctx.respond(embed=warn_embed)

    @slash_command(name='warnings', description='Get warnings of a member', guild_ids=[1128455366997463101, 1005266020400902305])
    @commands.has_permissions(manage_messages=True)
    async def warnings(self, ctx, member: discord.Member):
        guild_id = str(ctx.guild.id)
        member_id = str(member.id)

        if guild_id in self.warnings and member_id in self.warnings[guild_id]:
            warnings = self.warnings[guild_id][member_id]
        else:
            warnings = []

        warnings_embed = discord.Embed(title=f"Warnings for {member.name}", color=0xFFFFFF)
        for warning, moderator_id, time in warnings:
            moderator = ctx.guild.get_member(moderator_id)
            warnings_embed.add_field(name=f"Warned by {moderator.name} at {time.strftime('%Y-%m-%d %H:%M:%S')}", value=warning, inline=False)

        await ctx.respond(embed=warnings_embed)

    @slash_command(name='delete_warn', description='Delete a warning from a member', guild_ids=[1128455366997463101, 1005266020400902305])
    @commands.has_permissions(manage_messages=True)
    async def delete_warn(self, ctx, member: discord.Member, warn_index: int):
        guild_id = str(ctx.guild.id)
        member_id = str(member.id)

        if guild_id in self.warnings and member_id in self.warnings[guild_id] and 1 <= warn_index <= len(self.warnings[guild_id][member_id]):
            deleted_warn = self.warnings[guild_id][member_id].pop(warn_index - 1)
            delete_warn_embed = discord.Embed(title=f"Deleted warning from {member.name}", description=deleted_warn[0], color=0xFFFFFF)
        else:
            delete_warn_embed = discord.Embed(title=f"Failed to delete warning from {member.name}", description="Invalid warning index", color=0xFFFFFF)

        await ctx.respond(embed=delete_warn_embed)

def setup(bot):
    bot.add_cog(Warns(bot))
    
