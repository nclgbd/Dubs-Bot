import discord
import random
import datetime
# import spacy
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import CommandNotFound


INFO = str(open('botinfo.txt', 'r+').read()).split('\n')
TOKEN = INFO[0]
PREFIX = INFO[1]
client = commands.Bot(command_prefix = PREFIX)
nlp = None
start_time = datetime.datetime.utcnow()


@client.event
async def on_ready():
    # await client.change_presence(game = Game(name = "with RESTful API's"))
    print('Logged in as')
    print(client.user.name)
    print('------')
    '''
    nlp = spacy.load('en_core_web_lg')
    print('Modules Loaded:')
    if nlp: print('\tSpacy')
    '''
    await client.change_presence(activity=discord.Game(name='!help for bot info', type=1))
    

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

@client.command(name='ping',
                description='Pong! (returns latency)')
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(client.latency, 5)))

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
    
@client.command(name='uptime',
                description='Returns how long the bot has been running for.')
async def uptime(ctx):
    '''
    Source: https://stackoverflow.com/questions/52155265/my-uptime-function-isnt-able-to-go-beyond-24-hours-on-heroku
    '''
    now = datetime.datetime.utcnow() # Timestamp of when uptime function is run
    delta = now - start_time
    
    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    
    if days:
        time_format = "**{d}** days, **{h}** hours, **{m}** minutes, and **{s}** seconds."
        
    else:
        time_format = "**{h}** hours, **{m}** minutes, and **{s}** seconds."
        
    uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)
    await ctx.send('{} has been up for {}'.format(client.user.name, uptime_stamp))
    
client.run(TOKEN)