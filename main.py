import random
import telebot
from configurations import Configuration


bot = telebot.TeleBot(Configuration.token)
# keyboard1 = telebot.types.ReplyKeyboardMarkup()
# keyboard1.row("Բարիօր", "Հաջող", "Ծյուշ")

bad_words0 = ["տավար", "ապուշ", "էշ", "դեբիլ", "անասուն", "աննասուն", "եզ", "պյոս", "համբալ"]
bad_words1 = ["չմո"]

say_list = {
    "երեք": ["հլը ասա «երեք»", ["մի ձմերուկ բերեք", "բոյոյոյոյ"]],
    "հինգ": ["մի հատ ասա «հինգ»", ["ուտես մի վագոն խլինգ ։դդդդ լօօօլ", "բացել ա ։դ"]],
    "վեց": ["կարա՞ս ասես «վեց»", ["պապու թումբանը կեց", "։դդ ջոգի՞ր"]],
    "յոթ": ["ասա «յոթ»", ["դառնաս շոթ ։դ", "էս ես էի մտածել ։դդ"]],
    "ութ": ["հլը ասա «ութ»", ["ուտես մի վագոն թութ", "հըհըհըհը ։դ"]],
    "ինը": ["հլը ասա «ինը»", ["ուտես փղի տակինը ։դդ", "խի ա սենց բացում ։դ"]]
}

jokes = [
    ""
]

is_silent = False


def in_say_list(text, says):
    for key in says.keys():
        if key in text:
            return says[key][1]
    return False


def is_words_in_text(words: list, text) -> bool:
    for word in words:
        if word in text:
            return True
    return False


def in_bad_words(text):
    for w in bad_words0:
        if w in text:
            return w + "ը դու ես"
    for w in bad_words1:
        if w in text:
            return w + "ն դու ես"
    return False


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'ծյուշ ա անունս, բարիօր')  # , reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    global is_silent
    text = message.text.lower()
    if is_silent:
        if is_words_in_text(["ծյուշ արի", "արի ծյուշ", "ծյուշ հլը արի", "արի հլը ծյուշ"], text):
            is_silent = False
            bot.send_message(message.chat.id, "ստեղ եմ բրատ")
        return
    else:
        if is_words_in_text(["ծյուշ սուս", "սուս ծյուշ"], text):
            is_silent = True
            bot.send_message(message.chat.id, "լավ ((")
            return

    case_count = 0
    abarotka_bad_word = in_bad_words(text)
    if abarotka_bad_word:
        bot.send_message(message.chat.id, abarotka_bad_word)
        return
    if is_words_in_text(["բարիօր", "բարև", "պռիվետ", "պրիվետ", "բարլուս", "բարիոր", "բարի օր"], text):
        case_count += 1
        if is_words_in_text(["ջան", "ցավդ", "մեռնեմ", "սրտիդ"], text):
            bot.send_message(message.chat.id, 'Բարիօր մեռնեմ սրտիդ')
        else:
            bot.send_message(message.chat.id, "յանի նենց բարիօր")
    if is_words_in_text(["ինչ կա", "ոնց ես", "ո՞նց ես", "ոնց ե՞ս"], text):
        case_count += 1
        bot.send_message(message.chat.id, "առօրիա, դու ասա")
    if is_words_in_text(["ես քո ցավը տանեմ ես"], text):
        case_count += 1
        bot.send_message(message.chat.id, "ես քո մեռնեմ սրտիդ")
    if is_words_in_text(["ես քո մեռնեմ սրտիդ"], text):
        case_count += 1
        bot.send_message(message.chat.id, "ես քո ցավը տանեմ ես")
    if is_words_in_text(["լավ"], text):
        case_count += 1
        bot.send_message(message.chat.id, "դզված ես էլի")
    if is_words_in_text(["չեմ ասում", "չեմասում"], text):
        case_count += 1
        bot.send_message(message.chat.id, "ասաաա")
    if is_words_in_text(["անեկդոտ", "հումոր", "շուլուխ"], text):
        case_count += 1
        bot.send_message(message.chat.id, jokes[random.randint(0, len(jokes)-1)])
    if is_words_in_text(["տի տակոյ", "սմիշնոյ", "ումնիյ"], text):
        case_count += 1
        bot.send_message(message.chat.id, "նու պրիկռածի")

    if "չէ" == text.strip() or "չե" == text.strip():
        case_count += 1
        bot.send_message(message.chat.id, "խի՞")

    says = in_say_list(text, say_list)
    if says:
        case_count += 1
        for say in says:
            bot.send_message(message.chat.id, say)

    if is_words_in_text(["ծյուշ"], text) and case_count == 0:
        case_count += 1
        bot.send_message(message.chat.id, "անունս ո՞վ շոշափեց")

    if case_count == 0:
        case_count += 1
        bot.send_message(message.chat.id, say_list[random.choice(list(say_list.keys()))][0])


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    bot.send_message(message.chat.id, "սծիկեռներից լավ ե՞ս")


@bot.message_handler(content_types=['voice'])
def sticker_id(message):
    bot.send_message(message.chat.id, "վոյսեր մի ուղարկի")


@bot.message_handler(content_types=['location'])
def sticker_id(message):
    bot.send_message(message.chat.id, "զա տաբոյ ուժե վըյեխըլի")


bot.polling()
