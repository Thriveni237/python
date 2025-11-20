

# ===== 07: Square Root Program =====
import math
num = 16
square_root = math.sqrt(num)
print(f"Square root of {num} is {square_root}")

# ===== 08: Even or Odd =====
num = 25
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

# ===== 09: Positive Negative Zero =====
num = -10
if num > 0:
    print(f"{num} is Positive")
elif num < 0:
    print(f"{num} is Negative")
else:
    print("Number is Zero")

# ===== 10: Greatest of Two Numbers =====
a, b = 15, 20
greater = a if a > b else b
print(f"Greater number is {greater}")

# ===== 11: Sum of First N Numbers =====
n = 5
total = sum(range(1, n+1))
print(f"Sum of 1 to {n} is {total}")

# ===== 12: Factorial =====
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
print(f"Factorial of 5 is {factorial(5)}")

# ===== 13: Table of Multiplication =====
num = 7
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# ===== 14: Palindrome Check =====
string = "racecar"
if string == string[::-1]:
    print(f"{string} is Palindrome")
else:
    print(f"{string} is not Palindrome")

# ===== 15: Count Vowels =====
text = "Hello World"
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print(f"Vowels in '{text}': {count}")

# ===== 16: Reverse String =====
text = "Python"
reversed_text = text[::-1]
print(f"'{text}' reversed is '{reversed_text}'")

# ===== 17: Fibonacci Series =====
a, b = 0, 1
print("Fibonacci series:")
for _ in range(8):
    print(a, end=" ")
    a, b = b, a + b

# ===== 18: Prime Number Check =====
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(f"\n17 is Prime: {is_prime(17)}")

# ===== 19: Sum of Digits =====
num = 12345
digit_sum = sum(int(digit) for digit in str(num))
print(f"Sum of digits of {num}: {digit_sum}")

# ===== 20: Average of Numbers =====
numbers = [10, 20, 30, 40, 50]
average = sum(numbers) / len(numbers)
print(f"Average: {average}")

# ===== 21: Simple Interest =====
principal = 1000
rate = 5
time = 3
interest = (principal * rate * time) / 100
print(f"Simple Interest: {interest}")

# ===== 22: Swap Two Variables =====
a, b = 5, 10
print(f"Before: a={a}, b={b}")
a, b = b, a
print(f"After: a={a}, b={b}")

# ===== 23: Temperature Conversion =====
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# ===== 24: String Length =====
text = "Python Programming"
print(f"Length of '{text}': {len(text)}")

# ===== 25: Maximum of List =====
nums = [45, 23, 56, 89, 34]
max_num = max(nums)
print(f"Maximum: {max_num}")

# ===== 26: Minimum of List =====
nums = [45, 23, 56, 89, 34]
min_num = min(nums)
print(f"Minimum: {min_num}")

# ===== 27: Count Characters =====
text = "abracadabra"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print(f"Character count: {char_count}")

# ===== 28: List Sorting =====
nums = [64, 34, 25, 12, 22, 11, 90]
sorted_nums = sorted(nums)
print(f"Sorted: {sorted_nums}")

# ===== 29: Duplicate Removal =====
list_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_list = list(set(list_with_duplicates))
print(f"Unique: {unique_list}")

# ===== 30: List Comprehension =====
nums = [1, 2, 3, 4, 5]
squared = [x**2 for x in nums]
print(f"Squared: {squared}")
