# TestPackage/Test.py

# Import the functions from the PythonPackageDemo package
from PythonPackageDemo.Geetings import hello, bye

# Now, use the functions in Test.py
def test_call():
    hello("Rakesh")
    bye("Mayank")

if __name__ == "__main__":
    test_call()
