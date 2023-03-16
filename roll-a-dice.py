import random 

def rolldice(min, max):
    while True:
        print("Rolling the dice ...")
        print(f"your number: {random.randint(min, max)}")
        response = input("Do you want to roll the dice again? (y/n)")
        if response.lower() == 'n':
            break

rolldice(1,6)
