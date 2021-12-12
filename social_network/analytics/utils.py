import datetime
from datetime import timedelta

from django.utils.timezone import now
from django.conf import settings

from redis import Redis


r = Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB,
)


def today_stats_key():
    return stats_key(now().date())


def stats_key(date):
    return f"likes_for{date.strftime('%y-%m-%d')}"


def update_stats(decrease=False):
    if decrease:
        r.decr(today_stats_key())
    else:
        if not r.get(today_stats_key()):
            r.set(today_stats_key(), 1)
            return

        r.incr(today_stats_key())


def get_stats_for(date):
    data = r.get(stats_key(date))
    if not data:
        return 0

    return int(data.decode())


def get_stats(from_date, to_date):
    result = {}

    dates = [from_date + timedelta(days=i) for i in range((to_date - from_date).days + 1)]

    for date in dates:
        result[date.strftime("%Y-%m-%d")] = get_stats_for(date)

    return result
