import keyboards
import asyncio
from keyboards import Message
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart

from handlers import router as handlers_router 
TOKEN = "7489440249:AAGBPWNLbtfjdmBLfFPyQ08_HOb7qqktAb0"
dp = Dispatcher()
bot = Bot(TOKEN)

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await keyboards.keyboard(message=message)
    await message.answer("")

@dp.message(F.text == r"/secret_commands")   
async def secret(message: Message):
    await message.answer("Топ сикрет коммандс: \n/Ami - chrome пресет \n/Vi - edge пресет \n/Aiden - месит зомбаков \n"
                         "/Samurai - черт с катаной \n/Talk - штука чтобы говорить \n/Smoke - запустить пар" ) 
      
                
async def main():
    dp.include_router(handlers_router)
    await dp.start_polling(bot)
    await bot.get_updates(offset = -1)

if __name__ == "__main__":
    asyncio.run(main())    