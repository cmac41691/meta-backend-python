import time


def make_coffee():
    cup = "coffee_cup"
    utils = "spoon"

    print("Cup:", cup)
    print("Tool:", utils)

    heating_water()

    pour_instant_coffee(
        cup,
        ["add coffee", "pour water"]
    )

    mix_it()
    let_it_cool()
    coffee_is_ready(cup)


def heating_water():
    while True:
        kettle_water = input("is the water starting to boil? ").strip().lower()

        match kettle_water:
            case "stir":
                print("Spoon clanking")
            case "proceed":
                print("mix it good")
            case "stop":
                print("alright that's good enough")
                break
            case _:
                print("unknown input")


def pour_instant_coffee(cup, additives):
    print("Getting your coffee ready", cup)

    for additive in additives:
        print(additive)


def mix_it():
    spoon = input("Is the spoon ready? ").strip().lower()

    if spoon == "yes":
        for _ in range(10):
            print("mixing...")
    else:
        print("Did you get the spoon?")


def let_it_cool():
    print("Coffee is hot, don't drink it yet!")

    while True:
        drink_ready = input("Is it ready to drink? ").strip().lower()

        if drink_ready == "yes":
            print("Coffee is ready to consume")
            break
        elif drink_ready == "no":
            print("Cooling down now")
            time.sleep(3)
        else:
            print("Input yes or no")


def coffee_is_ready(cup):
    print("Coffee is ready! Enjoy.")
    return cup


if __name__ == "__main__":
    make_coffee()