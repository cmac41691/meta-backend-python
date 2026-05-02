# comprehensions_assignment.py

# Input data
employee_list = [
    {"id": 12345, "name": "John", "department": "Kitchen"},
    {"id": 12456, "name": "Paul", "department": "House Floor"},
    {"id": 12478, "name": "Sarah", "department": "Management"},
    {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
    {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
    {"id": 12419, "name": "Gill", "department": "Cashier"}
]


def mod(employee):
    return employee["name"] + "_" + employee["department"]



def to_mod_list(employee_list):
    result_list = []

    for employee in employee_list:
        result = mod(employee)
        result_list.append(result)

    return result_list



def generate_usernames(mod_list):
    usernames = []

    for item in mod_list:
        new_item = item.replace(" ", "_")
        usernames.append(new_item)

    return usernames



def map_id_to_initial(employee_list):
    result_dict = {}

    for employee in employee_list:
        key = employee["name"][0]
        value = employee["id"]
        result_dict[key] = value

    return result_dict




def main():
    mod_emp_list = to_mod_list(employee_list)
    print("Modified employee list:", mod_emp_list)

    print(f"Usernames: {generate_usernames(mod_emp_list)}")

    print(f"Initials and ids: {map_id_to_initial(employee_list)}")


if __name__ == "__main__":
    main()