#!/usr/bin/env python3

if __name__ == "__main__":
    try:
        import discord
        from discord.ext import commands
        import os
        from dotenv import load_dotenv
        import asyncio

        load_dotenv()

        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True  # メッセージコンテンツのインテントを有効にする
        bot = commands.Bot(command_prefix="!", intents=intents, activity=discord.Game("学食"), help_command=None)

        async def load_extensions():
            for filename in os.listdir("./cogs"):
                if filename.endswith(".py"):
                    await bot.load_extension(f"cogs.{filename[:-3]}")

        @bot.event
        async def on_ready():
            print(f'Logged in as {bot.user}')

        async def main():
            async with bot:
                await load_extensions()
                await bot.start(os.getenv("SYOKUDOU_MENU_BOT_TOKEN"))

        asyncio.run(main())
    except KeyboardInterrupt:
        print("end.")
        exit(1)
