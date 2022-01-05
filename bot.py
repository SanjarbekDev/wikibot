import logging
from typing import Text
from aiogram.types import callback_query
import wikipedia
from aiogram import Bot, Dispatcher, executor, types
from wikipedia.wikipedia import *
from time import sleep

wikipedia.set_lang("uz")

count=0
msg=" "

API_TOKEN = '5010460087:AAFIqTFrc4tb3HJyXl5GjI7DdNp1kwL6jUU'


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

search=[]


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(f"Assalomu aleykum {message.from_user.first_name} men wikipedia botman, qanday so'zni izlayabsiz")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("Izlayotgan so'zingizni yuboring, bot esa sizga turli xil variantlarni topib beradi")


@dp.message_handler()
async def send(message: types.Message):
    global count,search
    search=[]
    count=0
    search=wikipedia.search(message.text)
    if search == []:
        await message.answer("Malumot topilmadi qayta urinib kko'ring ")
    else:
        keyboard=types.InlineKeyboardMarkup(row_width=2)#.add(keyboards)
        for i in search:
            keyboards=types.KeyboardButton(text=i, callback_data=str(count))
            count+=1
            keyboard.insert(keyboards)          
        await bot.send_message(message.from_user.id, 'Quyidagi malumotlar topildi:', reply_markup=keyboard)
            
@dp.callback_query_handler(lambda c: c.data == f"{count-1}")
async def process_callback_button10(callback_query: types.CallbackQuery):
    global msg
    if msg is " ":
        await bot.answer_callback_query(callback_query.id)
        summary=wikipedia.summary(search[count-1])
        msg = await bot.send_message(callback_query.from_user.id, 'malumot olinmoqda...')
        sleep(5)
        await bot.delete_message(callback_query.from_user.id,msg.message_id)
        s_s = await bot.send_message(callback_query.from_user.id, f'{summary}')
        msg=s_s
    else:
        await bot.answer_callback_query(callback_query.id)
        await bot.delete_message(callback_query.from_user.id,msg.message_id)
        summary=wikipedia.summary(search[count-1])
        msg = await bot.send_message(callback_query.from_user.id, 'malumot olinmoqda...')
        sleep(5)
        await bot.delete_message(callback_query.from_user.id,msg.message_id)
        s_s = await bot.send_message(callback_query.from_user.id, f'{summary}')
        msg=s_s
# await callback_query.message.delete()
@dp.callback_query_handler(lambda c: c.data == f"{count-2}")
async def process_callback_button9(callback_query: types.CallbackQuery):
    global msg
    if msg is " ":
        await bot.answer_callback_query(callback_query.id)
        summary=wikipedia.summary(search[count-2])
        msg = await bot.send_message(callback_query.from_user.id, 'malumot olinmoqda...')
        sleep(5)
        await bot.delete_message(callback_query.from_user.id,msg.message_id)
        s_s = await bot.send_message(callback_query.from_user.id, f'{summary}')
        msg=s_s
    else:
        await bot.answer_callback_query(callback_query.id)
        await bot.delete_message(callback_query.from_user.id,msg.message_id)
        summary=wikipedia.summary(search[count-2])
        msg = await bot.send_message(callback_query.from_user.id, 'malumot olinmoqda...')
        sleep(5)
        await bot.delete_message(callback_query.from_user.id,msg.message_id)
        s_s = await bot.send_message(callback_query.from_user.id, f'{summary}')
        msg=s_s

@dp.callback_query_handler(lambda c: c.data == f"{count-3}")
async def process_callback_button8(callback_query: types.CallbackQuery):
    global msg
    if msg is " ":
        await bot.answer_callback_query(callback_query.id)
        summary=wikipedia.summary(search[count-3])
        msg = await bot.send_message(callback_query.from_user.id, 'malumot olinmoqda...')
        sleep(5)
        await bot.delete_message(callback_query.from_user.id,msg.message_id)
        s_s = await bot.send_message(callback_query.from_user.id, f'{summary}')
        msg=s_s
    else:
        await bot.answer_callback_query(callback_query.id)
        await bot.delete_message(callback_query.from_user.id,msg.message_id)
        summary=wikipedia.summary(search[count-3])
        msg = await bot.send_message(callback_query.from_user.id, 'malumot olinmoqda...')
        sleep(5)
        await bot.delete_message(callback_query.from_user.id,msg.message_id)
        s_s = await bot.send_message(callback_query.from_user.id, f'{summary}')
        msg=s_s

@dp.callback_query_handler(lambda c: c.data == f"{count-4}")
async def process_callback_button7(callback_query: types.CallbackQuery):
    global msg
    if msg is " ":
        await bot.answer_callback_query(callback_query.id)
        summary=wikipedia.summary(search[count-4])
        msg = await bot.send_message(callback_query.from_user.id, 'malumot olinmoqda...')
        sleep(5)
        await bot.delete_message(callback_query.from_user.id,msg.message_id)
        s_s = await bot.send_message(callback_query.from_user.id, f'{summary}')
        msg=s_s
    else:
        await bot.answer_callback_query(callback_query.id)
        await bot.delete_message(callback_query.from_user.id,msg.message_id)
        summary=wikipedia.summary(search[count-4])
        msg = await bot.send_message(callback_query.from_user.id, 'malumot olinmoqda...')
        sleep(5)
        await bot.delete_message(callback_query.from_user.id,msg.message_id)
        s_s = await bot.send_message(callback_query.from_user.id, f'{summary}')
        msg=s_s

@dp.callback_query_handler(lambda c: c.data == f"{count-5}")
async def process_callback_button6(callback_query: types.CallbackQuery):
    global msg
    if msg is " ":
        await bot.answer_callback_query(callback_query.id)
        summary=wikipedia.summary(search[count-5])
        msg = await bot.send_message(callback_query.from_user.id, 'malumot olinmoqda...')
        sleep(5)
        await bot.delete_message(callback_query.from_user.id,msg.message_id)
        s_s = await bot.send_message(callback_query.from_user.id, f'{summary}')
        msg=s_s
    else:
        await bot.answer_callback_query(callback_query.id)
        await bot.delete_message(callback_query.from_user.id,msg.message_id)
        summary=wikipedia.summary(search[count-5])
        msg = await bot.send_message(callback_query.from_user.id, 'malumot olinmoqda...')
        sleep(5)
        await bot.delete_message(callback_query.from_user.id,msg.message_id)
        s_s = await bot.send_message(callback_query.from_user.id, f'{summary}')
        msg=s_s

@dp.callback_query_handler(lambda c: c.data == f"{count-6}")
async def process_callback_button5(callback_query: types.CallbackQuery):
    global msg
    if msg is " ":
        await bot.answer_callback_query(callback_query.id)
        summary=wikipedia.summary(search[count-6])
        msg = await bot.send_message(callback_query.from_user.id, 'malumot olinmoqda...')
        sleep(5)
        await bot.delete_message(callback_query.from_user.id,msg.message_id)
        s_s = await bot.send_message(callback_query.from_user.id, f'{summary}')
        msg=s_s
    else:
        await bot.answer_callback_query(callback_query.id)
        await bot.delete_message(callback_query.from_user.id,msg.message_id)
        summary=wikipedia.summary(search[count-6])
        msg = await bot.send_message(callback_query.from_user.id, 'malumot olinmoqda...')
        sleep(5)
        await bot.delete_message(callback_query.from_user.id,msg.message_id)
        s_s = await bot.send_message(callback_query.from_user.id, f'{summary}')
        msg=s_s

@dp.callback_query_handler(lambda c: c.data == f"{count-7}")
async def process_callback_button4(callback_query: types.CallbackQuery):
    global msg
    if msg is " ":
        await bot.answer_callback_query(callback_query.id)
        summary=wikipedia.summary(search[count-7])
        msg = await bot.send_message(callback_query.from_user.id, 'malumot olinmoqda...')
        sleep(5)
        await bot.delete_message(callback_query.from_user.id,msg.message_id)
        s_s = await bot.send_message(callback_query.from_user.id, f'{summary}')
        msg=s_s
    else:
        await bot.answer_callback_query(callback_query.id)
        await bot.delete_message(callback_query.from_user.id,msg.message_id)
        summary=wikipedia.summary(search[count-7])
        msg = await bot.send_message(callback_query.from_user.id, 'malumot olinmoqda...')
        sleep(5)
        await bot.delete_message(callback_query.from_user.id,msg.message_id)
        s_s = await bot.send_message(callback_query.from_user.id, f'{summary}')
        msg=s_s

@dp.callback_query_handler(lambda c: c.data == f"{count-8}")
async def process_callback_button3(callback_query: types.CallbackQuery):
    global msg
    if msg is " ":
        await bot.answer_callback_query(callback_query.id)
        summary=wikipedia.summary(search[count-8])
        msg = await bot.send_message(callback_query.from_user.id, 'malumot olinmoqda...')
        sleep(5)
        await bot.delete_message(callback_query.from_user.id,msg.message_id)
        s_s = await bot.send_message(callback_query.from_user.id, f'{summary}')
        msg=s_s
    else:
        await bot.answer_callback_query(callback_query.id)
        await bot.delete_message(callback_query.from_user.id,msg.message_id)
        summary=wikipedia.summary(search[count-8])
        msg = await bot.send_message(callback_query.from_user.id, 'malumot olinmoqda...')
        sleep(5)
        await bot.delete_message(callback_query.from_user.id,msg.message_id)
        s_s = await bot.send_message(callback_query.from_user.id, f'{summary}')
        msg=s_s

@dp.callback_query_handler(lambda c: c.data == f"{count-9}")
async def process_callback_button2(callback_query: types.CallbackQuery):
    global msg
    if msg is " ":
        await bot.answer_callback_query(callback_query.id)
        summary=wikipedia.summary(search[count-9])
        msg = await bot.send_message(callback_query.from_user.id, 'malumot olinmoqda...')
        sleep(5)
        await bot.delete_message(callback_query.from_user.id,msg.message_id)
        s_s = await bot.send_message(callback_query.from_user.id, f'{summary}')
        msg=s_s
    else:
        await bot.answer_callback_query(callback_query.id)
        await bot.delete_message(callback_query.from_user.id,msg.message_id)
        summary=wikipedia.summary(search[count-9])
        msg = await bot.send_message(callback_query.from_user.id, 'malumot olinmoqda...')
        sleep(5)
        await bot.delete_message(callback_query.from_user.id,msg.message_id)
        s_s = await bot.send_message(callback_query.from_user.id, f'{summary}')
        msg=s_s

@dp.callback_query_handler(lambda c: c.data == f"{count-10}")
async def process_callback_button1(callback_query: types.CallbackQuery):
    global msg
    if msg is " ":
        await bot.answer_callback_query(callback_query.id)
        summary=wikipedia.summary(search[count-10])
        msg = await bot.send_message(callback_query.from_user.id, 'malumot olinmoqda...')
        sleep(5)
        await bot.delete_message(callback_query.from_user.id,msg.message_id)
        s_s = await bot.send_message(callback_query.from_user.id, f'{summary}')
        msg=s_s
    else:
        await bot.answer_callback_query(callback_query.id)
        await bot.delete_message(callback_query.from_user.id,msg.message_id)
        summary=wikipedia.summary(search[count-10])
        msg = await bot.send_message(callback_query.from_user.id, 'malumot olinmoqda...')
        sleep(5)
        await bot.delete_message(callback_query.from_user.id,msg.message_id)
        s_s = await bot.send_message(callback_query.from_user.id, f'{summary}')
        msg=s_s


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)