
class Employee:
    # Public variable
    name = "John"

    # Protected Variable
    _salary = 10000

    # Private Variable
    __ssn: int = 123-456-789

    # Creating an object of Employee class

emp = Employee()

# Accessing the public variable
print("Name:", emp.name)

# Accessing the protected variable
print("Salary:", emp._salary)

# Accessing the private variable (This will raise an error)
try:
    print("SSN:", emp.__ssn)
except AttributeError as e:
    print("Error:", e)

# Accessing the private variable using name mangling
print(f"SSN (via name mangling):", emp._Employee__ssn)


