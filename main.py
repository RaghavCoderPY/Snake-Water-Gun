import random as r

price = 0
choices = ("snake", "water", "gun")


def add_price(award):
    global price
    price = price + award


if __name__ == "__main__":
    print("Welcome to Snake Water Game")

    while True:
        robot = r.choice(choices)
        user = input("Your Turn: ").lower()

        if user == robot:
            print("Same, No One Win")
        elif (user == "snake" and robot == "water") or (user == "water" and robot == "gun") or (
                user == "gun" and robot == "snake"):
            print("User wins because robot is {} and user is {}".format(robot, user))
            add_price(5000)
        elif (robot == "snake" and user == "water") or (robot == "water" and user == "gun") or (
                robot == "gun" and user == "snake"):
            print("Robot wins because user is {} and robot is {}".format(user, robot))
            add_price(5000)
