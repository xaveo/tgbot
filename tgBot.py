import os, random
import telebot
from auth_data import *

def getRandomFile(path):
    # Returns a random filename
    fileName = os.listdir(path)
    index = random.randrange(0, len(fileName))
    return fileName[index]


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, hi_wordsB[random.randint(0, len(hi_wordsB) - 1)])
        bot.send_message(message.chat.id, question_sentencesB[random.randint(0, len(question_sentencesB) - 1)])            

    @bot.message_handler(commands=["команды"])
    def command_message(message):
        bot.send_message(message.chat.id, command)

    @bot.message_handler(commands=["фото"])
    def picMsg(message):
        path = os.path.normpath('C:\\Users\\xaveo\\Documents\\GitHub\\tgbot\\photo')
        pic = open(path + '\\' + getRandomFile(path), "rb")
        bot.send_photo(message.chat.id, pic)

    @bot.message_handler(commands=["музыка"])
    def audioMsg(message):
        path = 'C:\\Users\\xaveo\\Documents\\GitHub\\tgbot\\audio'
        audio = open(path+ '\\' + getRandomFile(path), "rb")
        bot.send_audio(message.chat.id, audio)

    @bot.message_handler(commands=["анимка"])
    def animeMessage(message):
        bot.send_message(message.chat.id, anime[random.randint(0, len(anime) - 1)])

    @bot.message_handler(commands=["комплиментик"])
    def complimentMessage(message):
        bot.send_message(message.chat.id, compliment[random.randint(0, len(compliment) - 1)])

    @bot.message_handler(commands=["поздравление"])
    def congratMessage(message):
        bot.send_message(message.chat.id, congratulation)

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() in hi_words:
            bot.send_message(message.chat.id, hi_wordsB[random.randint(0, len(hi_wordsB) - 1)])
            bot.send_message(message.chat.id, question_sentencesB[random.randint(0, len(question_sentencesB) - 1)])
        elif message.text.lower() in laugh:
            bot.send_message(message.chat.id, "чево смеешься, дурилка?)))")
        elif message.text.lower() == "хи-хи ха-ха":
            bot.send_message(message.chat.id, "ради этава стоит жыть!!!!")


    bot.polling()

if __name__ == '__main__':
    telegram_bot(token)