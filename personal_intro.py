# Program Name: User Welcome Message Generator
# Author: Ganesh Biradar
# Date: December 10, 2025
# Description: This program collects basic user information and displays a friendly, personalized summary.



# SECTION 1: Gathering User Input (Using input() function)
# Technical Requirement: Use input() to get user information (5 questions added)


# 1. Ask for the user's name
user_name = input("Welcome! What is your name? ")

# 2. Ask for the user's age (Stored as a string, which is fine for display purposes)
user_age = input(f"Hello, {user_name}! How old are you? ")

# 3. Ask for the user's favorite hobby
user_hobby = input("That's interesting! What is one of your favorite hobbies? ")

# 4. Ask for the user's favorite car
user_car = input("What is your favorite car? ")

# 5. Ask for the user's current city
user_city = input("Which city are you currently based in? ")




# SECTION 2: Generating and Displaying Output (Using print() function and f-strings)
# Technical Requirement: Use print() to display the welcome message


# Print a visual separator for better formatting
print("\n" + "="*60)
print(" Personalized Profile Summary 😄")
print("="*60)

# Display a friendly opening message, accessing the stored 'user_name' variable
print(f"Hello '{user_name}'! Thank you for sharing your details.")
print("Here is the complete information you provided:-")

# List all the stored variables clearly
print(f"* Name: {user_name}")
print(f"* Age: {user_age} years old")
print(f"* Hobby: {user_hobby}")
print(f"* Favorite Car: {user_car}")
print(f"* Current City: {user_city}")

# for another separator line
print("-" * 60)

# Display a warm, welcoming final message, integrating multiple variables
# Technical Requirement: Make the output friendly and welcoming
print(f" 🎉 We are excited to connect with someone from '{user_city}'! 🎉")
print(f"It sounds like you have a vibrant personality, '{user_name}', especially since you love '{user_hobby}' and the car '{user_car}'!")

# for the final separator
print("="*60)

# End of program