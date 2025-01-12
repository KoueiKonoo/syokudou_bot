from discord.ext import commands, tasks
import my_pd
import my_date

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.my_pandas = my_pd.MyPandas("menu_data_with_items.xlsx")
        self.my_date = my_date.MyDate()
        self.auto_delivery.start()  # Cogの初期化時にタスクを開始

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{__name__}.py is connected')
        try:
            synced = await self.bot.tree.sync()
            print(f"Synced {len(synced)} commands")
        except Exception as e:
            print(e)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.content == 'hello':
            await message.channel.send('Hello!')
        await self.bot.process_commands(message)  # 他のコマンドが処理されるようにする

    @tasks.loop(seconds=1) 
    async def auto_delivery(self):
        self.my_date.update()  # 最新の日付と時刻を取得
        if self.my_date.now_time == "08:00:00":  # 朝8時に通知
            channel = self.bot.get_channel(1270216407224680458)  # 実際のチャンネルIDを指定
            if channel:
                menu = self.my_pandas.get_menu_for_today()
                menu_message = "\n".join([item for item in menu if item != 'nan'])  # リストの内容を整形
                await channel.send(f"@everyone おはようございます。本日のメニューをお知らせします。\n{menu_message}")

    @auto_delivery.before_loop
    async def before_auto_delivery(self):
        await self.bot.wait_until_ready()  # ボットが準備完了するまで待機

def setup(bot):
    bot.add_cog(MyCog(bot))