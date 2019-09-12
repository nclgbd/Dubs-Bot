import discord
import random
import spacy
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import CommandNotFound


INFO = str(open('botinfo.txt', 'r+').read()).split('\n')
TOKEN = INFO[0]
PREFIX = INFO[1]
client = commands.Bot(command_prefix = PREFIX)
nlp = None


@client.event
async def on_ready():
    # await client.change_presence(game = Game(name = "with RESTful API's"))
    print('Logged in as')
    print(client.user.name)
    print('------')
    nlp = spacy.load('en_core_web_lg')
    print('Modules Loaded:')
    if nlp: print('\tSpacy')
    await client.change_presence(activity=discord.Game(name='!help for bot info', type=1))
    

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

@client.command(name='ping',
                description='pong. (returns latency)')
async def ping(ctx):
    await ctx.send('pong')

@client.command(name = '8ball',
                description = 'Answers a yes or no questions',
                aliases = ['eightball'])
async def eight_ball(ctx):
    '''
    Works like an 3rd grader's 8 ball. How cute.
    '''
    responses = [
        'That is a resounding no',
        'Yes',
        'No',
        'Definitely', 
        'It\'s possible'
    ]
    
    await ctx.send(random.choice(responses))
    
client.run(TOKEN)