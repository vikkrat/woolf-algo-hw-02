def is_symmetric(expression: str) -> str:
    stack: list[str] = []
    open_brackets: dict[str, str] = {'(': ')', '[': ']', '{': '}'}
    close_brackets: dict[str, str] = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if stack and stack[-1] == close_brackets[char]:
                stack.pop()
            else:
                return "Несиметрично"

    return "Симетрично" if not stack else "Несиметрично"

test_expressions: list[str] = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }",
    "{[()]}",
    "[({})]",
    "((()))",
    "({[)]}"
]

for expression in test_expressions:
    result: str = is_symmetric(expression)
    print(f"'{expression}': {result}")
