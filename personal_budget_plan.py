# Personal Budget Plan

# 1. Getting User Input:
# Prompt the user to enter their full name (first and last name)
full_name = input("Enter your full name (first and last name): ")
# Prompt the user to enter their monthly income and convert it to float
monthly_income = float(input("Enter your monthly income: "))
# Prompt the user to enter their monthly expenses for various categories and convert them to float
rent = float(input("Enter your monthly rent expense: "))
utilities = float(input("Enter your monthly utilities expense: "))
groceries = float(input("Enter your monthly groceries expense: "))
transportation = float(input("Enter your monthly transportation expense: "))
miscellaneous = float(input("Enter your monthly miscellaneous expense: "))

# 2. String Manipulation:
# Convert full name to uppercase and print it
# .upper() method converts all characters in the string to uppercase
full_name_upper = full_name.upper()
print(f"Full name in uppercase: {full_name_upper}")

# Convert full name to lowercase and print it
# .lower() method converts all characters in the string to lowercase
full_name_lower = full_name.lower()
print(f"Full name in lowercase: {full_name_lower}")

# Count the number of characters in the full name, excluding spaces, and print it
# .replace(" ", "") removes all spaces in the string
# len() function returns the length of the string
char_count = len(full_name.replace(" ", ""))
print(f"Number of characters in full name (excluding spaces): {char_count}")

# Check if the full name starts with the letter 'A' and print the result
# .startswith('A') checks if the string starts with the character 'A'
starts_with_a = full_name.startswith('A')
print(f"Full name starts with 'A': {starts_with_a}")

# Extract the first name and last name by splitting the full name string
# .split() method splits the string into a list of substrings using whitespace as the delimiter
first_name, last_name = full_name.split()
print(f"First name: {first_name}")
print(f"Last name: {last_name}")

# 3. Arithmetic Operations:
# Calculate total monthly expenses by summing all category expenses and print the total
# The sum of rent, utilities, groceries, transportation, and miscellaneous expenses
total_expenses = rent + utilities + groceries + transportation + miscellaneous
print(f"Total monthly expenses: {total_expenses:.2f}")

# Calculate the remaining balance after expenses and print it
# Subtract total expenses from monthly income to get the remaining balance
remaining_balance = monthly_income - total_expenses
print(f"Remaining balance: {remaining_balance:.2f}")

# Calculate and print the percentage of income spent on each category using division
# Divide each category expense by the monthly income and multiply by 100 to get the percentage
percent_rent = (rent / monthly_income) * 100
percent_utilities = (utilities / monthly_income) * 100
percent_groceries = (groceries / monthly_income) * 100
percent_transportation = (transportation / monthly_income) * 100
percent_miscellaneous = (miscellaneous / monthly_income) * 100

# Print the percentages with the word 'percent'
print(f"Percentage of income spent on rent: {percent_rent:.2f} percent")
print(f"Percentage of income spent on utilities: {percent_utilities:.2f} percent")
print(f"Percentage of income spent on groceries: {percent_groceries:.2f} percent")
print(f"Percentage of income spent on transportation: {percent_transportation:.2f} percent")
print(f"Percentage of income spent on miscellaneous: {percent_miscellaneous:.2f} percent")

# 4. Conditionals:
# Check the remaining balance and print the corresponding financial status message
# If remaining balance is greater than 0, print "You are within your budget."
if remaining_balance > 0:
    financial_status = "You are within your budget."
# If remaining balance is equal to 0, print "You have exactly balanced your budget."
elif remaining_balance == 0:
    financial_status = "You have exactly balanced your budget."
# If remaining balance is less than 0, print "You are over your budget."
else:
    financial_status = "You are over your budget."
print(financial_status)

# 5. Formatted Strings:
# Create and print a formatted string with the user's full name, total income, total expenses, and remaining balance
# Use f-strings to include variables within the string
formatted_string = (
    f"Hello, {full_name}. Your total income is {monthly_income:.2f}, "
    f"your total expenses are {total_expenses:.2f}, and your remaining balance is {remaining_balance:.2f}."
)
print(formatted_string)

# Create and print another formatted string with the user's full name and the number of characters in their name
# Use f-strings to include variables within the string
formatted_string_name_count = (
    f"Your name, {full_name}, has {char_count} characters."
)
print(formatted_string_name_count)
