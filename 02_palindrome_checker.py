from collections import deque

def is_palindrome(input_string: str) -> bool:
    cleaned_string: str = ''.join(char.lower() for char in input_string if char.isalnum())
    char_deque: deque = deque(cleaned_string)
    
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
            
    return True

test_strings: list[str] = [
    "A man a plan a canal Panama",
    "Was it a car or a cat I saw",
    "No lemon no melon",
    "Hello World",
    "Madam In Eden I'm Adam",
    "racecar",
    "palindrome",
    "Able was I ere I saw Elba",
    "Eva, can I see bees in a cave?",
    "A Santa at NASA",
    "Step on no pets",
    "Mr. Owl ate my metal worm",
    "A nut for a jar of tuna",
    "Doc, note I dissent. A fast never prevents a fatness. I diet on cod."
]

for test_string in test_strings:
    result: bool = is_palindrome(test_string)
    print(f"'{test_string}' is a palindrome: {result}")
