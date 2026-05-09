class Payslip():

    def __init__(self, name, payment_status, amount):
        self.name = name
        self.payment_status = payment_status
        self.amount = amount

    def payment(self):
        self.payment_status = "Paid"

    def current_status(self):

        if self.payment_status == "Paid":
            return self.name + " was paid $" + str(self.amount) 

        else:
            return self.name + " has not been paid"


will = Payslip("Will", "No", 200)

sam = Payslip("Sam", "No", 500)

print(will.current_status())

print(sam.current_status())

will.payment()

print(will.current_status())

