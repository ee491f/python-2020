from classes import Greeter # defining classes in separate files is a commonly used pattern
from functions import my_function, function_using_more_organization # functions are typically used with 3rd party libraries and less used within our own custom code
# import data_types # most often you want to import classes/functions to be used instead of calling another script
from package.another_greeter import AnotherGreeter

greeter = Greeter()
greeter.greet()
my_function()
function_using_more_organization()

another_greeter = AnotherGreeter()
another_greeter.greet()
