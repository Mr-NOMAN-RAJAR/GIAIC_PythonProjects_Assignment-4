def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def run():
    try:
        user_input = input("Enter a year to check: ")
        year = int(user_input)
        if check_leap_year(year):
            print("Yes! It's a leap year.")
        else:
            print("Nope, that's not a leap year.")
    except ValueError:
        print("Please enter a valid numeric year.")

if __name__ == '__main__':
    run()

