import json
from employee import details, employee_name, age, title 


def create_dict(name, age, title):
    employee_dict = {
        "first_name": employee_name,
        "age": age,
        "title": title
    }

    return employee_dict


def write_json_to_file(employee_dict, employee):
    with open(employee, "w") as f:
        json.dump(employee_dict, f, indent=4)

   


def main():
    details()

    employee_dict = create_dict(employee_name, age, title)

    write_json_to_file(employee_dict, "employee.json")


if __name__ == "__main__":
    main()