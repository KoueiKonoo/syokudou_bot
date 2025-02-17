import discord
from discord.ext import commands
from my_pd import MyPandas
from my_date import MyDate

class MySlash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.my_pandas = MyPandas("menu_data_with_items.xlsx")
        self.my_date = MyDate()
        self.channel_id = None  # channel_idを初期化

    @discord.app_commands.command(name="今日のメニュー", description="今日の食堂のメニューを表示します。")
    async def todays_menu(self, interaction: discord.Interaction):
        menu = self.my_pandas.get_menu_for_today()
        if menu == None:
            await interaction.response.send_message("今日のメニューはありません")
        menu_message = "\n".join(menu)
        await interaction.response.send_message(f"今日のメニューは\n{menu_message}\nです。")
    
    @discord.app_commands.command(name="明日以降のメニュー", description="明日以降の食堂のメニューを表示します。\n負数を与えるとそれに応じたメニューが出てきます。")
    async def next_days_menu(self, interaction: discord.Interaction, days: int):
        menu = self.my_pandas.get_menu_for_next_days(days)
        if days <= -1:   
            if menu == None:
                await interaction.response.send_message(f"{abs(days)}日前のメニューはありません。")
            menu_message = "\n".join(menu)
            await interaction.response.send_message(f"{abs(days)}日前のメニューは\n{menu_message}\nでした。")
        elif days == 0:
            if menu == None:
                await interaction.response.send_message(f"今日のメニューはありません。")
            menu_message = "\n".join(menu)
            await interaction.response.send_message(f"今日のメニューは\n{menu_message}\nです。")
        else:
            if menu == None:
                await interaction.response.send_message(f"{days}日後のメニューはありません。")
            menu_message = "\n".join(menu)
            await interaction.response.send_message(f"{days}日後のメニューは\n{menu_message}\nです。")
    

    @discord.app_commands.command(name="author", description="作者についての情報を表示します。")
    async def author(self, interaction: discord.Interaction):
        await interaction.response.send_message("This bot is created by Kouei Konoo.\nGithub:KoueiKonoo\ntwitter: @rhythmgame_nene\n")

async def setup(bot):
    await bot.add_cog(MySlash(bot))