class Logger():
    # Constructor
    def __init__(self):
        print("Logger object has beencreated")

    # Distructor
    def __del__(self):
        print("Logger object has been deleted")

# Create an object of the Logger class
logger = Logger()

# Delete the object explicitly to invoke the distructor
del logger

