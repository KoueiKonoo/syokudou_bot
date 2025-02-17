import discord
from discord.ext import commands
from datetime import timedelta
from my_pd import MyPandas
from my_date import MyDate

class MySlash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.my_pandas = MyPandas("menu_data_with_items.xlsx")
        self.my_date = MyDate()

    @discord.app_commands.command(name="今日のメニュー", description="今日の食堂のメニューを表示します。")
    async def todays_menu(self, interaction: discord.Interaction):
        menu = self.my_pandas.get_menu_for_today()
        if menu == None:
            await interaction.response.send_message("今日のメニューはありません")
            return
        menu_message = "\n".join(menu)
        await interaction.response.send_message(f"今日のメニューは\n{menu_message}\nです。")
    
    @discord.app_commands.command(name="明日以降のメニュー", description="明日以降の食堂のメニューを表示します。\n負数を与えるとそれに応じたメニューが出てきます。")
    async def next_days_menu(self, interaction: discord.Interaction, days: int):
        self.my_date.update()
        today = self.my_date.now_date
        menu = self.my_pandas.get_menu_for_next_days(days)
        if 1 <= abs(days):   
            if menu == None:
                await interaction.response.send_message(f"{(today + timedelta(days)).strftime("%Y/%m/%d")}のメニューはありません。")
                return
            menu_message = "\n".join(menu)
            await interaction.response.send_message(f"{(today + timedelta(days)).strftime("%Y/%m/%d")}のメニューは\n{menu_message}\nでした。")
        else:
            if menu == None:
                await interaction.response.send_message(f"今日のメニューはありません。")
                return
            menu_message = "\n".join(menu)
            await interaction.response.send_message(f"今日のメニューは\n{menu_message}\nです。")

    @discord.app_commands.command(name="author", description="作者についての情報を表示します。")
    async def author(self, interaction: discord.Interaction):
        await interaction.response.send_message("This bot is created by Kouei Konoo.\nGithub:KoueiKonoos\n")

async def setup(bot):
    await bot.add_cog(MySlash(bot))