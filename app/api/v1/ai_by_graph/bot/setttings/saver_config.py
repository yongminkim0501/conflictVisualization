import os

from app.core.config import settings

if os.getenv("ENV", "local") == "production":
    from langgraph.checkpoint.redis.aio import AsyncRedisSaver
    checkpointer = AsyncRedisSaver(redis_url=settings.REDIS_URL)
else:
    from langgraph.checkpoint.memory import MemorySaver
    checkpointer = MemorySaver()