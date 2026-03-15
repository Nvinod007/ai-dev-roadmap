"""
Week 1 - Day 1: Variables, Types, and Basic Operations
Run: python week1/01_variables_types.py

Your task: Uncomment each section and run it. Understand what each does.
"""

# === 1. Variables and types ===
name = "AI Developer"
age = 3  # years of experience
is_learning = True

print("Name:", name)
print("Type of name:", type(name))
print("Type of age:", type(age))

# === 2. Functions ===
def greet(person_name):
    """A simple function that returns a greeting."""
    return f"Hello, {person_name}!"

message = greet("Vinod")
print(message)

# === 3. Loops ===
topics = ["variables", "functions", "loops", "APIs"]
for i, topic in enumerate(topics):
    print(f"  {i + 1}. {topic}")

# === 4. Your exercise ===
# Write a function that takes a list of numbers and returns their sum.
# Then call it with [1, 2, 3, 4, 5] and print the result.
