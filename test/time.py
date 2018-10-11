import time;

print(time.ctime());
print("%s-%s"%("aaa", "bbb"));

print(time.localtime());
print(time.strftime("%Y-%m-%d", time.localtime()));
