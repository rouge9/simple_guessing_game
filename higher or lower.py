import art
from game_file import data
import random

def random_generator():
    random_number = random.randint(0,49)
    return random_number

def game_checker(a,b):
    if a['follower_count'] < b['follower_count']:
        return "b"
    else:
        return "a"

compare_a = data[random_generator()]
compare_b = data[random_generator()]
did_u_lose = False
score = 0
while not did_u_lose:
    print(art.higher)
    print(f"compare a {compare_a['name'],compare_a['description'],compare_a['country']} ")
    print(art.vs)
    print(f"against b {compare_b['name'],compare_b['description'],compare_b['country']}")

    choice = input("type a or b = ")
    if choice == game_checker(compare_a,compare_b):
        compare_a = compare_b
        compare_b = data[random_generator()]
        score+=1
    else:
        print(f"you lose:::: your score is {score}")
        did_u_lose = True



