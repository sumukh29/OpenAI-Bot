# APPLICATION ID : 1233063611992244305
# PUBLIC KEY : e4451d06e1a8a4251742e2bf5b706df06b57702eb0be35c996451c170c53264e
import discord
import os
import openai

my_secret = os.environ['SECRET_KEY']
openai.api_key = os.getenv('OPENAI_API_KEY')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.content.startswith('-b'):
          response = openai.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=message.content,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
          )
          await message.channel.send(response.choices[0].text)

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(my_secret)