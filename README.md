Getting User Input:
	•	full_name = input("Enter your full name (first and last name): ")
	  •	Prompts the user to enter their full name and assigns the input to the variable full_name.
	•	monthly_income = float(input("Enter your monthly income: "))
	  •	Prompts the user to enter their monthly income, converts the input to a float, and assigns it to the variable monthly_income.
	•	rent = float(input("Enter your monthly rent expense: "))
	  •	Prompts the user to enter their monthly rent expense, converts the input to a float, and assigns it to the variable rent.
	•	utilities = float(input("Enter your monthly utilities expense: "))
	  •	Prompts the user to enter their monthly utilities expense, converts the input to a float, and assigns it to the variable utilities.
	•	groceries = float(input("Enter your monthly groceries expense: "))
	  •	Prompts the user to enter their monthly groceries expense, converts the input to a float, and assigns it to the variable groceries.
	•	transportation = float(input("Enter your monthly transportation expense: "))
	  •	Prompts the user to enter their monthly transportation expense, converts the input to a float, and assigns it to the variable transportation.
	•	miscellaneous = float(input("Enter your monthly miscellaneous expense: "))
	  •	Prompts the user to enter their monthly miscellaneous expense, converts the input to a float, and assigns it to the variable miscellaneous.
 
	2.	String Manipulation:
	•	full_name_upper = full_name.upper()
	  •	Converts the full name to uppercase using the .upper() method and assigns it to full_name_upper.
	•	print(f"Full name in uppercase: {full_name_upper}")
	  •	Prints the uppercase version of the full name.
	•	full_name_lower = full_name.lower()
	  •	Converts the full name to lowercase using the .lower() method and assigns it to full_name_lower.
	•	print(f"Full name in lowercase: {full_name_lower}")
	  •	Prints the lowercase version of the full name.
	•	char_count = len(full_name.replace(" ", ""))
	  •	Removes all spaces from the full name using .replace(" ", ""), calculates the length of the resulting string using len(), and assigns it to char_count.
	•	print(f"Number of characters in full name (excluding spaces): {char_count}")
	  •	Prints the number of characters in the full name, excluding spaces.
	•	starts_with_a = full_name.startswith('A')
	  •	Checks if the full name starts with the letter ‘A’ using the .startswith('A') method and assigns the result to starts_with_a.
	•	print(f"Full name starts with 'A': {starts_with_a}")
	  •	Prints whether the full name starts with the letter ‘A’.
	•	first_name, last_name = full_name.split()
	  •	Splits the full name into first name and last name using the .split() method and assigns them to first_name and last_name respectively.
	•	print(f"First name: {first_name}")
	  •	Prints the first name.
	•	print(f"Last name: {last_name}")
	  •	Prints the last name.
 
	3.	Arithmetic Operations:
	•	total_expenses = rent + utilities + groceries + transportation + miscellaneous
	  •	Calculates the total monthly expenses by summing all category expenses and assigns the result to total_expenses.
	•	print(f"Total monthly expenses: {total_expenses:.2f}")
	  •	Prints the total monthly expenses, formatted to two decimal places.
	•	remaining_balance = monthly_income - total_expenses
	  •	Calculates the remaining balance by subtracting total expenses from monthly income and assigns the result to remaining_balance.
	•	print(f"Remaining balance: {remaining_balance:.2f}")
	  •	Prints the remaining balance, formatted to two decimal places.
	•	Calculates the percentage of income spent on each category using division and multiplication by 100:
	  •	percent_rent = (rent / monthly_income) * 100
	  •	percent_utilities = (utilities / monthly_income) * 100
	  •	`percent_groceries = (groceries / monthly_income)
