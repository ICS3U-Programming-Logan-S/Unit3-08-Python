# Python program to check if year is a leap year or not


def main():

    # year = 2000

    # To get year (integer input) from the user
    year = input("Enter a year: ")

    try:
        year_integer = int(year)
        if (year_integer % 4) == 0:
            if (year_integer % 100) == 0:
                if (year_integer % 400) == 0:
                    print()
                    print("{} is a leap year!".format(year))
                    print()
                else:
                    print()
                    print("{} is not a leap year.".format(year))
                    print()
            else:
                print()
                print("{} is a leap year!".format(year))
                print()
        else:
            print()
            print("{} is not a leap year.".format(year))
            print()
    except Exception:
        print()
        print("That's not a year...")
        print()
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
