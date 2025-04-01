import re
 
 def extract_correct_answers(input_string):
     # Use regex to find all instances of "The correct answer is (X)" and capture X
     answers = re.findall(r'The correct answer is \((.*?)\)', input_string)
     return answers
 
 # Example usage
 input_str = """
 wip
 """

result = extract_correct_answers(input_str)
print(result)  # Output: ['B', 'A']