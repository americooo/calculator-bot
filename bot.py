import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = '5865641153:AAFhGnMz2E3oF8YIdfL5F3Ch1M5QRC-GT5A'

wikipedia.set_lang('uz')
# wikipedia.set_lang('en')

# Configure logging

logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)



@dp.message_handler(commands=['start', 'help'])

async def send_welcome(message: types.Message):

    """

    This handler will be called when user sends `/start` or `/help` command

    """

    await message.reply("Hi!\nWelcome to Wikipedia bot!\nOwn amirbek_raxmatullayev")




@dp.message_handler()

async def sendwiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer('Bu mavzuga oid maqola topilmadi \n No article found for this topic')    



if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)