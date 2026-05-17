global_variable = "This is global"

# ver 0.1
# beginning of LEGB scope
def start_scope():
    local = "This is the start"
    print(local)

# Demonstrates nested scope behavior
def outer_scope():
    enclosed = "Working my way"

    # Inner function will work with outer variable
    def inner_scope():
        nonlocal enclosed
        enclosed = "Changed from inner scope"
        print(enclosed)

    inner_scope()
    print(enclosed)

# end of the scope
def built_in():
    finish_scope = "End of scope"
    return finish_scope

start_scope()
outer_scope()

end_result = built_in()
print(global_variable)
print(end_result)




