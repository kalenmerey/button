

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Pop"),
            KeyboardButton(text="Classical")
        ],
        [
            KeyboardButton(text="Rock"),
            KeyboardButton(text="Rap")
        ],
        [
            KeyboardButton(text="Jazz"),
            KeyboardButton(text="R&B")
        ],
        [
            KeyboardButton(text="Metal"),
            KeyboardButton(text="Folk")
        ],
    ],
    resize_keyboard=True
)
