from discord.ext import commands, tasks
from my_pd import MyPandas
from my_date import MyDate

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.my_pandas = MyPandas("menu_data_with_items.xlsx")
        self.my_date = MyDate()
        self.auto_delivery.start()

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
        if self.my_date.now_time == "09:40:00": 
                menu = self.my_pandas.get_menu_for_today()
                menu_message = "\n".join([item for item in menu if item != 'nan'])  # リストの内容を整形
                for guild in self.bot.guilds:  # Botが参加している全サーバを取得
                    for channel in guild.text_channels:  # サーバ内のテキストチャンネルを順にチェック
                        if channel.permissions_for(guild.me).send_messages:  # Botがメッセージを送れるか確認
                            await channel.send(f"@everyone\nおはようございます。今日のメニューをお知らせします。\n{menu_message}")
                            break  # 送信できたら次のサーバへ移動

    @auto_delivery.before_loop
    async def before_auto_delivery(self):
        await self.bot.wait_until_ready()

async def setup(bot):
    await bot.add_cog(MyCog(bot))
    