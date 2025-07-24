def find_palindromes(start, end):
    return [num for num in range(start, end + 1) if str(num) == str(num)[::-1]]
start = 1
end = 300
palindromes = find_palindromes(start, end)
print("Palindrome numbers between", start, "and", end, "are:", palindromes)
