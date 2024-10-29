import discord

# Bot'u tanımla
intents = discord.Intents.default()
intents.members = True  # Üyelerin etkinliklerini izlemek için gerekli

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='general')
    if channel:
        await channel.send(f'Hoş geldin {member.mention}!')
        
        # Fonksiyonları çalıştır ve sonuçlarını yazdır
        print(double_letter("Hello"))
        print(secret_function(1, 2))
        print(secret_function("Hello, ", "world!"))
        print(double_letter2("welcome"))
        print(secret_function(1, 2))
        print(secret_function("Welcome, ", "world!"))

# Kullanıcı girdiğinde çalışacak olan fonksiyonları tanımla
def double_letter(string):
    result = ''
    for letter in string:
        result += letter * 2
    return result

def double_letter2(string):
    result = ''
    for letter in string:
        result += letter * 2
    return result

def secret_function(a, b):
    # Buraya kendi kodunuzu yazabilirsiniz
    return " "







client.run('your token')
