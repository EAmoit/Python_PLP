import json
import difflib

# JSON file is being loaded into a dictionary
def load_json_to_dict(file_path):
    with open(file_path, 'r') as file:
        dictionary = json.load(file)
    return dictionary

# Function to get the definition of a word
def get_definition(word, dictionary):
    word = word.lower()  # Normalize to lowercase
    
    if word in dictionary:
        return dictionary[word][0]  # Return the first definition
    else:
        # Find close matches to the input word
        suggestions = difflib.get_close_matches(word, dictionary.keys())
        if suggestions:
            return f"'{word}' not found. Did you mean: {', '.join(suggestions)}?"
        else:
            return f"'{word}' not found and no close matches available."

# Main function to run the dictionary program
def main():
    # Load the dictionary from the JSON file
    dictionary = load_json_to_dict('data.json')
    
    # Get user input
    user_word = input("Enter a word: ")
    
    # Get the definition or suggestion
    result = get_definition(user_word, dictionary)
    print(result)

# Run the main function
if __name__ == "__main__":
    main()
