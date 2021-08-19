#Importação das bibliotecas
import discord #biblioteca do discord
from discord.ext import commands
import random #bibiloteca para randomizar comandos
import sqlite3 #biblioteca que realiza a conexão com a base de dados do robô


client = discord.Client() #Definição do cliente
intents = discord.Intents.default() #Configuração dos intents
intents.members = True

#Declaração de listas para sintaxe any(args)
bolodemorango = ["bolo"]
pipoca = ["pipoca"]
cachorro = ["cachorro", "cão"]

#Evento onde o cliente vai basicamente falar que está logado no servidor
@client.event
async def on_ready():
    print("Nós logamos como {0.user}".format(client))

#Evento que sauda a vinda de um novo membro no servidor
@client.event
async def on_member_join(member):
    channel = client.get_channel(860246036009713677)
    await channel.send(f"Seja bem vindo {member.mention}")

#Eventos centrais, basicamente onde tudo vai acontecer, desde de envio de mensagens até conversação bot -> usuário
@client.event
async def on_message(message):
    if message.author == client.user: #Se o autor da mensagem for um usuário, faça nada
        return

    msg: str = message.content

    if message.content.startswith("$update"): #Se o usuário digitar o comando, acessar a base de dados para atualizar seus dados
        try:
            update = msg.splitlines() #Quebra de linha estilo Enter (/n)
            pt1 = update[1] #Recolhimento do index de cada um
            pt2 = update[2]#...
            pt3 = update[3]#...
            pt4 = update[4]#...
            db = sqlite3.connect("bot.db") #Conexão do bot na base de dados
            cursor = db.cursor() #Configuração do cursor
            cursor.execute(f"INSERT INTO bot(ola, curiosidade, memes, vmemes) VALUES (?,?,?,?)",(pt1,pt2,pt3,pt4)) #Query do sql para realizar a atualização requisitada pelo usuário
            db.commit() #Salva
            db.close() #Fecha a conexão com a base de dados
            await message.reply("Cadastrado com Sucesso")
        except: await message.reply("Deu errado man, só lembrando que você tem que botar uma msg de olá, uma curiosidade, um meme e um video de meme, nem menos nem mais.")

    if message.content.startswith("$ver_ola"):
        db = sqlite3.connect("bot.db")
        cursor = db.cursor()
        cursor.execute("SELECT ola FROM bot")#Se o usuário quiser ver o que está cadastrado na base de dados
        await message.channel.send(cursor.fetchall())
        db.commit()
        db.close()

    if message.content.startswith("$ver_curiosidade"):
        db = sqlite3.connect("bot.db")
        cursor = db.cursor()
        cursor.execute("SELECT curiosidade FROM bot")#Se o usuário quiser ver o que está cadastrado na base de dados
        await message.channel.send(cursor.fetchall())
        db.commit()
        db.close()

    if message.content.startswith("$ver_memes"):
        db = sqlite3.connect("bot.db")
        cursor = db.cursor()
        cursor.execute("SELECT memes FROM bot")#Se o usuário quiser ver o que está cadastrado na base de dados
        await message.channel.send(cursor.fetchall())
        db.commit()
        db.close()

    if message.content.startswith("$ver_vmemes"):
        db = sqlite3.connect("bot.db")
        cursor = db.cursor()
        cursor.execute("SELECT vmemes FROM bot")#Se o usuário quiser ver o que está cadastrado na base de dados
        await message.channel.send(cursor.fetchall())
        db.commit()
        db.close()

    if message.content.startswith("$substituir"):
        try:
            update = msg.splitlines()
            s1 = update[1]
            s2 = update[2]
            db = sqlite3.connect("bot.db")
            cursor = db.cursor()
            cursor.execute("UPDATE bot SET ola = (?) WHERE ola = (?)", (s1,s2))
            db.commit()
            db.close()
            await message.reply("atualizado com sucesso")
        except: await message.reply("Man, eu preciso substituir um trem que existe ne kk, se tu quiser ver as msgs já cadastradas, só digitar $ver_ola")

    if message.content.startswith("$ola"):

        db = sqlite3.connect("bot.db")
        cursor = db.cursor()
        cursor.execute("SELECT ola FROM bot ORDER BY RANDOM() LIMIT 1")# Retorna um dos dados requisitados pelo usuário de forma aleatória
        db_response = cursor.fetchone()
        await message.reply(db_response[0])#Pega somente o primeiro resultado

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
        cursor.execute("SELECT curiosidade FROM bot ORDER BY RANDOM() LIMIT 1") # Retorna um dos dados requisitados pelo usuário de forma aleató
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
        cursor.execute("SELECT memes FROM bot ORDER BY RANDOM() LIMIT 1") # Retorna um dos dados requisitados pelo usuário de forma aleató
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
        cursor.execute("SELECT vmemes FROM bot ORDER BY RANDOM() LIMIT 1")# Retorna um dos dados requisitados pelo usuário de forma aleató
        db_response = cursor.fetchone()
        await message.reply(db_response[0])

    elif message.content.startswith("$ajuda"):

        msgs_ajuda = ["O dia de amanhã será melhor que hoje", "Não se preocupe, vai dar tudo certo", "Melhor errar do que não tentar",
        "Você consegue, basta não desistir :)", "Obrigado por fazer o meu dia melhor :)", "Lembre-se, quanto mais sus, melhor", "Não se esqueça, você é único",
        "Não dá bola pro pessoal do twitter, é só um monte de mongol.", "Se alegre, amanhã é um novo dia", "Eu estou aqui do seu lado :)", "Posso não ser uma pessoa real, mas sou seu amigo"]

        await message.reply(random.choice(msgs_ajuda))

    else: #Se caso outra coisa que não está no evento aconteça, apenas mantenha o programa
        pass

TOKEN = "ODYwMjQ2MzA2NDI5ODYxODg4.YN4czg.LP1QmvgT62_obVKcHYVih7xYTxo" #Token de ativação

if __name__ == '__main__': #Evita a ativação do bot de forma desnecessária
    client.run(TOKEN)

