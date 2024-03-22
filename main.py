def odd_numbers(n):
    return [i for i in range(1, n + 1) if i % 2 != 0]

def even_numbers(n):
    return [i for i in range(1, n + 1) if i % 2 == 0]

def fibonacci_sequence(n):
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

def print_menu():
    print("1. Odd numbers")
    print("2. Even numbers")
    print("3. Fibonacci sequence")
    print("4. Prime numbers")


def main():
    print_menu()
    function = int(input("Your choice: "))
    maxNum = int(input("Enter max number: "))
    if function == 1:
        odd_numbers(maxNum)
    elif function == 2:
        even_numbers(maxNum)
    elif function == 3:
        fibonacci_sequence(maxNum)
    else:
        print("Invalid choice")


if __name__ == '__main__':
    main()
