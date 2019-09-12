import discord

private_info = str(open('token.txt', 'r+').read().split('\n'))
opcode = private_info[1]

async def hello(self, message):
        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))