#!/usr/bin/env python3

if __name__ == "__main__":
    import discord
    from discord.ext import commands
    import os
    from dotenv import load_dotenv
    from my_cog import MyCog
    from my_slash import MySlash
    from my_date import MyDate
    import asyncio

    load_dotenv()

    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True  # メッセージコンテンツのインテントを有効にする
    bot = commands.Bot(command_prefix="!", intents=intents, activity=discord.Game("食事"), help_command=None)

    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user}')

    async def main():
        my_date = MyDate()
        my_date.start_monitoring(interval=10)
        await bot.add_cog(MyCog(bot))
        await bot.add_cog(MySlash(bot))

        token = os.getenv("SYOKUDOU_MENU_BOT_TOKEN")

        if token is None:
            raise ValueError("SYOKUDOU_MENU_BOT_TOKEN environment variable is not set")

        await bot.start(token)

    asyncio.run(main())