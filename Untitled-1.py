import discord
from discord.ext import commands
import requests
import random
from idk import transfer2
tips = ["Separa tus residuos por categorías; los plásticos en una bolsa, las latas en otra, y así sucesivamente", "El consumismo perjudica al medio ambiente; si tienes cierto artefacto y aún funciona, no renueves.", "Pon tus desperdicios en el tacho, no los dejes en la calle y mucho menos en la naturaleza", "Si encuentras desechos tirados, llevalos al contenedor y el planeta te lo agradecerá", "Apoya a tus conocidos para que cuiden al planeta."]
blacklist = []
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command('upload')
async def upload(ctx):
    if ctx.message.attachments:
        for i in ctx.message.attachments:
            name = i.filename
            url = i.url
            await i.save( f"./img/{name}" )
            await ctx.send(f"Succesfully uploaded {name}")
    else:
        await ctx.send("Olvidaste adjuntar una imagen :face_with_raised_eyebrow:")

abc = transfer2()

@bot.command()
async def get_informed(ctx):
    await ctx.send(f"Aquí hay una noticia sobre el cambio climático, toma conciencia: {abc}")

@bot.command()
async def suggest(ctx,*, advice:str):
    if advice == "":
        await ctx.send("No has sugerido nada, después del comando escribe tu sugerencia")
    else:
        tips.append(advice)
        await ctx.send(f"Has sugerido lo siguiente: {advice} \n Si rompe las reglas del sevidor serás sancionado. \n Consejo # {len(tips)}")

@bot.command()
async def advice(ctx):
    tip = random.randint(0, len(tips) - 1)
    counter = 3
    while True:
        if tip in blacklist:
            tip +=1
        elif tip >= len(tips):
            if counter > 0:
                tip = random.randint(0, len(tips) - 1)
            else:
                tip = random.randint(0,4)
        else:
            break
    await ctx.send(f"Consejo #{tip + 1} : {tips[tip]}")


@bot.command()
async def delete(ctx, number:str):
    mod_role = discord.utils.get(ctx.author.roles, name="Administrador")
    if mod_role:
        try:
            number= int(number)
        except ValueError:
            await ctx.send("Envía un número válido")
        if number < len(tips) and number > 4:
            blacklist.append(number)
            await ctx.send("Consejo neutralizado")
        else:
            await ctx.send("Este consejo no existe o está por defecto")
    elif mod_role:
        await ctx.send("No has especificado en consejo a eliminar")
    else:
        await ctx.send("Solo los moderadores pueden usar este comando")


    
bot.run("NzQ1NjQ3ODM3NjU1NzI4MjQ5.Gesv8J.7D0V394qDJy0vj9FQdSvCbUNOKvDFMh94FTmLM")