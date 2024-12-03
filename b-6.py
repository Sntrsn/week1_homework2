import random

num_faces = int(input("面の数："))
num_trials = int(input("試行回数："))

for i in range(1, num_trials):
    print(random.randint(1, num_faces), end=", ")
