import discord
from discord.ext import commands
import random
import sqlite3


client = discord.Client()
intents = discord.Intents.default()
intents.members = True

#Declaração de listas para sintaxe any(args)
bolodemorango = ["bolo"]
pipoca = ["pipoca"]
cachorro = ["cachorro"]


@client.event
async def on_ready():
    db = sqlite3.connect("bot.db")
    cursor = db.cursor()
    print("Nós logamos como {0.user}".format(client))

@client.event
async def on_member_join(member):
    channel = client.get_channel(860246036009713677)
    await channel.send(f"Seja bem vindo {member.mention}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg: str = message.content

    if message.content.startswith("$update"):
        try:
            update = msg.splitlines()
            pt1 = update[1]
            pt2 = update[2]
            pt3 = update[3]
            pt4 = update[4]
            db = sqlite3.connect("bot.db")
            cursor = db.cursor()
            cursor.execute(f"INSERT INTO bot(ola, curiosidade, memes, vmemes) VALUES (?,?,?,?)",(pt1,pt2,pt3,pt4))
            db.commit()
            db.close()
            await message.reply("Cadastrado com Sucesso")
        except: await message.reply("Deu errado man, só lembrando que você tem que botar uma msg de olá, uma curiosidade, um meme e um video de meme, nem menos nem mais.")

    if message.content.startswith("$ver_ola"):
        db = sqlite3.connect("bot.db")
        cursor = db.cursor()
        cursor.execute("SELECT ola FROM bot")
        await message.channel.send(cursor.fetchall())
        db.commit()
        db.close()

    if message.content.startswith("$ver_curiosidade"):
        db = sqlite3.connect("bot.db")
        cursor = db.cursor()
        cursor.execute("SELECT curiosidade FROM bot")
        await message.channel.send(cursor.fetchall())
        db.commit()
        db.close()

    if message.content.startswith("$ver_memes"):
        db = sqlite3.connect("bot.db")
        cursor = db.cursor()
        cursor.execute("SELECT memes FROM bot")
        await message.channel.send(cursor.fetchall())
        db.commit()
        db.close()

    if message.content.startswith("$ver_vmemes"):
        db = sqlite3.connect("bot.db")
        cursor = db.cursor()
        cursor.execute("SELECT vmemes FROM bot")
        await message.channel.send(cursor.fetchall())
        db.commit()
        db.close()

    if message.content.startswith("$ola"):

        db = sqlite3.connect("bot.db")
        cursor = db.cursor()
        cursor.execute("SELECT ola FROM bot ORDER BY RANDOM() LIMIT 1")
        db_response = cursor.fetchone()
        await message.reply(db_response[0])

    elif message.content.startswith("$amogus"):
        await message.reply("Sussy Baka ? 😳")

    elif message.content.startswith("$nome"):
        await message.reply("Meu nome é Sussy Bot, um robô inteligente programado para o discord !")

    elif message.content.startswith("$idade"):
        msg_resposta = ["Então, eu sou um robô então é meio difícil dizer minha idade kk", "Não sei dizer ao certo", "Digamos que eu sou atemporal, independente da minha idade eu continuo sendo sus 😳", "Eu não tenho realmente uma idade, só sei que existo, logo, penso :)"]
        await message.reply(random.choice(msg_resposta))

    elif message.content.startswith("$curiosidade"):

        db = sqlite3.connect("bot.db")
        cursor = db.cursor()
        cursor.execute("SELECT curiosidade FROM bot ORDER BY RANDOM() LIMIT 1")
        db_response = cursor.fetchone()
        await message.reply(db_response[0])

    elif message.content.startswith("$noticia"):
        canais_de_noticia = ["https://www.globo.com/", "https://www.uol.com.br/", "https://www.terra.com.br/",
                             "https://www.cnnbrasil.com.br/","https://oglobo.globo.com/", "https://www.metropoles.com/", "https://g1.globo.com/",
                             "https://news.google.com.br/","https://www.r7.com/", "https://www.bbc.com/portuguese"]

        await message.reply("Aqui está um site para ti : " + random.choice(canais_de_noticia))

    elif message.content.startswith("$meme"):

        db = sqlite3.connect("bot.db")
        cursor = db.cursor()
        cursor.execute("SELECT memes FROM bot ORDER BY RANDOM() LIMIT 1")
        db_response = cursor.fetchone()
        await message.reply(db_response[0])

    elif message.content.startswith("$tchau"):
        msg_tchau = ["Até mais !", "Flw", "Te vejo na próxima", "A gente se vê...", "tchau", "Té mais fi", "Não esqueça de voltar para a gelatina de vespa-africana",
                     "Da próxima vez que vir, seja mais sus 😳", "Volte sempre, ou não sla"]
        await message.reply(random.choice(msg_tchau))

    elif any(word in msg for word in pipoca):
        await message.channel.send("https://www.youtube.com/watch?v=6AGana3rpa8&pp=sAQA")

    elif any(word in msg for word in bolodemorango):
        await message.channel.send("https://youtu.be/yiJVZknbCCM")

    elif message.content.startswith("$sus"):
        await message.channel.send("ඞ")

    elif any(word in msg for word in cachorro):
        await message.channel.send('https://youtu.be/az-zJ4QeQwc')

    elif message.content.startswith("$vmeme"):
        db = sqlite3.connect("bot.db")
        cursor = db.cursor()
        cursor.execute("SELECT vmemes FROM bot ORDER BY RANDOM() LIMIT 1")
        db_response = cursor.fetchone()
        await message.reply(db_response[0])

    elif message.content.startswith("$ajuda"):

        msgs_ajuda = ["O dia de amanhã será melhor que hoje", "Não se preocupe, vai dar tudo certo", "Melhor errar do que não tentar",
        "Você consegue, basta não desistir :)", "Obrigado por fazer o meu dia melhor :)", "Lembre-se, quanto mais sus, melhor", "Não se esqueça, você é único",
        "Não dá bola pro pessoal do twitter, é só um monte de mongol.", "Se alegre, amanhã é um novo dia ?"]

        await message.reply(random.choice(msgs_ajuda))

    else:
        pass


'''@client.command()
async def kick(msg, member = discord.Member, *, reason = None):
    await member.kick(reason=reason)'''





TOKEN = "ODYwMjQ2MzA2NDI5ODYxODg4.YN4czg.LP1QmvgT62_obVKcHYVih7xYTxo"

if __name__ == '__main__':
    client.run(TOKEN)

