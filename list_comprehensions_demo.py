"""
List Comprehensions Demo
Demonstrates various ways to use list comprehensions in Python
"""


def main():
    print("=" * 60)
    print("LIST COMPREHENSIONS DEMO")
    print("=" * 60)

    # 1. Basic list comprehension
    print("\n1. Basic List Comprehension")
    print("-" * 40)
    squares = [x**2 for x in range(10)]
    print(f"Squares of 0-9: {squares}")

    # 2. List comprehension with conditional (filter)
    print("\n2. List Comprehension with Conditional")
    print("-" * 40)
    evens = [x for x in range(20) if x % 2 == 0]
    print(f"Even numbers 0-19: {evens}")

    # 3. List comprehension with if-else (mapping)
    print("\n3. List Comprehension with If-Else")
    print("-" * 40)
    labels = ["Even" if x % 2 == 0 else "Odd" for x in range(10)]
    print(f"Even/Odd labels for 0-9: {labels}")

    # 4. List comprehension with string manipulation
    print("\n4. String Manipulation")
    print("-" * 40)
    words = ["hello", "world", "python", "list"]
    uppercase = [word.upper() for word in words]
    print(f"Original: {words}")
    print(f"Uppercase: {uppercase}")

    # 5. List comprehension with function calls
    print("\n5. Using Functions in List Comprehension")
    print("-" * 40)
    def double(n):
        return n * 2

    doubled = [double(x) for x in range(5)]
    print(f"Doubled values: {doubled}")

    # 6. Nested list comprehension (2D list)
    print("\n6. Nested List Comprehension")
    print("-" * 40)
    matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
    print("Multiplication table (3x3):")
    for row in matrix:
        print(row)

    # 7. Flattening a 2D list
    print("\n7. Flattening a 2D List")
    print("-" * 40)
    nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [num for row in nested for num in row]
    print(f"Nested: {nested}")
    print(f"Flattened: {flattened}")

    # 8. List comprehension with multiple conditions
    print("\n8. Multiple Conditions")
    print("-" * 40)
    divisible = [x for x in range(50) if x % 3 == 0 and x % 5 == 0]
    print(f"Numbers divisible by both 3 and 5 (0-49): {divisible}")

    # 9. Working with tuples
    print("\n9. Working with Tuples")
    print("-" * 40)
    pairs = [(x, x**2) for x in range(5)]
    print(f"Number and square pairs: {pairs}")

    # 10. Filtering and transforming
    print("\n10. Filter and Transform Combined")
    print("-" * 40)
    numbers = [1, -2, 3, -4, 5, -6, 7, -8]
    positive_squares = [x**2 for x in numbers if x > 0]
    print(f"Original: {numbers}")
    print(f"Squares of positive numbers: {positive_squares}")

    # Comparison: List comprehension vs traditional loop
    print("\n" + "=" * 60)
    print("COMPARISON: List Comprehension vs Traditional Loop")
    print("=" * 60)

    # Traditional way
    traditional = []
    for x in range(5):
        if x % 2 == 0:
            traditional.append(x**2)

    # List comprehension way
    comprehension = [x**2 for x in range(5) if x % 2 == 0]

    print("\nTraditional loop result:", traditional)
    print("List comprehension result:", comprehension)
    print("\nBoth produce the same result, but list comprehension is more concise!")


if __name__ == "__main__":
    main()
