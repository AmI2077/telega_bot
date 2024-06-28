from aiogram import Router, F
from aiogram.types import CallbackQuery
import functions

router = Router(name=__name__)

@router.callback_query(F.data == "visual_studio")
async def visual(call: CallbackQuery):
    await call.answer(text = f"Запускаю")
    functions.open_visual_studio()    
    
@router.callback_query(F.data == "vs_code")
async def visual(call: CallbackQuery):
    await call.answer(text = f"Запускаю")
    functions.open_vs_code()    
    
@router.callback_query(F.data == "unreal_engine")
async def visual(call: CallbackQuery):
    await call.answer(text = f"Запускаю")
    functions.open_unreal()    
    
@router.callback_query(F.data == "aseprite")
async def visual(call: CallbackQuery):
    await call.answer(text = f"Запускаю")
    functions.open_aseprite()    