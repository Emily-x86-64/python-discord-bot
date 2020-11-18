import discord
import random
import duckduckgo
from discord.ext import commands

client = commands.Bot(command_prefix = '~')

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.dnd, activity=discord.Game("With JavaScript"))
	print('logged in as: {0.user}'.format(client))
@client.command()
async def ping(ctx):
	title = "Ping!"
	desc = f"Pong! Time Taken: {round(client.latency * 1000)}ms"
	col = random.randint(0, 0xfffff)
	embedVar = discord.Embed(title = title, description = desc, colour = col)
	await ctx.send(embed=embedVar)
@client.command(aliases = ['8ball', '8b'])
async def _8ball(ctx, *, question):

	responses = ['It is certain.',
	'It is decidedly so.',
	'Without a doubt.',
	'Yes - definitely.',
	'You may rely on it.',
	'As I see it, yes.',
	'Most likely.',
	'Outlook good.',
	'Yes.',
	'Signs point to yes.',
	'Reply hazy, try again.',
	'Ask again later.',
	'Better not tell you now.',
	'Cannot predict now.',
	'Concentrate and ask again.',
	'Dont count on it.',
	'My reply is no.',
	'My sources say no.',
	'Outlook not so good.',
	'Very doubtful.']

	title = "8-Ball"
	desc = f"Question: {question}\nAnswer: {random.choice(responses)}"
	col = random.randint(0, 0xfffff)
	embedVar = discord.Embed(title = title, description = desc, colour = col)
	await ctx.send(embed=embedVar)
@client.command(aliases = ['duck', 'bang', 'search', 'd', 'google'])
async def duckduckgo(ctx, *, query):
	title = f"{query}"
	desc = f"{duckduckgo.query(query, html=True).answer.text}"
	col = random.randint(0, 0xfffff)
	embedVar = discord.Embed(title = title, description = desc, colour = col)
	await ctx.send(embed=embedVar)
@client.command()
async def ticket(ctx):
	mod_em = discord.Embed(description="Support will be with you shortly.")
	user = ctx.author
	overwrites = {
	client.guild.default_role: discord.PermissionOverwrite(view_channel=False),
	"Internal Affairs" : discord.PermissionOverwrite(read_messages=True, send_messages=True)
	}
	user_ticket_channel = await ctx.guild.create_text_channel(name=f'Ticket: {ctx.author.name}')
	await user_ticket_channel.set_permissions(user, read_messages=True, send_messages=True, attach_files=True, overwrites=overwrites)
	await user_ticket_channel.send(f"{ctx.author.mention}", embed=mod_em)
@client.command()
async def jevil(ctx):
	await ctx.send('https://images-ext-1.discordapp.net/external/X9bj23zho7MqHFco8MrNx5k4cNXnRzyljKhOWofjGB0/https/i.postimg.cc/SsHzLr2W/jevilswing.gif')

client.run('<token>')
