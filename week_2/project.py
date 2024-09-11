from datetime import datetime
current_year = datetime.now().year
name = input("What is your name? ")
age = int(input("How old are you? "))
birth_year = current_year-age
print(f"Hello {name}! You were born in {birth_year}")