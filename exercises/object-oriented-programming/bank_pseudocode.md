CLASS Bank EXTENDS ABC

    DEFINE basicinfo
        PRINT generic bank message
        RETURN "Generic bank: 0"

    DEFINE abstract withdraw
        PASS


CLASS Swiss EXTENDS Bank

    DEFINE init
        SET self.bal = 1000

    DEFINE basicinfo
        PRINT Swiss bank message
        RETURN "Swiss Bank: " + balance

    DEFINE withdraw(amount)

        IF amount <= self.bal
            SUBTRACT amount from self.bal
            PRINT withdrawn amount
            PRINT new balance
            RETURN self.bal

        ELSE
            PRINT insufficient funds
            RETURN self.bal


CREATE s = Swiss()

DISPLAY s.basicinfo()
CALL s.withdraw(30)
CALL s.withdraw(1000)