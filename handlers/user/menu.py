from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp
from keyboards.default import menu

@dp.message_handler(Command("start"))
async def show_menu(message:Message):
    await message.answer("Hello! I am Merey, Choose your favorite genre!", reply_markup=menu)

@dp.message_handler(Text(equals=["Pop","Classical","Rock","Rap","Jazz","R&B","Metal","Folk"]))
async def get_food(message:Message):
    await message.answer(f"Choosen {message.text}.Thanks for choosing",
                         reply_markup=ReplyKeyboardRemove())


