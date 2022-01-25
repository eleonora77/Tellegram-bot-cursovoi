# 5086780234:AAF02pkiMPXvU-WT2v5xAQiF9XvUn60j_G8
import telebot
from telebot import types
import config


bot = telebot.TeleBot(config.API_TOKEN)
@bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard=create_keyboard()
    bot.send_message(message.chat.id,
    'Привет! Я помогу тебе выбрать хорошую еду '
    'выбери,что больше нравится',reply_markup=keyboard)



def create_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    home = types.InlineKeyboardButton(text="домашняя еда", callback_data='1')
    place_top = types.InlineKeyboardButton(text='места с отличной кухней',
                                           callback_data='2')
    keyboard.add(home, place_top)
    return keyboard
def home():
    keyboard=types.InlineKeyboardMarkup(row_width=1)
    pancake=types.InlineKeyboardButton(text='🥞банановые оладьи',callback_data='3')
    sirnici=types.InlineKeyboardButton(text='сырники',callback_data='4')
    fish=types.InlineKeyboardButton(text='🐟🥕рыба с овощами',callback_data='5')
    pasta=types.InlineKeyboardButton(text='🍝 паста с тунцом',callback_data='6')
    maffin=types.InlineKeyboardButton(text='🧁кексы',callback_data='7')
    apple_cake=types.InlineKeyboardButton(text='🥮яблочный пирог',callback_data='8')
    ret_btn=types.InlineKeyboardButton(text='возврат в основное меню',
                                       callback_data='9')
    keyboard.add(pancake,sirnici,fish,pasta,maffin,apple_cake,ret_btn)
    return keyboard

def place_top():
    keyboard=types.InlineKeyboardMarkup(row_width=2)
    sushi=types.InlineKeyboardButton(text='лучшие суши🍣',callback_data='10')
    pizza=types.InlineKeyboardButton(text='лучшая пицца🍕',callback_data='11')
    burger=types.InlineKeyboardButton(text='лучший бургер🍔',callback_data='12')
    ret_btn=types.InlineKeyboardButton(text='возврат в основное меню',
                                       callback_data='9')
    keyboard.add(sushi,pizza,burger,ret_btn)
    return keyboard

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    keyboard=types.InlineKeyboardMarkup(row_width=3)
    keyboard_1 = home()
    keyboard_2 = place_top()
    bot.send_message(call.message.chat.id, 'выберите,что хотите'
                                       ' или вернитесь в основное меню',
                      reply_markup=keyboard)
    if call.message:
       if call.data=='1':
           bot.send_message(call.message.chat.id,
               'Выберите, что хотите приготовить'
               ,reply_markup=keyboard_1)
       if call.data=='3':
              bot.send_message(call.message.chat.id,
                'бананы -шт, молоко - 60мл,'
                'мука - 100гр'
                'сахар-2ст ложки,яйцо-1шт,сода-0,5 ч ложки'   
                 'лимонный сок-1ст ложка:'
                'бананы блендировать,яйца взбить с сахаром'
                'перемешать все ингридиенты и выпекать оладьи'
                'на сковородке с раст маслом пару минут с каждой стороны'
                'тесто брать ложкой небольшое количество',
                reply_markup=keyboard_1)
       if call.data=='4':
               bot.send_message(call.message.chat.id,
                '0.5 кг творога,чем жирнеее,тем лучше,'
                '2-3 яйца,2 ст ложки сахара,2-3 ст ложки '
                'муки,щепотка соды: яйца взбить с сахаром,'
                'добавить остальные ингредиенты,;жарить на среднем '
                'огне,масло не жадничать',reply_markup=keyboard_1)
       if call.data=='5':
               bot.send_message(call.message.chat.id,
               'филе трески-0,5 кг, морковь-2 шт,лук- 2щт,томатный соус-'
               '1 ст ложка,cпеции какие любите'
               'рыбу порезать,приправмть,морковь с луком обжврть на ско-'
               'вороде, через 10 мин добавить томатный соус,рыбу обжврить'
               'затем выложить рыбу в сотейник сверху выхожить овощи,'
               'и тушить на маленьком огне минут 15',reply_markup=keyboard_1)
       if call.data=='6':
               bot.send_message(call.message.chat.id,
                'паста 250 гр, тунец консервированный - 1 банка ,сыр твердый,'
                'лучше пармезан,чеснок,имбирь, специи,масло оливковое'
                'на масле обжарить имбирь,затем добавить чеснок,размять'
                'тунец вилкой, добавить имбирь с чесноком-это заправка для'
                'пасты, отварить макароны,слить воду,добавить заправку,сверху '
                'тертый сыр,прогреть все в кастрюле или на сковороде, чтобы'
                'сыр расплавился-паста готова',reply_markup=keyboard_1)

       if call.data=='7':
                bot.send_message(call.message.chat.id,
                '1 ст муки,3/4 ст сахара,1/2 ст изюма, 130 гр сливочного масла,'
                '3 яйца,щепотка соли,щепотка соды, 1 ст ложка любого крепкого'
                'алкоголя,лучше коньяк, стакан муки'
                'разогретое до состояния сметаны масло взбить с ахаром, добавить яйца,'
                'соль,коньяк все взбить, добавить муку соду и изюм, хорошо перемешать'
                'тесто разложить ложкой в формы, смазанные маслом , поставить в разогретую до '
                '190-200 градусов духовку и выпекать 25-35 минут, поверхность готовых'
                'кексов имеет продольные трещины',reply_markup=keyboard_1 )

       if call.data=='8':
              bot.send_message(call.message.chat.id,
               '4 яйца,175 грамм сахара,тертая цедра 1 лимона, 2 чайные ложки корицы,'
               '125 грамм сливочного масла, 200 грамм муки, 50 грамм грецких орехов'
               'несколько яблок,яйца взбить с сахаром,добавит масло, корицу,муку,орехи'
               'выложить тесто в форму,смазанную маслом,на тесто выложить порезанные '
               'тонко яблоки без кожуры, поставить в разогретую до 180 градусов духовку'
               'на 40 минут', reply_markup=keyboard_1)


       elif call.data == '2':
                   bot.send_message(call.message.chat.id, 'Отлично,выберите лучшую еду️',
                                reply_markup=keyboard_2)

       if call.data=='10':
               bot.send_message(call.message.chat.id,"🍣Ронин,ул.М.Богдановича 78",reply_markup=keyboard_2)
       if call.data=='11':
               bot.send_message(call.message.chat.id,'🍕Бергамо ул. Кульман 37',reply_markup=keyboard_2)
       if call.data=='12':
               bot.send_message(call.message.chat.id,'🍔BurgerLab ул.Октябрьская 19 к.4 ',reply_markup=keyboard_2)

       elif call.data=='9':
           keyboard = create_keyboard()


           bot.send_message(call.message.chat.id, 'возврат в основное меню',
                            reply_markup=keyboard)




if __name__=="__main__":
  bot.polling(none_stop=True,interval=0)