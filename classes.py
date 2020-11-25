class Greeter:
    def __init__(self, message = "hello, world"):
        self.message = message

    def greet(self):
        print(self.message)

# these method calls should all be done in a file that is not defining the Greeter class
#greeter1 = Greeter()
#greeter1.greet()
#
#greeter2 = Greeter("bye, world")
#greeter2.greet()
#
#greeter3 = Greeter("some other message")
#greeter3.greet()
#
#greeter2.greet()