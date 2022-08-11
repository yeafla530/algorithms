# CLASS
# class Charactor:
#     def __init__(self, user="", level=0):
#         self.user = user
#         self.level = level
    
# user, lv = input().split()

# c1 = Charactor('codetree', 10)
# c2 = Charactor(user, lv)

# print("user", c1.user, "lv", c1.level)
# print("user", c2.user, "lv", c2.level)

# tuple
user1 = ("codetree", 10)
user2 = tuple(input().split())

for user_id, lv in [user1, user2]:
    print(f"user {user_id} lv {lv}")
