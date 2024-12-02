token = 'MTI4MzQ1NTI1NjY1NDUxNjI2Ng.GC9VjP.Tv7LWlspooyqLdkXeZCT2m2MkOo9VmsA2VHdw8'
import discord
import random

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)
symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


def gen_parol(length = 6):
    parol = ''
    for i in range(length):
        parol += random.choice(symbols)
    return parol
    

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('parsley is'):
        await message.channel.send("cute!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('math'):
        await message.channel.send("Time for math!")
        await message.channel.send("Choose: \n 1. Give YOU a task \n 2. YOU will give ME a task")
    elif message.content.startswith('password'):
        await message.channel.send("Enter the length of the password:")
        msg = await client.wait_for('message')
        length = int(msg.content)
        await message.channel.send(gen_parol(length))
    if message.content.startswith('ladders and snakes'):
        await message.channel.send("Ohhhh yeah!")
        await message.channel.send("Choose size: \n 1. Normal (100 slots) \n 2. Advanced (250 slots) \n 3. Big (500 slots) \n 4. Giant (1000 slots)")
    if message.content.startswith('cube'):
        cube_number = random.randint(1,6)
        await message.channel.send("the number is:" ,cube_number)
        cube_plus_one = cube_number + 1
        await message.channel.send("the number plus 1:" ,cube_plus_one)
        double_number = cube_number + cube_number
        await message.channel.send("the doubled number:" ,double_number)
        number_times_number = cube_number * cube_number
        await message.channel.send("the number times himself:" ,number_times_number)
        
    
    
        

    else:
        await message.channel.send(message.content)

client.run(token)