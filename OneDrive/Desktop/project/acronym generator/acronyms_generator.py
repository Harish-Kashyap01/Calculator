# Function to generate acronym from a phrase
def generate_acronym(phrase):
    # Remove 'of' and split the phrase into words
    words = phrase.replace('of', '').split()
    
    # Build acronym by taking the first letter of each word and converting to uppercase
    acronym = ''.join(word[0].upper() for word in words)
    
    return acronym

# Get user input
user_input = input("Enter a phrase: ")

# Generate and print the acronym
acronym = generate_acronym(user_input)
print(f"Acronym of {user_input} is {acronym}")

# Alternative method with separate input
user_input2 = input("Enter a phrase: ")

# Generate and print the acronym using the same function
acronym2 = generate_acronym(user_input2)
print(f"Acronym of {user_input2} is {acronym2}")


