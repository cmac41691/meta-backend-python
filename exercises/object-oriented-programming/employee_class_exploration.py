"""
Employee Class Exploration

Practicing OOP concepts:
- attributes
- methods
- object behavior
"""

class Employee:
    def __init__(self, name, badge_id):
        self.name = name
        self.badge_id = badge_id
        self.can_go = True

    def credentials(self):
        return f"{self.name} ({self.badge_id})"

    def station(self, target):
        print(f"{self.name} is assigned to {target}")

    def clock_out(self):
        self.can_go = False
        print(f"{self.name} can head home")


# Creating objects
p1 = Employee("Coady", 536321)
p2 = Employee("Jenny", 687458)

print(p1.credentials())
print(p2.credentials())

p1.station("Assembly Line")
p2.station("Quality Control")    

p1.clock_out()
p2.clock_out()