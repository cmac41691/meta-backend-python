# Define class MyFirstClass
class MyFirstClass:

    print("Who wrote this?")

    # Define string variable called index
    index = "Author-book"

    # Define function hand_list()
    def hand_list(self, philosopher, book):
        print(MyFirstClass.index)

        # variable + " wrote the book: " + variable
        print(philosopher + " wrote the book: " + book)


# Object created to call class
whodunnit = MyFirstClass()

# Call function hand_list()
whodunnit.hand_list("Sun Tzu", "The Art of War")