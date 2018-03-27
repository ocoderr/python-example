from datetime import datetime, timedelta, timezone

# 当前时间
now = datetime.now()
print(now)
print(now.strftime('%Y-%m-%d %H:%M:%S'))

# 指定时间
aday = datetime(2015, 4, 9, 12, 20)
print(aday)
print(aday.timestamp())  # 获得对应时间戳，Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
print(aday.strftime('%Y-%m-%d %H:%M:%S'))

# 通过时间戳
print(datetime.fromtimestamp(1428553200.0))  # 本地时间，timestamp的值与时区毫无关系
print(datetime.utcfromtimestamp(1428553200.0))  # UTC时间，timestamp的值与时区毫无关系

# 通过字符串
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

# 时间的加减
now = datetime.now()

print(now + timedelta(hours=10))  # 加10小时
print(now - timedelta(days=1))

# 关于时区
utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00

print(now)
dt = now.replace(tzinfo=utc_8)
print(dt)


# 时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。
# 利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。
utc_9 = timezone(timedelta(hours=9))  # 创建时区UTC+8:00
print(dt,'--->',dt.astimezone(utc_9)) # 转换时区