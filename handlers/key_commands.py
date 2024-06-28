from aiogram import Router, F
from aiogram.types import Message
import keyboards

router = Router(name=__name__)

@router.message(F.text == "Музыка")
async def choose_music(message: Message):   
    await keyboards.inline_music(message=message)

@router.message(F.text == "Игры")
async def games(message: Message):
    await keyboards.inline_games(message = message)
      
@router.message(F.text == "Приложения")
async def games(message: Message):
    await keyboards.inline_apps(message = message)
    
@router.message(F.text == "Пресеты")
async def games(message: Message):
    await keyboards.inline_presets(message = message)   
    
@router.message(F.text == "Эдиторы")
async def games(message: Message):
    await keyboards.inline_editors(message = message)
