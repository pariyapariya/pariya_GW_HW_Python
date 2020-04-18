# Initial variable to track game play
user_continue = "y" 

# Set start and last number
start_num = 0

# While we are still playing...
while user_continue == "y":

    # Ask the user how many numbers to loop through
    user_input = input("How many numbers?  ")

    # Loop through the numbers. (Be sure to cast the string into an integer.)
    for x in range(start_num, int(user_input)+start_num):

        # Print each number in the range
        print(x)
        
    # Set the next start number as the last number of the loop
    start_num = start_num + int(user_input)
    
    # Once complete... ask if the user wants to continue
    user_continue = input("Want to continue? Type 'y' if so.   ")

