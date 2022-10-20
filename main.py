from asyncio import sleep
import config
import discord
from binance import Client

cfg = config.Config('res/config.cfg')
b_client = Client(cfg.b_api, cfg.b_api_s)
intents = discord.Intents.all()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    try:
        print(client.user.name)
        print(client.user.id)
        print('Discord.py Version: {}'.format(discord.__version__))
    except Exception as e:
        print(e)
    while True:
        await client.change_presence(status=discord.Status.online, activity=discord.Game("BTC: " + get_price() + ' $'))
        await sleep(30)


def get_price():
    price = b_client.get_margin_price_index(symbol='BTCUSDT')
    str(round(float(price['price']), 2))
    return str(round(float(price['price']), 2))

client.run(cfg.bot_token)