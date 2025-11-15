# Survey with yes/no questions

print("SURVEY")


cs = input("Are you interested in computer science? (y/n): ")
games = input("Do you like playing computer games? (y/n): ")
instagram = input("Do you have an Instagram account? (y/n): ")


cs_result = "Yes" if cs == "y" else "No"
games_result = "Yes" if games == "y" else "No"
instagram_result = "Yes" if instagram == "y" else "No"


print("SURVEY RESULTS")
print(f"Interested in computer science: {cs_result}")
print(f"Playing computer games: {games_result}")
print(f"Has an Instagram account: {instagram_result}")