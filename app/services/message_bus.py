import json
import redis

from app.config import settings

redis_client = redis.Redis.from_url(settings.redis_url, decode_responses=True)


def publish_event(channel: str, payload: dict):
    redis_client.publish(channel, json.dumps(payload))


def get_redis():
    return redis_client
