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

    msg = message.content

    msg_ola = ["Olá seja bem vindo !", "E aí !", "Opa ! Tudo bem ?", "Boa tarde meu camarada",
               "Seja bem vindo, churrasco de tatu e pudim de tamanduá todos os sabádos e strogonoff de gato-palheiro com feijoada de de louva-deus aos domingos, não deixamos sobras.",
               "Seja bem vindo, sussy baka", "Bom ver você por aqui", "E aí, jóia ?",
               "Seja bem-vindo, não se esqueça do pudim de arara-vermelha às quintas",
               "Sério que você apareceu só agora ?", "Estava esperando por você ;)",
               "Achei que você não viria até aqui, estou surpreso", "Você por aqui ? Sus..."]

    '''if message.content.startswith("$update"):
        try:

            await message.reply("O que você gostaria de colocar ?")
            update_ola = await client.wait_for("message")
            update_curiosidade = await client.wait_for("message")
            update_memes = await client.wait_for("message")
            update_vmemes = await client.wait_for("message")

            db = sqlite3.connect("bot.db")
            cursor = db.cursor()
            cursor.execute(f"INSERT INTO bot(ola, curiosidade, memes, vmemes) VALUES (?,?,?,?)", (update_ola, update_curiosidade, update_memes, update_vmemes))
            db.commit()
            db.close()
            await message.reply("Cadastrado com Sucesso")
        except:
            await message.reply("Deu ruim, mlr esperar o adm me atualizar")'''

    if message.content.startswith("$insert_ola"):
        try:
            update = msg.split("$insert_ola ",1)[1]
            db = sqlite3.connect("bot.db")
            cursor = db.cursor()
            cursor.execute(f"INSERT INTO bot(ola) VALUES (?)",(update,))
            db.commit()
            db.close()
            await message.reply("Cadastrado com Sucesso")
        except: await message.reply("Deu errado tá man, depois eu peço pro adm me consertar")

    if message.content.startswith("$ola"):
        await message.reply(random.choice(msg_ola))

    elif message.content.startswith("$amogus"):
        await message.reply("Sussy Baka ? 😳")

    elif message.content.startswith("$nome"):
        await message.reply("Meu nome é Sussy Bot, um robô inteligente programado para o discord !")

    elif message.content.startswith("$idade"):
        msg_resposta = ["Então, eu sou um robô então é meio difícil dizer minha idade kk", "Não sei dizer ao certo", "Digamos que eu sou atemporal, independente da minha idade eu continuo sendo sus 😳", "Eu não tenho realmente uma idade, só sei que existo, logo, penso :)"]
        await message.reply(random.choice(msg_resposta))

    elif message.content.startswith("$curiosidade"):
        curiosidades = ["A terra não é uma esfera perfeita, cientificamente, ela é retrada como um elipsoide",
                        "O mar não é azul, nós vemos ele azul por causa do reflexo do céu",
                        "Não é biscoito, é bolacha :)", "O maior deserto da terra é a Antártica", "Um Boeing 747 levaria 120 bilhões de anos para cruzar a Via Láctea.", "a maior parte dos ataques cardíacos acontecem às segundas-feira.",
                        "Os homens são 6 vezes mais propensos a serem atingidos por um raio do que as mulheres.", "O primeiro telefone móvel inventado custava 3.995 dólares.", "As mulheres conseguem enxergar muito mais cores do que os homens",
                        "As mulheres precisam respirar mais vezes que os homens por causa da produção de hormônios.", "Na China, se alguém matar um urso panda pode ser sentenciado à morte.",
                        " No ano de 2010, a Síria recebeu mais turistas do que a Austrália.", "Cientistas estimaram que as temperaturas no local onde a bomba de Hiroshima explodiu chegaram a extraordinários 300 mil graus Célsius — isto é, cerca de 300 vezes mais quente do que a temperatura com a qual os corpos humanos normalmente são cremados.",
                        "Existe uma lâmpada que está ligada há mais de 113 anos na cidade de Livermore, na Califórnia.","4% da população mundial é canhota.", "Tocantins, fundado em 1988, é o estado mais novo do Brasil.", "O calendário da Etiópia, basicamente, é sete anos atrasado em relação a todo o ocidente.",
                        "Alguns gatos são alérgicos a pessoas", "O pássaro-lira pode imitar quase todos os sons que ouve", "Os bebês lontras marinhas não sabem nadar",
                        "A Coca-Cola seria verde se não fossem adicionados corantes.", "É impossível criar uma pasta com o nome con se você tiver Windows.",
                        "Alexander Graham Bell, o inventor do telefone, não podia ligar para sua mulher, ela era surda.", "Sapos não gostam de bebida alcoólica.",
                        "A única comida que não apodrece é o mel.", "Leonardo da Vinci inventou a tesoura.", "Existem aproximadamente 5, 000, 000, 000, 000, 000, 000, 000, 000, 000,000 de bactérias vivendo no planeta Terra.",
                        "A velocidade de rotação da Terra é de 1674.4 km/h."]
        await message.channel.send(random.choice(curiosidades))

    if message.content.startswith("$insert_curiosidade"):
        try:
            update = msg.split("$insert_curiosidade ", 1)[1]
            db = sqlite3.connect("bot.db")
            cursor = db.cursor()
            cursor.execute(f"INSERT INTO bot(curiosidade) VALUES (?)", (update,))
            db.commit()
            db.close()
            await message.reply("Cadastrado com Sucesso")
        except:
            await message.reply("Deu errado tá man, depois eu peço pro adm me consertar")

    elif message.content.startswith("$noticia"):
        canais_de_noticia = ["https://www.globo.com/", "https://www.uol.com.br/", "https://www.terra.com.br/",
                             "https://www.cnnbrasil.com.br/","https://oglobo.globo.com/", "https://www.metropoles.com/", "https://g1.globo.com/",
                             "https://news.google.com.br/","https://www.r7.com/", "https://www.bbc.com/portuguese"]

        await message.reply("Aqui está um site para ti : " + random.choice(canais_de_noticia))

    elif message.content.startswith("$meme"):
        memes = ["https://yt3.ggpht.com/L0rNzd4dpEEIgWOjx-5VQ504CnjM8AbAr9UOv3Ll42QP1S7-QFGyzSBQdcEN5KmQkO-mP1xCjIEkpw=s640-c-fcrop64=1,00000000ffffffff-nd",
                 "https://yt3.ggpht.com/5FtaDXJupEaM0RLbWPyc7wOVZb9NTdXCKewHi6nfyRlOkL_buZq81-6yaK9LqbChRVF9OeFkVLqOwg=s640-c-fcrop64=1,00000000ffffffff-nd",
                 "https://yt3.ggpht.com/JMhahrtnwcUHB7fV_9KPgIq8vR3lkpYZ99v74cdSp5_hRRfWgOdvAny9b-N0IICE-ZkUgnX0XRvSfdM=s640-c-fcrop64=1,00000000ffffffff-nd",
                 "https://yt3.ggpht.com/98dEBfoqLPoLMbwDbFt4RvSSaFrQVSXtA7zLC-uGyexylrP0TLwJatB2P8B7gQ4Fj9hBncaIudCrQg=s640-c-fcrop64=1,33990000cc66ffff-nd",
                 "https://yt3.ggpht.com/CIIQDFPGz1Jchtv1m4Cz_kHeunjaBICKLDgZbMo3DXyqEBtcekLUS503IGGfdNj3oENUo7Hq5-uRr5w=s640-c-fcrop64=1,00000000ffffffff-nd",
                 "https://yt3.ggpht.com/xYNG83yny-SJgh4EYPK2XGKYot99gIuE5BmZK24alQrmfmSSsSyu9foRIBFYVjqCFb11L85GMBp19w=s640-c-fcrop64=1,00000000ffffffff-nd",
                 "https://yt3.ggpht.com/ouafSfJ4iL0gox58-P03ssC8ULe1iEbvmfgS525R-tn46-4NFj_ZaabSI-1itCi0mCVFF5WRSeS-Cw=s146-c-fcrop64=1,00000000ffffffff-nd",
                 "https://yt3.ggpht.com/4VLrTnALxsToowI3ePcs1GFTEQjOWDd4rK1o2DBBnn1AbYelixENNCmr2kDK5WAlEdP_mAkOSJWrJg=s640-c-fcrop64=1,0b9d0000f462ffff-nd",
                 "https://yt3.ggpht.com/lnvgDwhI5eOvTI8RoqWypzwBjeF8dNX0lhSKddJD8AaEs-5actZbI4V6vCiBQcJnwOh66B_-O4qigc0=s640-c-fcrop64=1,00000000ffffffff-nd",
                 "https://yt3.ggpht.com/XLhf-Yzcq3rIsC4tDVYeSFqalnfNY8pH_3alv2yuKqJnpVnkoFTHo2_G2IfmhdAD_Dmse2aeYxsmc1g=s490-c-fcrop64=1,2e550000d1aaffff-nd",
                 "https://yt3.ggpht.com/prhslVbNgA6YvV6y-ZqwGV4x3PVL1QSz0Nxsgn2w7unvT5n32Yqylxi6zGlzdNprzaavbGiwJlNTwiA=s640-c-fcrop64=1,00000000ffffffff-nd",
                 "https://yt3.ggpht.com/aNEaPbFPG6Om3s8ck6XfenbgVb67sFUySEZk8-Q9hzlF_q63c9rXqgMyjDYOAwdcAeYICKjdMjGhrA=s240-c-fcrop64=1,00000000ffffffff-nd-rwa",
                 "https://yt3.ggpht.com/kjbINu5qVxEk64bsE1BrnTKBxNS7otmwQWW-yeaQ9MoG8rHCPK66qWloNSGId3U2dymdoMaQtbL4=s490-c-fcrop64=1,00000000cda3ffff-nd",
                 "https://yt3.ggpht.com/FKarY1HpTa4NF7jF7bT-rMjTNEeYbnv_2WoBElz9Pvl2Db_RPcP8HpZBdKU0GVXiJiwBaoGoQmM0lA=s640-c-fcrop64=1,69990000ffffffff-nd",
                 "https://yt3.ggpht.com/j87orFAL9wviiDuoOsIi2GcIxPB8b1ypJjv9SpedUdSUseJrp1MAYfGAK4xL2SUWQlDSohc61E4RlA=s640-c-fcrop64=1,38000000c7ffffff-nd",
                 "https://yt3.ggpht.com/5VqMJMIX3Iwuy-tCWkKCGVEuWTPkhBJCYlqy4dEtJ2USoG6jVaq8py4onRSG9wRVvqaREIBa6vUcPA=s640-c-fcrop64=1,00003f03ffffffe9-nd",
                 "https://yt3.ggpht.com/Y4NHJB799h0VKgayDRBo3WlvE3K5jClc-BW-mWiChiHwRf-1CPB2hx9hIp7uGGmQZ4-52BnZ_Wws60Y=s640-c-fcrop64=1,00000000ffffffff-nd",
                 "https://yt3.ggpht.com/HJIXFZebW6SYDZ4hgFHMl9ZLvJ9bjzJVDuQx9_RPq0OXSVNUj8x4l3h8WW2lZMcDuIZVuauOfhcCvQ=s640-c-fcrop64=1,00000000ffffffff-nd"
                 ]
        await message.channel.send(random.choice(memes))

    if message.content.startswith("$insert_memes"):
        try:
            update = msg.split("$insert_memes ", 1)[1]
            db = sqlite3.connect("bot.db")
            cursor = db.cursor()
            cursor.execute(f"INSERT INTO bot(memes) VALUES (?)", (update,))
            db.commit()
            db.close()
            await message.reply("Cadastrado com Sucesso")
        except: await message.reply("Deu errado man, depois eu peço pro adm me consertar")


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
        memesv = ["https://www.youtube.com/watch?v=Oq2Viwd7nOo", "https://www.youtube.com/watch?v=D0W9WoOesuM",
                  "https://www.youtube.com/watch?v=nxAR8ydI9aE", "https://www.youtube.com/watch?v=G6sdC5jV-VM",
                  "https://www.youtube.com/watch?v=8JA9R1VdtCQ", "https://www.youtube.com/watch?v=ANx5yMRCFbU",
                  "https://www.youtube.com/watch?v=jHw76mFvVUM", "https://www.youtube.com/channel/UCCINPOg76lH0tCC5aEur2BA",
                  "https://www.youtube.com/watch?v=ANx5yMRCFbU"]
        await message.channel.send(random.choice(memesv))

    if message.content.startswith("$insert_vmemes"):
        try:
            update = msg.split("$insert_vmemes ", 1)[1]
            db = sqlite3.connect("bot.db")
            cursor = db.cursor()
            cursor.execute(f"INSERT INTO bot(vmemes) VALUES (?)", (update,))
            db.commit()
            db.close()
            await message.reply("Cadastrado com Sucesso")
        except: await message.reply("Deu errado man, depois eu peço pro adm me consertar")



    elif message.content.startswith("$ajuda"):

        msgs_ajuda = ["O dia de amanhã será melhor que hoje", "Não se preocupe, vai dar tudo certo", "Melhor errar do que não tentar",
        "Você consegue, basta não desistir :)", "Obrigado por fazer o meu dia melhor :)", "Lembre-se, quanto mais sus, melhor", "Não se esqueça, você é único",
        "Não dá bola pro pessoal do twitter, é só um monte de mongol.", "Se alegre, amanhã é um novo dia ?"]

        await message.reply(random.choice(msgs_ajuda))

    else:
        pass


TOKEN = "ODYwMjQ2MzA2NDI5ODYxODg4.YN4czg.v-UX88PDi9ExO746e1apZ9H6E18"

if __name__ == '__main__':
    client.run(TOKEN)

