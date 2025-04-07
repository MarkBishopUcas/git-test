import re

# Function to extract the correct answers
def extract_correct_answers(input_string):
    # Use regex to find all instances of "The correct answer is (X)" and capture X
    answers = re.findall(r'The correct answer is \((.*?)\)', input_string)
    return answers

# Read the input string from a local text file
with open("input.txt", "r") as file:
    input_str = file.read()

# Extract answers from the input string
answers = extract_correct_answers(input_str)

# Define the expected sets for odd and even questions
set1 = set("ABCDE")  # Odd questions
set2 = set("FGHIJK")  # Even questions

# Store user inputs for any DNF answers
manual_answers = {}

# First pass: collect manual answers for any missing answers
q_num = 1
i = 0  # Index in answers list

while i < len(answers):
    expected_set = set1 if q_num % 2 == 1 else set2  # Set for odd/even questions
    current_answer = answers[i]

    if current_answer in expected_set:
        # Answer is found, proceed to next
        q_num += 1
        i += 1
    else:
        # Prompt for a manual input if answer is not found
        user_input = input(f"Did not find the answer to question {q_num}. Please input manual answer: ").strip().upper()
        manual_answers[q_num] = user_input
        q_num += 1
        i += 1  # Make sure to increment i here to move to the next answer

# Now, replace missing answers with the manually entered ones
for i in range(len(answers)):
    q_num = i + 1
    if q_num in manual_answers:
        answers[i] = manual_answers[q_num]

# Function to display answers in sets of 10
def display_page(page_number):
    start_index = page_number * 10
    end_index = start_index + 10
    q_num = start_index + 1  # Start question number for this page
    
    page_answers = []
    i = start_index  # Start from the correct index in the answers list
    
    while i < len(answers) and i < end_index:
        expected_set = set1 if q_num % 2 == 1 else set2  # Set for odd/even questions
        current_answer = answers[i]

        page_answers.append(f"{q_num}. {current_answer.upper()}")  # Convert to uppercase
        
        q_num += 1
        i += 1
    
    # Display the answers for the current page
    if page_answers:
        print("\n" * 10)  # Add 10 newlines before showing the page
        print("\n".join(page_answers))
    else:
        print("No more questions to display.")
    
    return i  # Return the last index processed for navigation

# Start with the first page
page_number = 0
last_index = display_page(page_number)

while True:
    # Ask for user input to navigate pages
    user_input = input("\nEnter '<' to go back, '>' to go forward, or 'exit' to quit: ").strip().lower()
    
    if user_input == '>':
        if last_index < len(answers):
            page_number += 1
            last_index = display_page(page_number)
        else:
            print("You are already at the last page.")
    
    elif user_input == '<':
        if page_number > 0:
            page_number -= 1
            last_index = display_page(page_number)
        else:
            print("You are already at the first page.")
    
    elif user_input == 'exit':
        print("Exiting.")
        break
    
    else:
        print("Invalid input. Please try again.")
