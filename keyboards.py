from aiogram.types import Message
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.types.inline_keyboard_button import InlineKeyboardButton


async def keyboard(message: Message):
    keyboard = [
        [KeyboardButton(text='Игры')],
        [KeyboardButton(text='Приложения')],
        [KeyboardButton(text='Эдиторы')],
        [KeyboardButton(text='Пресеты')], 
        [KeyboardButton(text='Музыка')]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
    await message.answer("Выбирай", reply_markup=keyboard)
    
    
async def inline_games(message: Message):
    zombi_button = InlineKeyboardButton(text="Месить зомби", callback_data="zombi")
    ghost_button = InlineKeyboardButton(text="Махать катаной", callback_data="katana")
    row_first = [zombi_button]
    row_sec = [ ghost_button]
    rows = [row_first, row_sec]
    keyboard = InlineKeyboardMarkup(inline_keyboard=rows)
    await message.answer("Сегодня ты будешь: ", reply_markup=keyboard)
    
    
async def inline_apps(message: Message):
    steam_button = InlineKeyboardButton(text="Steam", callback_data="steam")
    discord_button = InlineKeyboardButton(text="Ds", callback_data="discord")
    row = [steam_button, discord_button]
    rows = [row]
    keyboard = InlineKeyboardMarkup(inline_keyboard=rows)
    await message.answer("Сегодня ты будешь: ", reply_markup=keyboard)
    
async def inline_editors(message: Message):
    visual_button = InlineKeyboardButton(text="Visual Studio", callback_data="visual_studio")
    vs_code_button = InlineKeyboardButton(text="VS Code", callback_data="vs_code")
    ureal_button = InlineKeyboardButton(text="Unreal Engine", callback_data="unreal_engine")
    pixel_button = InlineKeyboardButton(text="Aseprite", callback_data="aseprite")
    row1 = [visual_button]
    row2 = [vs_code_button]
    row3 = [ureal_button]
    row4 = [pixel_button]
    rows = [row1, row2, row3, row4]
    keyboard = InlineKeyboardMarkup(inline_keyboard=rows)
    await message.answer("Сегодня ты будешь: ", reply_markup=keyboard)
    
    
async def inline_presets(message: Message):
    ami_button = InlineKeyboardButton(text="Ami", callback_data="ami")
    vi_button = InlineKeyboardButton(text="Vi", callback_data="vi")
    row = [ami_button, vi_button]
    rows = [row]
    keyboard = InlineKeyboardMarkup(inline_keyboard=rows)
    await message.answer("Сейчас ты: ", reply_markup=keyboard)
 
 
 
    
async def inline_music(message: Message):
    """buttons"""
    hills_button = InlineKeyboardButton(text="LILDrugHILL", url="https://music.yandex.ru/artist/5608970")
    mark_button = InlineKeyboardButton(text="Markul", url="https://music.yandex.ru/artist/2938031")
    mayot_button = InlineKeyboardButton(text="Mayot", url="https://music.yandex.ru/artist/6312364")
    bbt_button = InlineKeyboardButton(text="BBT", url="https://music.yandex.ru/artist/5701276")
    aarne_button = InlineKeyboardButton(text="Aarnemba", url="https://music.yandex.ru/artist/494394")
    kristina_button = InlineKeyboardButton(text="LIL Kristina", url="https://music.yandex.ru/artist/5766526")
    platina_button = InlineKeyboardButton(text="Платина", url="https://music.yandex.ru/artist/6531894")
    friendly_button = InlineKeyboardButton(text="Friendly Thug NGG 52", url="https://music.yandex.ru/artist/12666124")
    allblack_button = InlineKeyboardButton(text="Alblak 52", url="https://music.yandex.ru/artist/17303154")
    scrip_button = InlineKeyboardButton(text="Скриптонит", url="https://music.yandex.ru/artist/3246342")
    fludd_button = InlineKeyboardButton(text="Gone Fludda", url="https://music.yandex.ru/artist/4865954")
    rocket_button = InlineKeyboardButton(text="Rocketaa", url="https://music.yandex.ru/artist/5625690")
    kai_button = InlineKeyboardButton(text="Kai AMC", url="https://music.yandex.ru/artist/16509384")
    saluki_button = InlineKeyboardButton(text="Saluki", url="https://music.yandex.ru/artist/4439056")
    obla_button = InlineKeyboardButton(text="Obladaet", url="https://music.yandex.ru/artist/3676308")
    anikv_button = InlineKeyboardButton(text="Anikv", url="https://music.yandex.ru/artist/6914440")
    monetka_button = InlineKeyboardButton(text="Монеточка(не ЛСП)", url="https://music.yandex.ru/artist/4623000")
    
    """rows"""
    row0 = [mark_button]
    row1 = [saluki_button]
    row2 = [anikv_button, monetka_button]
    row3 = [hills_button]
    row4 = [rocket_button]
    row5 = [kristina_button, obla_button]
    row6 = [aarne_button, platina_button]
    row7 = [friendly_button]
    row8 = [allblack_button, bbt_button]
    row9 = [scrip_button]
    row10 = [fludd_button]
    row11 = [kai_button, mayot_button]
    
    """klava"""
    rows = [row0, row1, row2, row3, row4, row5, row6, row7, row8, row9, row10, row11]
    keyboard = InlineKeyboardMarkup(inline_keyboard=rows)
    await message.answer("Седня я слушаю  ", reply_markup=keyboard)