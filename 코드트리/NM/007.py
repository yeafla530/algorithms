# class 이용
class Seven:
    def __init__(self, code, loc, time):
        self.code = code
        self.loc = loc
        self.time = time

secret_code, location, time = input().split()
secret = Seven(secret_code, location, time)

print("secret code :", secret.code)
print("meeting point :", secret.loc)
print("time :", secret.time)
