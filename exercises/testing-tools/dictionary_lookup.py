soft_drinks = {
    1: "Coke",
    2: "Pepsi",
    3: "Mountain Dew",
    4: "Root Beer",
}


def get_drink(drink_id):
    if drink_id in soft_drinks:
        return soft_drinks[drink_id]
    else:
        return "Not Found"