from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from buttons import menyu, phone_number 
from states import Sherik, validate_phone_number, Ish_Joyi, Xodim, Ustoz, SHogird

bot = Bot(token='7573927937:AAHItgjA9ob3D0CunrRpS2H31XA1fBqhyOE')
dp = Dispatcher(bot=bot, storage=MemoryStorage())



@dp.message_handler(commands='start')
async def start(msg: types.Message):
    text = f"""
<b>Assalom alaykum {msg.from_user.full_name}
UstozShogird kanalining rasmiy botiga xush kelibsiz!</b>

/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!
"""
    await msg.answer(text, parse_mode='html', reply_markup=menyu)


# Sherik kerak boshi


@dp.message_handler(text='Sherik kerak', state='*')
async def sherik_kerak(msg: types.Message):
    text = """
<b>Sherik topish uchun ariza berish</b>

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.
"""
    await msg.answer(text, parse_mode='html')
    await msg.answer("Ism, familiyangizni kiriting?")
    await Sherik.name.set()


@dp.message_handler(state=Sherik.name)
async def f_n(msg: types.Message, state: FSMContext):
    await state.update_data(ism=msg.text)
    await msg.answer('Texnologiya kiriting')
    await Sherik.texnologiya.set()


@dp.message_handler(state=Sherik.texnologiya)
async def texnologiyaa(msg: types.Message, state: FSMContext):
    await state.update_data(texnologiya=msg.text)
    await msg.answer('Telefon raqam kiriting', reply_markup=phone_number)
    await Sherik.phone.set()



@dp.message_handler(state=Sherik.phone, content_types=types.ContentTypes.CONTACT)
async def tel(msg: types.Message, state: FSMContext):
    await state.update_data(phone=msg.contact.phone_number)
    await msg.answer('Hudud kiriting')
    await Sherik.hudud.set()


@dp.message_handler(state=Sherik.phone)
async def tel(msg: types.Message, state: FSMContext):
    if validate_phone_number(msg.text):
        await state.update_data(phone=msg.text)
        await msg.answer('Hudud kiriting')
        await Sherik.hudud.set()
    else:
        await msg.answer('Telefon raqam xato!')
        await msg.answer('Telefon raqam kiriting', reply_markup=phone_number)
        await Sherik.phone.set()



@dp.message_handler(state=Sherik.hudud)
async def hu(msg: types.Message, state: FSMContext):
    await state.update_data(hudud=msg.text)
    await msg.answer('Narx kiriting')
    await Sherik.narx.set()


@dp.message_handler(state=Sherik.narx)
async def narh(msg: types.Message, state: FSMContext):
    await state.update_data(narx=msg.text)
    await msg.answer('Kasb kiriting')
    await Sherik.kasb.set()


@dp.message_handler(state=Sherik.kasb)
async def ka(msg: types.Message, state: FSMContext):
    await state.update_data(kasb=msg.text)
    await msg.answer('Vaqt kiriting')
    await Sherik.vaqt.set()


@dp.message_handler(state=Sherik.vaqt)
async def va(msg: types.Message, state: FSMContext):
    await state.update_data(vaqt=msg.text)
    await msg.answer('Maqsad kiriting')
    await Sherik.maqsad.set()


@dp.message_handler(state=Sherik.maqsad)
async def ma(msg: types.Message, state: FSMContext):
    await state.update_data(maqsad=msg.text)
    data = await state.get_data()
    user_name = msg.from_user.username
    ism = data.get('ism')
    texnologiya = data.get('texnologiya')
    phone = data.get('phone')
    hudud = data.get('hudud')
    narx = data.get('narx')
    kasb = data.get('kasb')
    vaqt = data.get('vaqt')
    maqsad = data.get('maqsad')
    text = f"""
Sherik kerak:

🏅 Sherik: {ism} 
📚 Texnologiya: {texnologiya} 
🇺🇿 Telegram: @{user_name} 
📞 Aloqa: {phone}
🌐 Hudud: {hudud} 
💰 Narxi: {narx} 
👨🏻‍💻 Kasbi: {kasb}
🕰 Murojaat qilish vaqti: {vaqt} 
🔎 Maqsad: {maqsad} 

#sherik

"""
    
    await msg.answer(text, reply_markup=menyu)
    await state.finish()



# Sherik kerish tugashi


# Ish joy boshi



@dp.message_handler(text='Ish joy kerak', state="*")
async def Ish_kerak(msg: types.Message):
    text = """
<b>Ish joyi topish uchun ariza berish</b>

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.
"""
    await msg.answer(text, parse_mode='html')
    await msg.answer("Ism, familiyangizni kiriting?")
    await Ish_Joyi.name.set()

@dp.message_handler(state=Ish_Joyi.name)
async def f_n(msg: types.Message, state: FSMContext):
    await state.update_data(name=msg.text)
    await msg.answer('''
🕑 Yosh: 

Yoshingizni kiriting?
Masalan, 19''')
    await Ish_Joyi.yosh.set()

@dp.message_handler(state=Ish_Joyi.yosh)
async def f_n(msg: types.Message, state: FSMContext):
    await state.update_data(yosh=msg.text)
    await msg.answer('''
📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#''')
    await Ish_Joyi.texnologiya.set()


@dp.message_handler(state=Ish_Joyi.texnologiya)
async def texnologiyaa(msg: types.Message, state: FSMContext):
    await state.update_data(texnologiya=msg.text)
    await msg.answer('Telefon raqam kiriting', reply_markup=phone_number)
    await Ish_Joyi.phone.set()



@dp.message_handler(state=Ish_Joyi.phone, content_types=types.ContentTypes.CONTACT)
async def tel(msg: types.Message, state: FSMContext):
    await state.update_data(phone=msg.contact.phone_number)
    await msg.answer("""
🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.""")
    await Ish_Joyi.hudud.set()


@dp.message_handler(state=Ish_Joyi.phone)
async def tel(msg: types.Message, state: FSMContext):
    if validate_phone_number(msg.text):
        await state.update_data(phone=msg.text)
        await msg.answer('Hudud kiriting')
        await Ish_Joyi.hudud.set()
    else:
        await msg.answer('Telefon raqam xato!')
        await msg.answer('Telefon raqam kiriting', reply_markup=phone_number)
        await Ish_Joyi.phone.set()



@dp.message_handler(state=Ish_Joyi.hudud)
async def hu(msg: types.Message, state: FSMContext):
    await state.update_data(hudud=msg.text)
    await msg.answer('''
💰 Narxi:

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?''')
    await Ish_Joyi.narx.set()


@dp.message_handler(state=Ish_Joyi.narx)
async def narh(msg: types.Message, state: FSMContext):
    await state.update_data(narx=msg.text)
    await msg.answer('''
👨🏻‍💻 Kasbi: 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba''')
    await Ish_Joyi.kasb.set()


@dp.message_handler(state=Ish_Joyi.kasb)
async def ka(msg: types.Message, state: FSMContext):
    await state.update_data(kasb=msg.text)
    await msg.answer('''
🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00''')
    await Ish_Joyi.vaqt.set()


@dp.message_handler(state=Ish_Joyi.vaqt)
async def va(msg: types.Message, state: FSMContext):
    await state.update_data(vaqt=msg.text)
    await msg.answer('''
🔎 Maqsad: 

Maqsadingizni qisqacha yozib bering.''')
    await Ish_Joyi.maqsad.set()


@dp.message_handler(state=Ish_Joyi.maqsad)
async def ma(msg: types.Message, state: FSMContext):
    await state.update_data(maqsad=msg.text)
    data = await state.get_data()
    ism = data.get('name')
    yosh = data.get('yosh')
    texnologiya = data.get('texnologiya')   
    phone = data.get('phone')
    hudud = data.get('hudud')
    narx = data.get('narx')
    kasb = data.get('kasb')
    vaqt = data.get('vaqt')
    maqsad = data.get('maqsad')
    text = f"""
Ish_Joyi kerak:

🏅 Xodim: {ism} 
🕑 Yosh: {yosh}
📚 Texnologiya: {texnologiya} 
🇺🇿 Telegram: @{msg.from_user.username} 
📞 Aloqa: {phone}
🌐 Hudud: {hudud} 
💰 Narxi: {narx} 
👨🏻‍💻 Kasbi: {kasb}
🕰 Murojaat qilish vaqti: {vaqt} 
🔎 Maqsad: {maqsad} 

#Ish_Joyi

"""
    
    # await msg.answer(text)
    await msg.answer(text, reply_markup=menyu)
    await state.finish()


# Ish joy tugashi


# Xodim kerak boshi



@dp.message_handler(text='Xodim kerak', state="*")
async def Idora(msg: types.Message):
    text = """
<b>Xodim topish uchun ariza berish</b>

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.
"""
    await msg.answer(text, parse_mode='html')
    await msg.answer("Ism, familiyangizni kiriting?")
    await Xodim.Idora.set()

@dp.message_handler(state=Xodim.Idora)
async def f_n(msg: types.Message, state: FSMContext):
    await state.update_data(Idora=msg.text)
    await msg.answer('''
📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#''')
    await Xodim.texnologiya.set()


@dp.message_handler(state=Xodim.texnologiya)
async def texnologiyaa(msg: types.Message, state: FSMContext):
    await state.update_data(texnologiya=msg.text)
    await msg.answer('Telefon raqam kiriting', reply_markup=phone_number)
    await Xodim.phone.set()



@dp.message_handler(state=Xodim.phone, content_types=types.ContentTypes.CONTACT)
async def tel(msg: types.Message, state: FSMContext):
    await state.update_data(phone=msg.contact.phone_number)
    await msg.answer("""
🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.""")
    await Xodim.hudud.set()


@dp.message_handler(state=Xodim.phone)
async def tel(msg: types.Message, state: FSMContext):
    if validate_phone_number(msg.text):
        await state.update_data(phone=msg.text)
        await msg.answer('Hudud kiriting')
        await Xodim.hudud.set()
    else:
        await msg.answer('Telefon raqam xato!')
        await msg.answer('Telefon raqam kiriting', reply_markup=phone_number)
        await Xodim.phone.set()


@dp.message_handler(state=Xodim.hudud)
async def hu(msg: types.Message, state: FSMContext):
    await state.update_data(hudud=msg.text)
    await msg.answer('''
✍️Mas'ul ism sharifi?
''')
    await Xodim.masul.set()


@dp.message_handler(state=Xodim.masul)
async def hu(msg: types.Message, state: FSMContext):
    await state.update_data(masul=msg.text)
    await msg.answer('''
🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00''')
    await Xodim.vaqt.set()


@dp.message_handler(state=Xodim.vaqt)
async def narh(msg: types.Message, state: FSMContext):
    await state.update_data(vaqt=msg.text)
    await msg.answer('''
🕰 Ish vaqtini kiriting?''')
    await Xodim.Ish_vaqti.set()


@dp.message_handler(state=Xodim.Ish_vaqti)
async def ka(msg: types.Message, state: FSMContext):
    await state.update_data(Ish_vaqti=msg.text)
    await msg.answer('''
💰 Maoshni kiriting?''')
    await Xodim.oylik.set()


@dp.message_handler(state=Xodim.oylik)
async def va(msg: types.Message, state: FSMContext):
    await state.update_data(oylik=msg.text)
    await msg.answer('''
‼️ Qo`shimcha ma`lumotlar?''')
    await Xodim.qoshimcha_info.set()


# Xodim tugashi



@dp.message_handler(state=Xodim.qoshimcha_info)
async def ma(msg: types.Message, state: FSMContext):
    await state.update_data(qoshimcha_info=msg.text)
    data = await state.get_data()
    Idora = data.get('Idora')
    texnologiya = data.get('texnologiya')
    Aloqa = data.get('phone')
    hudud = data.get('hudud')
    masul = data.get('masul')
    vaqt = data.get('vaqt')
    Ish_vaqti = data.get('Ish_vaqti')
    oylik = data.get('oylik')
    qoshimcha_info = data.get('qoshimcha_info')
    text = f"""
Xodim kerak:

🏢 Idora: {Idora}
📚 Texnologiya: {texnologiya} 
🇺🇿 Telegram: @{msg.from_user.username} 
📞 Aloqa: {Aloqa} 
🌐 Hudud: {hudud}
✍️ Mas'ul: {masul}
🕰 Murojaat vaqti: {vaqt} 
🕰 Ish vaqti: {Ish_vaqti} 
💰 Maosh: {oylik}
‼️ Qo`shimcha: {qoshimcha_info}
#Xodim

"""
    
    await msg.answer(text)
    await state.finish()


# Ustoz kerak boshi

@dp.message_handler(text='Ustoz kerak', state="*")
async def hodim(msg: types.Message):
    text = """
<b>Ustoz topish uchun ariza berish</b>

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.
"""
    await msg.answer(text, parse_mode='html')
    await msg.answer("Ism, familiyangizni kiriting?")
    await Ustoz.name.set()

@dp.message_handler(state=Ustoz.name)
async def f_n(msg: types.Message, state: FSMContext):
    await state.update_data(name=msg.text)
    await msg.answer('''
🕑 Yosh: 

Yoshingizni kiriting?
Masalan, 19''')
    await Ustoz.yosh.set()

@dp.message_handler(state=Ustoz.yosh)
async def f_n(msg: types.Message, state: FSMContext):
    await state.update_data(yosh=msg.text)
    await msg.answer('''
📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#''')
    await Ustoz.texnologiya.set()


@dp.message_handler(state=Ustoz.texnologiya)
async def texnologiyaa(msg: types.Message, state: FSMContext):
    await state.update_data(texnologiya=msg.text)
    await msg.answer('Telefon raqam kiriting', reply_markup=phone_number)
    await Ustoz.phone.set()



@dp.message_handler(state=Ustoz.phone, content_types=types.ContentTypes.CONTACT)
async def tel(msg: types.Message, state: FSMContext):
    await state.update_data(phone=msg.contact.phone_number)
    await msg.answer("""
🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.""")
    await Ustoz.hudud.set()


@dp.message_handler(state=Ustoz.phone)
async def tel(msg: types.Message, state: FSMContext):
    if validate_phone_number(msg.text):
        await state.update_data(phone=msg.text)
        await msg.answer('Hudud kiriting')
        await Ustoz.hudud.set()
    else:
        await msg.answer('Telefon raqam xato!')
        await msg.answer('Telefon raqam kiriting', reply_markup=phone_number)
        await Ustoz.phone.set()



@dp.message_handler(state=Ustoz.hudud)
async def hu(msg: types.Message, state: FSMContext):
    await state.update_data(hudud=msg.text)
    await msg.answer('''
💰 Narxi:

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?''')
    await Ustoz.narx.set()


@dp.message_handler(state=Ustoz.narx)
async def narh(msg: types.Message, state: FSMContext):
    await state.update_data(narx=msg.text)
    await msg.answer('''
👨🏻‍💻 Kasbi: 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba''')
    await Ustoz.kasb.set()


@dp.message_handler(state=Ustoz.kasb)
async def ka(msg: types.Message, state: FSMContext):
    await state.update_data(kasb=msg.text)
    await msg.answer('''
🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00''')
    await Ustoz.vaqt.set()


@dp.message_handler(state=Ustoz.vaqt)
async def va(msg: types.Message, state: FSMContext):
    await state.update_data(vaqt=msg.text)
    await msg.answer('''
🔎 Maqsad: 

Maqsadingizni qisqacha yozib bering.''')
    await Ustoz.maqsad.set()



# Ustoz tugashi



@dp.message_handler(state=Ustoz.maqsad)
async def ma(msg: types.Message, state: FSMContext):
    await state.update_data(maqsad=msg.text)
    data = await state.get_data()
    ism = data.get('name')
    yosh = data.get('yosh')
    texnologiya = data.get('texnologiya')
    phone = data.get('phone')
    hudud = data.get('hudud')
    narx = data.get('narx')
    kasb = data.get('kasb')
    vaqt = data.get('vaqt')
    maqsad = data.get('maqsad')
    text = f"""
Ustoz kerak:

🏅 Xodim: {ism} 
🕑 Yosh: {yosh}
📚 Texnologiya: {texnologiya} 
🇺🇿 Telegram: @{msg.from_user.username} 
📞 Aloqa: {phone}
🌐 Hudud: {hudud} 
💰 Narxi: {narx} 
👨🏻‍💻 Kasbi: {kasb}
🕰 Murojaat qilish vaqti: {vaqt} 
🔎 Maqsad: {maqsad} 

#Ustoz

"""
    
    await msg.answer(text)
    await state.finish()




# Shogirt kerak boshi



@dp.message_handler(text='Shogirt kerak', state="*")
async def Shogird(msg: types.Message):
    text = """
<b>Shogirt topish uchun ariza berish</b>

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.
"""
    await msg.answer(text, parse_mode='html')
    await msg.answer("Ism, familiyangizni kiriting?")
    await SHogird.name.set()

@dp.message_handler(state=SHogird.name)
async def f_n(msg: types.Message, state: FSMContext):
    await state.update_data(name=msg.text)
    await msg.answer('''
🕑 Yosh: 

Yoshingizni kiriting?
Masalan, 19''')
    await SHogird.yosh.set()

@dp.message_handler(state=SHogird.yosh)
async def f_n(msg: types.Message, state: FSMContext):
    await state.update_data(yosh=msg.text)
    await msg.answer('''
📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#''')
    await SHogird.texnologiya.set()


@dp.message_handler(state=SHogird.texnologiya)
async def texnologiyaa(msg: types.Message, state: FSMContext):
    await state.update_data(texnologiya=msg.text)
    await msg.answer('Telefon raqam kiriting', reply_markup=phone_number)
    await SHogird.phone.set()



@dp.message_handler(state=SHogird.phone, content_types=types.ContentTypes.CONTACT)
async def tel(msg: types.Message, state: FSMContext):
    await state.update_data(phone=msg.contact.phone_number)
    await msg.answer("""
🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.""")
    await SHogird.hudud.set()


@dp.message_handler(state=SHogird.phone)
async def tel(msg: types.Message, state: FSMContext):
    if validate_phone_number(msg.text):
        await state.update_data(phone=msg.text)
        await msg.answer('Hudud kiriting')
        await SHogird.hudud.set()
    else:
        await msg.answer('Telefon raqam xato!')
        await msg.answer('Telefon raqam kiriting', reply_markup=phone_number)
        await SHogird.phone.set()



@dp.message_handler(state=SHogird.hudud)
async def hu(msg: types.Message, state: FSMContext):
    await state.update_data(hudud=msg.text)
    await msg.answer('''
💰 Narxi:

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?''')
    await SHogird.narx.set()


@dp.message_handler(state=SHogird.narx)
async def narh(msg: types.Message, state: FSMContext):
    await state.update_data(narx=msg.text)
    await msg.answer('''
👨🏻‍💻 Kasbi: 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba''')
    await SHogird.kasb.set()


@dp.message_handler(state=SHogird.kasb)
async def ka(msg: types.Message, state: FSMContext):
    await state.update_data(kasb=msg.text)
    await msg.answer('''
🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00''')
    await SHogird.vaqt.set()


@dp.message_handler(state=SHogird.vaqt)
async def va(msg: types.Message, state: FSMContext):
    await state.update_data(vaqt=msg.text)
    await msg.answer('''
🔎 Maqsad: 

Maqsadingizni qisqacha yozib bering.''')
    await SHogird.maqsad.set()


@dp.message_handler(state=SHogird.maqsad)
async def ma(msg: types.Message, state: FSMContext):
    await state.update_data(maqsad=msg.text)
    data = await state.get_data()
    ism = data.get('name')
    yosh = data.get('yosh')
    texnologiya = data.get('texnologiya')
    phone = data.get('phone')
    hudud = data.get('hudud')
    narx = data.get('narx')
    kasb = data.get('kasb')
    vaqt = data.get('vaqt')
    maqsad = data.get('maqsad')
    text = f"""
SHogird kerak:

🏅 Ustoz: {ism} 
🕑 Yosh: {yosh}
📚 Texnologiya: {texnologiya} 
🇺🇿 Telegram: @{msg.from_user.username} 
📞 Aloqa: {phone}
🌐 Hudud: {hudud} 
💰 Narxi: {narx} 
👨🏻‍💻 Kasbi: {kasb}
🕰 Murojaat qilish vaqti: {vaqt} 
🔎 Maqsad: {maqsad} 

#SHogird

"""
    
    await msg.answer(text)
    await state.finish()


# Shogirt kerak tugashi



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)