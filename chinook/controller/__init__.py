from fastapi import APIRouter

from .album import router as album_router
from .artist import router as artist_router
from .customer import router as customer_router
from .employee import router as employee_router
from .genre import router as genre_router
from .invoice import router as invoice_router
from .invoice_item import router as invoice_item_router
from .media_type import router as media_type_router
from .playlist import router as playlist_router
from .playlist_track import router as playlist_track_router
from .track import router as track_router

apis = APIRouter()
apis.include_router(album_router)
apis.include_router(artist_router)
apis.include_router(customer_router)
apis.include_router(employee_router)
apis.include_router(genre_router)
apis.include_router(invoice_router)
apis.include_router(invoice_item_router)
apis.include_router(media_type_router)
apis.include_router(playlist_router)
apis.include_router(playlist_track_router)
apis.include_router(track_router)

__all__ = ["apis"]
