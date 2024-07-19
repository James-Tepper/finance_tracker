import adapters.database as db
import redis

from app import settings
from app.server import clients


async def start():
    await _start_database()
    await _start_redis()

async def stop():
    await _stop_database()
    await _stop_redis()

async def _start_database():
    clients.database = db.Database(
        url=db.dsn(
            db_scheme=settings.DB_SCHEME,
            db_user=settings.DB_USER,
            db_port=settings.DB_PORT,
            db_host=settings.DB_HOST,
            db_pass=settings.DB_PASS,
            db_name=settings.DB_NAME,
        )
    )
    await clients.database.connect()


async def _start_redis():
    clients.redis = redis.Redis(
        host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB
    )

async def _stop_database():
    await clients.database.disconnect()
    del clients.database


async def _stop_redis():
    await clients.redis.quit()
    del clients.redis
