import discord
from discord.ext import commands
from my_pd import MyPandas
from my_date import MyDate

class MySlash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.my_pandas = MyPandas("menu_data_with_items.xlsx")
        self.my_date = MyDate()

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{__name__}.py is connected')
        try:
            synced = await self.bot.tree.sync()
            print(f"Synced {len(synced)} commands")
        except Exception as e:
            print(e)

    @discord.app_commands.command(name="今日のメニュー", description="今日の食堂のメニューを表示します。")
    async def todays_menu(self, interaction: discord.Interaction):
        menu = self.my_pandas.get_menu_for_today()
        menu_message = "\n".join(menu)
        await interaction.response.send_message(f"Today's menu is:\n{menu_message}")

    @discord.app_commands.command(name="author", description="作者についての情報を表示します。")
    async def author(self, interaction: discord.Interaction):
        await interaction.response.send_message("This bot is created by Kouei Konoo.\nGithub:KoueiKonoo\ntwitter: @rhythmgame_nene\n")

def setup(bot):
    bot.add_cog(MySlash(bot))