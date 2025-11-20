n = 5
total = sum(range(1, n+1))
print(f"Sum of 1 to {n} is {total}")


print("Program 12 - Factorial:")
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
print(f"Factorial of 5 is {factorial(5)}")


print("Program 13 - Multiplication Table:")
num = 7
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


print("Program 14 - Palindrome Check:")
string = "racecar"
if string == string[::-1]:
    print(f"{string} is Palindrome")
else:
    print(f"{string} is not Palindrome")


print("Program 15 - Count Vowels:")
text = "Hello World"
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print(f"Vowels in '{text}': {count}")


print("Program 16 - Reverse String:")
text = "Python"
reversed_text = text[::-1]
print(f"'{text}' reversed is '{reversed_text}'")


print("Program 17 - Fibonacci Series:")
a, b = 0, 1
fib_list = []
for _ in range(8):
    fib_list.append(a)
    a, b = b, a + b
print(fib_list)


print("Program 18 - Prime Number Check:")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(f"17 is Prime: {is_prime(17)}")


print("Program 19 - Sum of Digits:")
num = 12345
digit_sum = sum(int(digit) for digit in str(num))
print(f"Sum of digits of {num}: {digit_sum}")


print("Program 20 - Average of Numbers:")
numbers = [10, 20, 30, 40, 50]
average = sum(numbers) / len(numbers)
print(f"Average: {average}")


print("Program 21 - Simple Interest:")
principal = 1000
rate = 5
time = 3
interest = (principal * rate * time) / 100
print(f"Simple Interest: {interest}")


print("Program 22 - Swap Two Variables:")
a, b = 5, 10
print(f"Before: a={a}, b={b}")
a, b = b, a
print(f"After: a={a}, b={b}")


print("Program 23 - Temperature Conversion:")
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")


print("Program 24 - String Length:")
text = "Python Programming"
print(f"Length of '{text}': {len(text)}")


print("Program 25 - Maximum of List:")
nums = [45, 23, 56, 89, 34]
max_num = max(nums)
print(f"Maximum: {max_num}")


print("Program 26 - Minimum of List:")
nums = [45, 23, 56, 89, 34]
min_num = min(nums)
print(f"Minimum: {min_num}")


print("Program 27 - Count Characters:")
text = "abracadabra"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print(f"Character count: {char_count}")


print("Program 28 - List Sorting:")
nums = [64, 34, 25, 12, 22, 11, 90]
sorted_nums = sorted(nums)
print(f"Sorted: {sorted_nums}")


print("Program 29 - Duplicate Removal:")
list_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_list = list(set(list_with_duplicates))
print(f"Unique: {unique_list}")


print("Program 30 - List Comprehension:")
nums = [1, 2, 3, 4, 5]
squared = [x**2 for x in nums]
print(f"Squared: {squared}")
