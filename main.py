from discord.ext import commands
import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('------')
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))

# -- New command {!help}

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!help'):
            await message.channel.send('> Hello {0.author.mention}, je suis désolé mais la major partie de mes commandes ont étées perdues mais reste  tranquille, je suis en cours de redéveloppement '.format(message))

# -- New command {!bot-info}

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!bot-info'):
            await message.channel.send('> Hey {0.author.mention}, tu demandes plus d`info sur moi ?\n> Eh bien sache que je suis actuellement codé par <@!595159463028195330> mais que j`ai été imaginé par <@!707934350880014348>, mon nom viens de celui du cousin de<@!707934350880014348>.\n> Voilà voilà, c`est tout ce que je peux te dire '.format(message))


client = MyClient()
client.run('NzgzNzc5NTQ1NDk1ODk2MDk1.X8ftlQ.2__ETSm7MFIEq0B_gOZUOYm_nLY')