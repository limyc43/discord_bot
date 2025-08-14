import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()  # .env 파일 읽기
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # 메시지 내용 읽기 허용
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} 봇 온라인!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "안녕" in message.content:  # 메시지에 '안녕'이 포함되면 반응
        await message.channel.send("안녕! 난 100% 캘리포니아산 프리미엄 아몬드로 만들어진 아몬드 브리즈야")

    await bot.process_commands(message)

bot.run(TOKEN)
