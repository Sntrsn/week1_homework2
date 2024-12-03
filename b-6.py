import random


num_faces = int(input("面の数："))
num_trials = int(input("試行回数："))


daice = [random.randint(1, num_faces) for _ in range(1, num_trials + 1)]
print(daice)
