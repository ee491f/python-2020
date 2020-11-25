def my_function(first_name = "John", last_name = "Doe"):
  print(f"Hello {first_name} {last_name} from a function")

# these method calls should all be done in a file that is not defining the function
#my_function( # keyword arguments are more flexible and readable
#    last_name = 'Flinstone',
#    first_name = 'Fred',
#)
#
#my_function('Flinstone', 'Fred') # positional arguments are more brittle and rigid
#
#my_function() # use defaults

def function_using_more_organization(
    person = {
        "first": "John",
        "last": "Doe",
    },
    address = {
        "number": "123",
        "street": "Main St",
    }
):
  print(f"Hello {person['first']} of {address['street']} from a more organized function")

# these method calls should all be done in a file that is not defining the function
#function_using_more_organization(
#    person = {
#        "first": "Jane"
#    }
#)