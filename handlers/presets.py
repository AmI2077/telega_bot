from aiogram import Router, F
from aiogram.types import CallbackQuery
import functions

router = Router(name=__name__)

@router.callback_query(F.data == "ami")
async def visual(call: CallbackQuery):
    await call.answer(text = f"Запускаю")
    functions.open_chrome()    
    
@router.callback_query(F.data == "vi")
async def visual(call: CallbackQuery):
    await call.answer(text = f"Запускаю")
    functions.open_edge()    