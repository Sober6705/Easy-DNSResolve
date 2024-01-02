import discord
from discord.ext import commands
import socket

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command(name='dns')
async def dns_lookup(ctx, query):
    try:
        ip_addresses_v4 = socket.getaddrinfo(query, None, socket.AF_INET)
        ip_addresses_v6 = socket.getaddrinfo(query, None, socket.AF_INET6)

        result_message = f'DNS 查询结果 - {query}:\n\n'

        if ip_addresses_v4:
            result_message += f'IPv4 地址：\n'
            for entry in ip_addresses_v4:
                result_message += f'{entry[4][0]}\n'

        if ip_addresses_v6:
            result_message += f'IPv6 地址：\n'
            for entry in ip_addresses_v6:
                result_message += f'{entry[4][0]}\n'

        if not ip_addresses_v4 and not ip_addresses_v6:
            result_message += '没有找到匹配的记录。'

        embed = discord.Embed(
            title=f'DNS 查询结果 - {query}',
            color=0x00ff00  # 可以更改嵌入消息的颜色
        )
        embed.add_field(name='DNS 查询', value=result_message, inline=False)

        await ctx.send(embed=embed)
    except socket.gaierror:
        await ctx.send(f'无法解析域名 {query}')
    except Exception as e:
        await ctx.send(f'DNS查询 {query} 时出现错误：{str(e)}') 


bot.run(''your bot token)
