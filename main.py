import discord
from discord.ext import commands
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = '$', intents = intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == '$what_can_I_do':
        await message.channel.send('''
Асалам алейкум, вот тебе несколько решений проблем с загрезнением:
                                   
- Старайтесь использовать многоразовые предметы, такие как стаканчики и термосы, а не одноразовые пластиковые стаканчики и бутылки.
- Переходите на цифровые версии книг, журналов и газет, чтобы снизить использование бумаги.
- Выбирайте продукты с минимальной упаковкой, покупайте продукты весом и используйте собственные многоразовые сумки для покупок.
- Старайтесь перерабатывать отходы. Организуйте раздельный сбор мусора дома, и отнесите отходы в соответствующие пункты приема.
- Изучайте информацию о переработке отходов и о том, какие материалы можно переработать.
- Отдавайте старые вещи на переработку, а не выбрасывайте их в мусор.
- Используйте многоразовые предметы, чтобы сократить использование одноразовых изделий.
- Изучайте, какие продукты и упаковки лучше всего подходят для переработки, и выбирайте их при покупке.
- Экономьте воду, не оставляйте кран открытым, когда не используете воду.
- Используйте энергоэффективные приборы дома, такие как лампы накаливания и кондиционеры.
- Покупайте продукты из местных источников, чтобы сократить транспортировку.
- Старайтесь использовать общественный транспорт, ходить пешком или ездить на велосипеде вместо использования автомобиля.''')
    elif message.content == '$help':
        await message.channel.send('''
Специальный символ это $.
Используй его перед командами чтобы бот понял что это адресовано ему.
Функции:
what_can_I_do - Дает несколько советов как можно решить проблемы с загрязнениями.
recycleable - Выводит что можно переработать.
rand_url - Выводы рандомную ссылку
''')
    elif message.content == '$rand_url':
        url_list = ['https://www.youtube.com/watch?v=hRAqE1I-AAI', 
                    'https://ru.wikipedia.org/wiki/%D0%9E%D1%85%D1%80%D0%B0%D0%BD%D0%B0_%D0%BE%D0%BA%D1%80%D1%83%D0%B6%D0%B0%D1%8E%D1%89%D0%B5%D0%B9_%D1%81%D1%80%D0%B5%D0%B4%D1%8B', 
                    'https://www.kp.ru/guide/okhrana-okruzhajushchei-sredy.html']
        rand = random.choice(url_list)
        await message.channel.send(rand)
    elif message.content == '$recycleable':
        await message.channel.send('бумага батарейки пластик стекло ткань металл дерево пищевые отходы кожа картон')
    else:
        await message.channel.send('Нет такой функции! Напиши команду $help для ознакомления с функциями')

bot.run("Token")
