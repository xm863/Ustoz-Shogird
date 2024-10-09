import re
from aiogram.dispatcher.filters.state import State, StatesGroup


class Sherik(StatesGroup):
    name = State()  
    texnologiya = State()
    user_name = State()
    phone = State()
    hudud = State()
    narx = State()
    kasb = State()
    vaqt = State()
    maqsad = State()

class Ish_Joyi(StatesGroup):
    name = State()  
    yosh = State()  
    texnologiya = State()
    phone = State()
    hudud = State()
    narx = State()
    kasb = State()
    vaqt = State()
    maqsad = State()

class Xodim(StatesGroup):
    Idora = State()    
    texnologiya = State()
    phone = State()
    hudud = State()
    masul = State()
    vaqt = State()
    Ish_vaqti = State()
    oylik = State()
    qoshimcha_info = State()

class Ustoz(StatesGroup):
    name = State()  
    yosh = State()  
    texnologiya = State()
    phone = State()
    hudud = State()
    narx = State()
    kasb = State()
    vaqt = State()
    maqsad = State()

class SHogird(StatesGroup):
    name = State()  
    yosh = State()  
    texnologiya = State()
    phone = State()
    hudud = State()
    narx = State()
    kasb = State()
    vaqt = State()
    maqsad = State()



def validate_phone_number(phone_number):
    pattern = r'^\+998\d{9}$|^\d{9}$'
    match = re.match(pattern, phone_number)
    if match:
        return True
    else:
        return False
    

# print(validate_phone_number('+998974562321'))
    