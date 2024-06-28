from aiogram import Router
from .editors import router as editors_router
from .games import router as games_router
from .apps import router as apps_router
from .presets import router as presets_router
from .key_commands import router as music_router
from .secret_commands import router as secret_router

router = Router()
router.include_router(games_router)
router.include_router(apps_router)
router.include_router(editors_router)
router.include_router(presets_router)
router.include_router(music_router)
router.include_router(secret_router)


__all__ = ["router"]