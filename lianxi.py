import redis
conn = redis.Redis(host="192.168.1.250",port=6379,password="shang123")
# key = conn.keys("payment_key_1_*")
# print(key)
# conn.delete(*key)
print(conn.keys())



# print(conn.hgetall('shopping_car_1_2'))