import discord
from discord.ext import commands

class MySlash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{__name__}.py is connected')
        try:
            synced = await self.bot.tree.sync()
            print(f"Synced {len(synced)} commands")
        except Exception as e:
            print(e)

    @discord.app_commands.command(name="today's_menu", description="今日の食堂のメニューを表示します。")
    async def todays_menu(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Today's menu is curry")

def setup(bot):
    bot.add_cog(MySlash(bot))