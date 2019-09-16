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
greetings = ['hi', 'hello', 'hey']
'''
with open('badwords.txt', 'r') as file:
    bad_words = file.read().split()
'''


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

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='HuSCII Coder')
    await client.add_roles(member, role)
    
    
    
'''
@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    
    
    content = message.content.strip().lower()
    author = message.author
    channel = message.channel
    
    if any(greeting in content for greeting in greetings):
        await channel.send('Bark!')
        
    await client.process_commands(message)
'''    
    
  
@client.command(name='info',
                aliases=['botinfo'])
async def info(ctx):
    '''
    Returns the code for the bot.
    '''
    embed = discord.Embed(color=0x4b2e83)
    embed.add_field(name='GitHub', value='https://github.com/nguobadia/Dubs-Bot')
    
    await ctx.send(embed=embed)


@client.command(name='socials',
                description='Returns a list of all our social media with links.')
async def socials(ctx):
    embed = discord.Embed(title="Our Social Media Links!", color=0x4b2e83)
    embed.set_footer(text='Follow any of these links to join our growing community!')
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/508830285698301992/623042784835796992/huscii_ascii.jpg?width=1288&height=1151')
    
    embed.add_field(name='DawgDen', value='https://uw-tacoma.presence.io/organization/huscii-coding-club')
    embed.add_field(name='Slack', value='https://husciicoding.slack.com/', inline=False)
    embed.add_field(name='FaceBook', value='https://www.facebook.com/groups/UWTProgrammingClub/')
    embed.add_field(name='Discord', value='https://discord.gg/vt5ZWdN')
    
    await ctx.send(embed=embed)


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
    
  
  
@client.command(name='schedule')
async def schedule(ctx):
    '''
    Returns a list of upcoming events.
    '''  
    await ctx.send('Coming soon!')

  
  
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