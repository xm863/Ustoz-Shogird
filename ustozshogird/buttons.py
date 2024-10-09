from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menyu = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

b1 = KeyboardButton(text='Sherik kerak')
b2 = KeyboardButton(text='Ish joy kerak')
b3 = KeyboardButton(text='Xodim kerak')
b4 = KeyboardButton(text='Ustoz kerak')
b5 = KeyboardButton(text='Shogirt kerak')

menyu.add(b1, b2, b3, b4, b5)


phone_number = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
number = KeyboardButton(text='Telefon raqamni ulashish', request_contact=True)
phone_number.add(number)
