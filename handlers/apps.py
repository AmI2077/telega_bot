from aiogram import Router, F
from aiogram.types import CallbackQuery
import functions

router = Router(name=__name__)

@router.callback_query(F.data == "steam")
async def visual(call: CallbackQuery):
    await call.answer(text = f"Запускаю")
    functions.open_steam()    
    
@router.callback_query(F.data == "discord")
async def visual(call: CallbackQuery):
    await call.answer(text = f"Запускаю")
    functions.open_discord()    
    
