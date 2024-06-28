from aiogram import Router, F
from aiogram.types import Message
import functions


router = Router(name=__name__)


@router.message(F.text == r"/Ami")
async def command_for_ami(message: Message):
    await message.answer("na")
    functions.open_chrome()
    
@router.message(F.text == r"/Vi")
async def command_for_ami(message: Message):
    await message.answer("на")
    functions.open_edge()    

@router.message(F.text == r"/Aiden")
async def command_for_ami(message: Message):
    await message.answer("")
    functions.open_dying_lite()
    
@router.message(F.text == r"/Samurai")
async def command_for_ami(message: Message):
    await message.answer("на")
    functions.open_ghost_thusima()     
    
@router.message(F.text == r"/Talk")
async def command_for_ami(message: Message):
    await message.answer("ща запущу")
    functions.open_discord()
    
@router.message(F.text == r"/Smoke")
async def command_for_ami(message: Message):
    await message.answer("на")
    functions.open_steam()    
    
@router.message(F.text == r"/info")
async def command_for_ami(message: Message):
    await message.answer("на")
    chrome_name = 'chrome.exe'
    #all_apps = ['Steam.exe', f'{chrome_name}', 'notepad.exe']
    #all_apps = [f'{chrome_name}']
    #for app in all_apps:
    functions.is_app_run(chrome_name)
            
            
@router.message(F.text == r"/info_all")
async def command_for_ami(message: Message):
    await message.answer("на")
    functions.all_running_apps()