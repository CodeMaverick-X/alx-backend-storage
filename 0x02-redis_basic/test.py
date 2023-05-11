import redis

r = redis.Redis()

print(r.get('broo'))
