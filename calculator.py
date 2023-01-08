"""
This a simple calculator which takes 2 numbers and an operation as an input (in the form of a string).
It also gives the user the option to read data that is formatted in the same manner
from a text file and calculate the results

for testing reading from operations.txt has correct input formatting, whereas test.txt has a mixture of correct
and incorrect formatting
"""

import os


# function for handling data, returns tuple of calculation result, and output for writing to file
# on error it will return a tuple of (0, "Error"), "Error" will be used to keep the loop going
def input_handler(operation: list) -> tuple:
    # check length of operation list (should be 3, 2 numbers and an operation)
    if len(operation) != 3:
        print("You have entered data in the incorrect format, please try again")
        return 0, "Error"
    else:
        try:
            # assign numbers 1 and 2 from operation list and cast to float
            number_1 = float(operation[0])
            number_2 = float(operation[1])

            # assign operator from the operation list
            operator = operation[2]

            # match on the operation
            match operator:
                case "+":
                    # calculate the result, join operation list for text output to write data
                    result = number_1 + number_2
                    text_output = " ".join(operation)

                    return result, text_output
                case "-":
                    # calculate the result, join operation list for text output to write data
                    result = number_1 - number_2
                    text_output = " ".join(operation)

                    return result, text_output
                case "x" | "X" | "*":
                    # calculate the result, join operation list for text output to write data
                    result = number_1 * number_2
                    text_output = " ".join(operation)

                    return result, text_output
                case "/":
                    # calculate the result, join operation list for text output to write data
                    result = number_1 / number_2
                    text_output = " ".join(operation)

                    return result, text_output
                case _:
                    print(f"{operator} is not a valid operation")
                    return 0, "Error"
        except ValueError as error:
            print(f"Cannot convert to a float:\n{error}")
            return 0, "Error"
        except ZeroDivisionError:
            print("Cannot divide by 0!")
            return 0, "Error"


# function for writing to file
def data_write(write_data: str, file: str = "operations"):
    # check file exists
    if os.path.exists(f"./{file}.txt"):
        # open file in append mode for saving operations (if file exists)
        with open(file=f"./{file}.txt", mode="a") as operations_file:
            # write the data to the file (with a new line)
            operations_file.write(write_data + "\n")
    else:
        # open file in write mode if it doesn't exist
        with open(file=f"./{file}.txt", mode="w") as operations_file:
            # write the data to the file (with a new line)
            operations_file.write(write_data + "\n")


# function for reading from file, returns a string for validation
def data_read(file: str) -> str:
    try:
        with open(file=f"./{file}.txt", mode="r") as read_file:
            # get data from file
            file_data = read_file.readlines()

            # list comprehension to strip \n and split on white space
            calc_list = [
                calc.strip("\n").split() for calc in file_data
            ]

            # loop through calc list and calculate results
            for i, calc in enumerate(calc_list, start=1):
                # get result for each calculation
                output, data = input_handler(calc)

                # get number 1, 2, and operation for display
                number_1 = calc[0]
                number_2 = calc[1]
                operation = calc[2]

                # display result if there isn't an error, show data that is formatted incorrectly otherwise
                if data != "Error":
                    print(f"{number_1} {operation} {number_2} = {output}")
                else:
                    # display which line of data has an error, including the list that was passed into the function
                    print(f"Line {i} ({calc}) in {file}.txt is not formatted correctly.\n")

        # return a string to validate on breaking out of loop
        return "Done"

    except FileNotFoundError:
        # display to user that file couldn't be found
        print(f"File: {file}.txt cannot be found, please try again")

        # return a string to validate on breaking out of loop
        return "Failed"


# loop until expected input is entered
while True:
    # ask user if they would like to calculate from a file or from entry
    choice = input("Would you like to calculate from a file or manually enter a calculation?"
                   "\n(enter f or m)\n> ").lower()

    # check user choice (m is manual calculation)
    if choice == "m":
        while True:
            # ask for input, split on white space and assign to list
            calc_data = input("Enter 2 numbers followed by an operation\n(+ | x | - | /)\ne.g. 10 22 +\n> ").split()

            # pass user input into input handler, get result and text for writing (or error) from function
            calc_result, text = input_handler(operation=calc_data)

            # break if there is no error from the function
            if text != "Error":
                break

        # display result
        print(calc_result)

        # write calculation input to default text file, and break
        data_write(text)
        break

    elif choice == "f":
        # loop until a valid file is typed
        while True:
            # ask user for the file name
            file_to_read = input("Which file would you like to read from?\n"
                                 "(enter filename without file extension, must be a txt file)\n> ")

            # pass file name to data_read function, returns "Done" if it ran without error
            status = data_read(file=file_to_read)

            # check the function ran without error, break out of loop if it did
            if status == "Done":
                break

        # break from loop
        break
    else:
        print(f"{choice} is not a valid option, please try again.")
