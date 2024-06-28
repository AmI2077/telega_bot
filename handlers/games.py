from aiogram import Router, F
from aiogram.types import CallbackQuery
import functions

router = Router(name=__name__)

@router.callback_query(F.data == "zombi")
async def visual(call: CallbackQuery):
    await call.answer(text = f"Запускаю")
    functions.open_dying_lite()    
    
@router.callback_query(F.data == "katana")
async def visual(call: CallbackQuery):
    await call.answer(text = f"Запускаю")
    functions.open_ghost_thusima()    