"""
Skills function practice.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE:
"""

def hello_world():

    """
    prints "Hello World"

    >>> hello_world()
    Hello World
    """

    print("Hello World")


def say_hi(name):

    """
    Takes a name as a string and prints "Hi" followed by the name

    >>> say_hi("Balloonicorn")
    Hi Balloonicorn
    """

    print("Hi {}".format(name))
#

def print_product(arg, arg2):
    """
    >>> print_product(3, 5)
    15
    """
    product = arg * arg2
    print(product)


def repeat_string(string_to_repeat, times_to_repeat):

    """
    Takes a string and an integer and prints the string that many times

   >>> repeat_string("Balloonicorn", 3)
    BalloonicornBalloonicornBalloonicorn
    """

    repeated_string = " "
    for x in range(times_to_repeat):
        repeated_string += string_to_repeat
    print(repeated_string)


def print_sign(number):

    """
    Takes an integer and prints "Higher than 0" if higher than zero and "Lower than 0" if lower than zero.
    If the integer is zero, print "Zero"

    >>> print_sign(3)
    Higher than 0

    >>> print_sign(0)
    Zero

    >>> print_sign(-3)
    Lower than 0
    """
    if number > 0:
        print("Higher than 0")
    elif number < 0:
        print("Lower than 0")
    else:
        print("Zero")


def is_divisible_by_three(number):

    """
    Takes an integer and returns a boolean (True or False), depending on whether the number is evenly divisible by 3

    >>> is_divisible_by_three(12)
    True

    >>> is_divisible_by_three(10)
    False
    """

    return number % 3 == 0


def num_spaces(string):

    """
    Takes a sentence as one string and returns the number of spaces

    >>> num_spaces("Balloonicorn is awesome!")
    2

    >>> num_spaces("Balloonicorn is       awesome!")
    8
    """
    return string.count(" ")


def total_meal_price(amount, tax=.15):

    """
    Takes a meal price and a tip percentage. It should return the total amount paid (price + price * tip).
     **However:** passing in the tip percentage should be optional; if not given, it should default to 15%.

    >>> total_meal_price(30)
    34.5

    >>> total_meal_price(30, .3)
    39.0
    """
    return amount + (amount * tax)


def sign_and_parity(number):

    """
    Takes an integer as an argument and returns two pieces of information as strings --- "Positive" or "Negative" and
    "Even" or "Odd". The two strings should be returned in a list.

    >>> sign_and_parity(3)
    ['Positive', 'Odd']

    >>> sign_and_parity(-2)
    ['Negative', 'Even']
    """

    results = []
    if number < 0:
        results.append("Negative")
    else:
        results.append("Positive")
    if number % 2 == 0:
        results.append("Even")
    else:
        results.append("Odd")

    return results



#PART TWO:

def full_title(name, position="Engineer"):

    """
    Takes a name and a job title, making it so the job title defaults to "Engineer" if a job title is not passed in.
    Returns the person's title and name in one string

    >>> full_title("Balloonicorn")
    'Engineer Balloonicorn'

    >>> full_title("Jane Hacks", "Hacker")
    'Hacker Jane Hacks'
    """
    return "{} {}".format(position, name)

def write_letter(recipient, position, sender):
    """
    Takes a recipient name & job title and a sender name, prints the following letter:

       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
       Sincerely, SENDER_NAME.

    >>> write_letter("Jane Hacks", "Hacker", "Balloonicorn")
    Dear Hacker Jane Hacks, I think you are amazing! Sincerely, Balloonicorn
    """
    formatted_string = "Dear {}, I think you are amazing! Sincerely, {}".format(full_title(recipient, position), sender)
    print(formatted_string)

"""

###############################################################################

# PART ONE

# 1. Write a function called 'hello_world' that does not take any arguments and
#    prints "Hello World".


# 2. Write a function called 'say_hi' that takes a name as a string and
#    prints "Hi" followed by the name.


# 3. Write a function called 'print_product' that takes two integers and
#    multiplies them together. Print the result.


# 4. Write a function called 'repeat_string' that takes a string and an integer
#    and prints the string that many times


# 5. Write a function called 'print_sign' that takes an integer and prints
#    "Higher than 0" if higher than zero and "Lower than 0" if lower than zero.
#    If the integer is zero, print "Zero".


# 6. Write a function called 'is_divisible_by_three' that takes an integer and
#    returns a boolean (True or False), depending on whether the number is
#    evenly divisible by 3.


# 7. Write a function called 'num_spaces' that takes a sentence as one string
#    and returns the number of spaces.


# 8. Write a function called 'total_meal_price' that can be passed a meal price
#    and a tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip percentage should
#    be optional; if not given, it should default to 15%.


# 9. Write a function called 'sign_and_parity' that takes an integer as an
#    argument and returns two pieces of information as strings --- "Positive"
#    or "Negative" and "Even" or "Odd". The two strings should be returned in
#    a list.
#
#    Then, write code that shows the calling of this function on a number and
#    unpack what is returned into two variables --- sign and parity (whether
#    it's even or odd). Print sign and parity.


###############################################################################

# PART TWO

# 1. Write a function called full_title that takes a name and a job title as
#    parameters, making it so the job title defaults to "Engineer" if a job
#    title is not passed in. Return the person's title and name in one string.

# 2. Write a function called write_letter that, given a recipient name & job
#    title and a sender name, prints the following letter:
#
#       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
#       Sincerely, SENDER_NAME.
#
#    Use the function from #1 to construct the full title for the letter's
#    greeting.


###############################################################################

# END OF PRACTICE: You can ignore everything below.

"""

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GOOD WORK!")
    print