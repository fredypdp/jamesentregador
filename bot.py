import os
import random
import telebot
from telebot import types
from babel.numbers import format_currency

Token = os.environ.get("CHAVE_API")
bot = telebot.TeleBot(Token)

pizzaSelecionada = {}
monarkSelecionado = {}

@bot.message_handler(commands=["reclamar"])
def reclamar(mensagem):
    respostas = [
        "Pô, eu sei que a entrega tá demorando, mas, meu camarada, a situação aqui tá complicada! Tem trânsito, vias interditadas, e até o clima do Rio que não ajuda. Tô fazendo o meu melhor pra chegar aí logo!",
        
        "Cara, atrasou mesmo, não vou negar. Mas olha, tá difícil navegar nessa cidade, com tanto perrengue no caminho. Acredita em mim, tô correndo pra te entregar isso o mais rápido possível!",
        
        "Ô meu chapa, entendo a sua bronca, mas aqui no Rio é sinistro, né? Tem uns lugares que eu tenho que dar uma de ninja pra não levar um preju. Relaxa, tô chegando aí com o seu pedido, pode crer!",
        
        "Tô ligado que você tá puto com a demora, mas o Rio tá uma loucura! Tem umas paradas rolando no meio do caminho que eu não controlo. Juro que tô dando meu melhor pra te entregar o que você pediu!",
        
        "Fala, irmão, eu sei que tá esperando faz tempo, mas o role tá brabo hoje. Tô correndo igual um maluco pra chegar aí. Me desculpa pela demora, vou tentar ser mais rápido na próxima, blz?"
    ]
    texto = random.choice(respostas)

    markup = types.InlineKeyboardMarkup()

    # Adicione botões inline com comandos
    botao1 = types.InlineKeyboardButton("Inicio🏠", callback_data='inicio')

    markup.add(botao1)

    bot.send_message(mensagem.chat.id, texto, reply_markup=markup)

@bot.message_handler(commands=["sobre"])
def sobre(mensagem):
    introducoes = [
        "E aí, meu camarada! Sou um entregador carioca, trazendo aquele gostinho do Rio até a sua porta. Preparado para receber um sabor carioca no conforto da sua casa?",
        "Ei, beleza? Eu sou o entregador carioca que vai levar até você o calor do Rio em cada pedido. É sempre um prazer fazer parte do seu dia!",
        "Fala aí, galera! Eu sou o entregador carioca que vai trazer o tempero da Cidade Maravilhosa direto para a sua mesa. Vamos fazer desse momento uma viagem gastronômica!",
        "Salve, pessoal! Aqui é o entregador carioca, trazendo todo o ritmo e sabor do Rio para a sua casa. É hora de se deliciar com o que temos de melhor por aqui!"
    ]
    texto = random.choice(introducoes)

    markup = types.InlineKeyboardMarkup()

    # Adicione botões inline com comandos
    botao1 = types.InlineKeyboardButton("Inicio🏠", callback_data='inicio')

    markup.add(botao1)

    bot.send_message(mensagem.chat.id, texto, reply_markup=markup)

@bot.message_handler(commands=["cardapio"])
def cardapio(mensagem):
    texto = """
Qual sabor deseja🍕🍕?
    /nutella Nutella🍫
    /calabresa Calabresa🍕
    /portuguesa Portuguesa🇵🇹
    /frango Frango com catupiry🧀
    /recomendacao Pedir recomendação🆘"""

    markup = types.InlineKeyboardMarkup()

    # Adicione botões inline com comandos
    botao1 = types.InlineKeyboardButton("Pizza de Nutella🍫", callback_data='nutella')
    botao2 = types.InlineKeyboardButton("Pizza de Calabresa🍕", callback_data='calabresa')
    botao3 = types.InlineKeyboardButton("Pizza Portuguesa🇵🇹", callback_data='portuguesa')
    botao4 = types.InlineKeyboardButton("Pizza de Frango e Catupiry🧀", callback_data='frango')
    botao5 = types.InlineKeyboardButton("Pedir recomendação🆘", callback_data='recomendacao')
    botao6 = types.InlineKeyboardButton("Inicio🏠", callback_data='inicio')

    markup.add(botao1, botao2)
    markup.add(botao3, botao4)
    markup.add(botao5, botao6)

    bot.reply_to(mensagem, texto, reply_markup=markup)

@bot.message_handler(commands=["nutella"])
def nutella(mensagem):
    texto = """
    Escolha o tamanho:
    1 - Pequena, R$20,00
    2 - Média, R$35,00
    3 - Grande, R$45,00
Digite o número do tamanho que deseja, ou clique em um dos botões abaixo:"""

    markup = types.InlineKeyboardMarkup()

    # Adicione botões inline com comandos
    botao1 = types.InlineKeyboardButton("Pequena", callback_data='pequena')
    botao2 = types.InlineKeyboardButton("Média", callback_data='media')
    botao3 = types.InlineKeyboardButton("Grande", callback_data='grande')
    botao4 = types.InlineKeyboardButton("Inicio🏠", callback_data='inicio')

    markup.add(botao1, botao2, botao3)
    markup.add(botao4)

    global pizzaSelecionada
    pizzaSelecionada["sabor"] = "nutella"
    bot.reply_to(mensagem, texto, reply_markup=markup)

@bot.message_handler(commands=["calabresa"])
def calabresa(mensagem):
    texto = """
    Escolha o tamanho:
    1 - Pequena, R$30,00
    2 - Média, R$45.00
    3 - Grande, R$50.00
Digite o número do tamanho que deseja, ou clique em um dos botões abaixo:"""

    markup = types.InlineKeyboardMarkup()

    # Adicione botões inline com comandos
    botao1 = types.InlineKeyboardButton("Pequena", callback_data='pequena')
    botao2 = types.InlineKeyboardButton("Média", callback_data='media')
    botao3 = types.InlineKeyboardButton("Grande", callback_data='grande')
    botao4 = types.InlineKeyboardButton("Inicio🏠", callback_data='inicio')

    markup.add(botao1, botao2, botao3)
    markup.add(botao4)

    global pizzaSelecionada
    pizzaSelecionada["sabor"] = "calabresa"
    bot.reply_to(mensagem, texto, reply_markup=markup)

@bot.message_handler(commands=["portuguesa"])
def portuguesa(mensagem):
    texto = """
    Escolha o tamanho:
    1 - Pequena, R$20,00
    2 - Média, R$35.00
    3 - Grande, R$45.00
Digite o número do tamanho que deseja, ou clique em um dos botões abaixo:"""

    markup = types.InlineKeyboardMarkup()

    # Adicione botões inline com comandos
    botao1 = types.InlineKeyboardButton("Pequena", callback_data='pequena')
    botao2 = types.InlineKeyboardButton("Média", callback_data='media')
    botao3 = types.InlineKeyboardButton("Grande", callback_data='grande')
    botao4 = types.InlineKeyboardButton("Inicio🏠", callback_data='inicio')

    markup.add(botao1, botao2, botao3)
    markup.add(botao4)

    global pizzaSelecionada
    pizzaSelecionada["sabor"] = "portuguesa"
    bot.reply_to(mensagem, texto, reply_markup=markup)

@bot.message_handler(commands=["frango"])
def frango(mensagem):
    texto = """
    Escolha o tamanho:
    1 - Pequena, R$30,00
    2 - Média, R$45.00
    3 - Grande, R$60.00
Digite o número do tamanho que deseja, ou clique em um dos botões abaixo:"""

    markup = types.InlineKeyboardMarkup()

    # Adicione botões inline com comandos
    botao1 = types.InlineKeyboardButton("Pequena", callback_data='pequena')
    botao2 = types.InlineKeyboardButton("Média", callback_data='media')
    botao3 = types.InlineKeyboardButton("Grande", callback_data='grande')
    botao4 = types.InlineKeyboardButton("Inicio🏠", callback_data='inicio')

    markup.add(botao1, botao2, botao3)
    markup.add(botao4)

    global pizzaSelecionada
    pizzaSelecionada["sabor"] = "Frango e Catupiry"
    bot.reply_to(mensagem, texto, reply_markup=markup)

@bot.message_handler(commands=["recomendacao"])
def recomendacao(mensagem):
    recomendacoes = [
        "Nutella: Se você é um amante de sobremesas, não pode deixar de experimentar nossa deliciosa pizza de Nutella. Uma combinação irresistível de massa crocante coberta com Nutella cremosa e uma pitada de avelãs torradas. Uma verdadeira indulgência para os amantes de chocolate!",
        "Calabresa: A pizza de calabresa é um clássico que nunca sai de moda. Nossa versão é feita com uma massa fina e crocante, generosamente coberta com fatias suculentas de linguiça calabresa, queijo derretido e um toque especial de pimenta. Uma explosão de sabores que vai deixar seu paladar pedindo por mais.",
        "Portuguesa: Se você gosta de uma pizza recheada de ingredientes saborosos, a pizza portuguesa é a escolha perfeita. Nossa massa macia é coberta com molho de tomate, presunto, queijo, ovos, cebola, azeitonas e um toque de orégano. Uma combinação harmoniosa que agrada a todos os gostos.",
        "Portuguesa: Se você gosta de uma pizza recheada de ingredientes saborosos, a pizza portuguesa é a escolha perfeita. Nossa massa macia é coberta com molho de tomate, presunto, queijo, ovos, cebola, azeitonas e um toque de orégano. Uma combinação harmoniosa que agrada a todos os gostos."
    ]
    texto = random.choice(recomendacoes)

    markup = types.InlineKeyboardMarkup()

    # Adicione botões inline com comandos
    botao1 = types.InlineKeyboardButton("Cardápio📋", callback_data='cardapio')
    botao2 = types.InlineKeyboardButton("Inicio🏠", callback_data='inicio')

    markup.add(botao1, botao2)

    bot.send_message(mensagem.chat.id, texto, reply_markup=markup)

def pizzaDefinirTamanho(tamanho, chatId):
    global pizzaSelecionada

    if tamanho == "1":
        pizzaSelecionada["tamanho"] = "Pequena"

        if pizzaSelecionada["sabor"] == "nutella":
            pizzaSelecionada["preco"] = 20.00
        elif pizzaSelecionada["sabor"] == "calabresa":
            pizzaSelecionada["preco"] = 30.00
        elif pizzaSelecionada["sabor"] == "portuguesa":
            pizzaSelecionada["preco"] = 20.00
        elif pizzaSelecionada["sabor"] == "frango":
            pizzaSelecionada["preco"] = 30.00
    elif tamanho == "2":
        pizzaSelecionada["tamanho"] = "Média"

        if pizzaSelecionada["sabor"] == "nutella":
            pizzaSelecionada["preco"] = 35.00
        elif pizzaSelecionada["sabor"] == "calabresa":
            pizzaSelecionada["preco"] = 45.00
        elif pizzaSelecionada["sabor"] == "portuguesa":
            pizzaSelecionada["preco"] = 35.00
        elif pizzaSelecionada["sabor"] == "frango":
            pizzaSelecionada["preco"] = 45.00
    elif tamanho == "3":
        pizzaSelecionada["tamanho"] = "Grande"
        
        if pizzaSelecionada["sabor"] == "nutella":
            pizzaSelecionada["preco"] = 45.00
        elif pizzaSelecionada["sabor"] == "calabresa":
            pizzaSelecionada["preco"] = 50.00
        elif pizzaSelecionada["sabor"] == "portuguesa":
            pizzaSelecionada["preco"] = 45.00
        elif pizzaSelecionada["sabor"] == "frango":
            pizzaSelecionada["preco"] = 60.00
    else:
        bot.send_message(chatId, f"Escolha um tamanho!")
        return

    bot.send_message(chatId, f"Quantas Pizzas deseja? Digite o número de pizzas que deseja.")

def pizzaDefinirQuantidade(tamanho, chatId):
    global pizzaSelecionada
    
    try:
        pizzaSelecionada["quantidade"] = int(tamanho)
    except ValueError:
        bot.send_message(chatId, f"Digite o número de pizzas que deseja!")
        return
    
    try:
        precoCalculado = pizzaSelecionada["quantidade"] * pizzaSelecionada["preco"]
        preco = format_currency(precoCalculado, 'BRL', locale='pt_BR')
        markup = types.InlineKeyboardMarkup()

        # Adicione botões inline com comandos
        botao1 = types.InlineKeyboardButton("Inicio🏠", callback_data='inicio')

        markup.add(botao1)

        bot.send_message(chatId, f"""James está chegando a todo vapor com o seu pedido!🎁🏍
Pizza sabor🍕: {pizzaSelecionada["sabor"].capitalize()}
Quantidade🔄: {pizzaSelecionada["quantidade"]}
Preço💰: {preco}""", reply_markup=markup)
        pizzaSelecionada = {}
    except ValueError as erro:
        print(erro)

# Manipulador de consulta de botão inline
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chatId = call.message.chat.id 
    mensagem = call.message
    global pizzaSelecionada

    if call.data == 'cardapio':
        texto = """
Qual sabor deseja🍕🍕?
    /nutella Nutella🍫
    /calabresa Calabresa🍕
    /portuguesa Portuguesa🇵🇹
    /frango Frango com catupiry🧀
    /recomendacao Pedir recomendação🆘"""

        markup = types.InlineKeyboardMarkup()

        # Adicione botões inline com comandos
        botao1 = types.InlineKeyboardButton("Pizza de Nutella🍫", callback_data='nutella')
        botao2 = types.InlineKeyboardButton("Pizza de Calabresa🍕", callback_data='calabresa')
        botao3 = types.InlineKeyboardButton("Pizza Portuguesa🇵🇹", callback_data='portuguesa')
        botao4 = types.InlineKeyboardButton("Pizza de Frango e Catupiry🧀", callback_data='frango')
        botao5 = types.InlineKeyboardButton("Pedir recomendação🆘", callback_data='recomendacao')
        botao6 = types.InlineKeyboardButton("Inicio🏠", callback_data='inicio')

        markup.add(botao1, botao2)
        markup.add(botao3, botao4)
        markup.add(botao5, botao6)
        bot.send_message(chatId, texto, reply_markup=markup)
    elif call.data == 'nutella':
        texto = """
        Escolha o tamanho:
    1 - Pequena, R$20,00
    2 - Média, R$35,00
    3 - Grande, R$45,00
Digite o número do tamanho que deseja, ou clique em um dos botões abaixo:"""

        markup = types.InlineKeyboardMarkup()

        # Adicione botões inline com comandos
        botao1 = types.InlineKeyboardButton("Pequena", callback_data='pequena')
        botao2 = types.InlineKeyboardButton("Média", callback_data='media')
        botao3 = types.InlineKeyboardButton("Grande", callback_data='grande')
        botao4 = types.InlineKeyboardButton("Inicio🏠", callback_data='inicio')

        markup.add(botao1, botao2, botao3)
        markup.add(botao4)

        pizzaSelecionada["sabor"] = "nutella"
        bot.send_message(chatId, texto, reply_markup=markup)
    elif call.data == 'calabresa':
        texto = """
        Escolha o tamanho:
    1 - Pequena, R$30,00
    2 - Média, R$45.00
    3 - Grande, R$50.00
Digite o número do tamanho que deseja, ou clique em um dos botões abaixo:"""

        markup = types.InlineKeyboardMarkup()

        # Adicione botões inline com comandos
        botao1 = types.InlineKeyboardButton("Pequena", callback_data='pequena')
        botao2 = types.InlineKeyboardButton("Média", callback_data='media')
        botao3 = types.InlineKeyboardButton("Grande", callback_data='grande')
        botao4 = types.InlineKeyboardButton("Inicio🏠", callback_data='inicio')

        markup.add(botao1, botao2, botao3)
        markup.add(botao4)

        pizzaSelecionada["sabor"] = "calabresa"
        bot.send_message(chatId, texto, reply_markup=markup)
    elif call.data == 'portuguesa':
        texto = """
        Escolha o tamanho:
    1 - Pequena, R$20,00
    2 - Média, R$35.00
    3 - Grande, R$45.00
Digite o número do tamanho que deseja, ou clique em um dos botões abaixo:"""

        markup = types.InlineKeyboardMarkup()

        # Adicione botões inline com comandos
        botao1 = types.InlineKeyboardButton("Pequena", callback_data='pequena')
        botao2 = types.InlineKeyboardButton("Média", callback_data='media')
        botao3 = types.InlineKeyboardButton("Grande", callback_data='grande')
        botao4 = types.InlineKeyboardButton("Inicio🏠", callback_data='inicio')

        markup.add(botao1, botao2, botao3)
        markup.add(botao4)

        pizzaSelecionada["sabor"] = "portuguesa"
        bot.send_message(chatId, texto, reply_markup=markup)
    elif call.data == 'frango':
        texto = """
        Escolha o tamanho:
    1 - Pequena, R$30,00
    2 - Média, R$45.00
    3 - Grande, R$60.00
Digite o número do tamanho que deseja, ou clique em um dos botões abaixo:"""

        markup = types.InlineKeyboardMarkup()

        # Adicione botões inline com comandos
        botao1 = types.InlineKeyboardButton("Pequena", callback_data='pequena')
        botao2 = types.InlineKeyboardButton("Média", callback_data='media')
        botao3 = types.InlineKeyboardButton("Grande", callback_data='grande')
        botao4 = types.InlineKeyboardButton("Inicio🏠", callback_data='inicio')

        markup.add(botao1, botao2, botao3)
        markup.add(botao4)

        pizzaSelecionada["sabor"] = "frango"
        bot.send_message(chatId, texto, reply_markup=markup)
    elif call.data == 'recomendacao':
        recomendacao(mensagem)
    elif pizzaSelecionada and pizzaSelecionada["sabor"] and call.data == 'pequena':
        pizzaDefinirTamanho("1", chatId)
    elif pizzaSelecionada and pizzaSelecionada["sabor"] and call.data == 'media':
        pizzaDefinirTamanho("2", chatId)
    elif pizzaSelecionada and pizzaSelecionada["sabor"] and call.data == 'grande':
        pizzaDefinirTamanho("3", chatId)
    elif not "sabor" in pizzaSelecionada and call.data == 'pequena':
        markup = types.InlineKeyboardMarkup()

        # Adicione botões inline com comandos
        botao1 = types.InlineKeyboardButton("Cardápio📋", callback_data='cardapio')
        botao2 = types.InlineKeyboardButton("Inicio🏠", callback_data='inicio')

        markup.add(botao1, botao2)

        bot.send_message(chatId, "Escolha um sabor de Pizza", reply_markup=markup)
    elif not "sabor" in pizzaSelecionada and call.data == 'media':
        markup = types.InlineKeyboardMarkup()

        # Adicione botões inline com comandos
        botao1 = types.InlineKeyboardButton("Cardápio📋", callback_data='cardapio')
        botao2 = types.InlineKeyboardButton("Inicio🏠", callback_data='inicio')

        markup.add(botao1, botao2)

        bot.send_message(chatId, "Escolha um sabor de Pizza", reply_markup=markup)
    elif not "sabor" in pizzaSelecionada and call.data == 'grande':
        markup = types.InlineKeyboardMarkup()

        # Adicione botões inline com comandos
        botao1 = types.InlineKeyboardButton("Cardápio📋", callback_data='cardapio')
        botao2 = types.InlineKeyboardButton("Inicio🏠", callback_data='inicio')

        markup.add(botao1, botao2)

        bot.send_message(chatId, "Escolha um sabor de Pizza", reply_markup=markup)
    elif call.data == 'reclamar':
        reclamar(mensagem)
    elif call.data == 'sobre':
        sobre(mensagem)
    elif call.data == 'inicio':
        markup = types.InlineKeyboardMarkup()

        # Adicione botões inline com comandos
        botao1 = types.InlineKeyboardButton("Cardápio📋", callback_data='cardapio')
        botao2 = types.InlineKeyboardButton("Sobre mim🙎🏽‍♂️", callback_data='sobre')
        botao3 = types.InlineKeyboardButton("Reclamar de um pedido🗣", callback_data='reclamar')


        markup.add(botao1, botao2)
        markup.add(botao3)

        bot.send_message(chatId, """
        Você acabou de invocar os serviços de James. O que quer da realeza? faça a sua escolha:
        /menu Cardápio📋
        /sobre Sobre mim🙎🏽‍♂️
        /reclamar Reclamar de um pedido🗣
Ou clique em um dos botões abaixo⬇️:""", reply_markup=markup)

def verificar(mensagem):
    if pizzaSelecionada and pizzaSelecionada["sabor"] and "tamanho" not in pizzaSelecionada:
        pizzaDefinirTamanho(mensagem.text, mensagem.chat.id)
        return
    elif pizzaSelecionada and pizzaSelecionada["sabor"] and pizzaSelecionada["tamanho"]:
        pizzaDefinirQuantidade(mensagem.text, mensagem.chat.id)
        return
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    markup = types.InlineKeyboardMarkup()

    # Adicione botões inline com comandos
    botao1 = types.InlineKeyboardButton("Cardápio📋", callback_data='cardapio')
    botao2 = types.InlineKeyboardButton("Sobre mim🙎🏽‍♂️", callback_data='sobre')
    botao3 = types.InlineKeyboardButton("Reclamar de um pedido🗣", callback_data='reclamar')

    markup.add(botao1, botao2)
    markup.add(botao3)

    bot.reply_to(mensagem, """
    Você acabou de invocar os serviços de James. O que quer da realeza? faça a sua escolha:
/cardapio Cardápio📋
/sobre Sobre mim🙎🏽‍♂️
/reclamar Reclamar de um pedido🗣
Ou clique em um dos botões abaixo⬇️:""", reply_markup=markup)
