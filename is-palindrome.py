#!/usr/bin/env python3

# Create a function isPalindrome

word = input("Write a word: ")
# Split the word string
word_arr = [letter for letter in word]

# Inverted the word string
inverted_word_arr = [word_arr[letter] for letter in range(len(word_arr)-1,-1 ,-1)]

# Join string
join_word_arr = ""
for i in range(0, len(inverted_word_arr), 1):
    join_word_arr += inverted_word_arr[i]

# Palindrome validation
if word == join_word_arr:
    print(f'{word} is a palindrome')
else:
    print(f'{word} Is not a palindrome')
