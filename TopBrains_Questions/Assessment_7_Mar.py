
# ---- Question 1 ----
# Password Strength Validator
# Problem Description
# A website checks the strength of passwords. A password is considered strong if it satisfies the following rules:
# Length must be at least 8 characters
# Must contain at least one uppercase letter
# Must contain at least one digit
# Must contain at least one special character (@, #, $)
# Given a list of passwords, return a list containing only strong passwords.

class Solution:
    def strong_passwords(self, passwords):
        strong = []

        for pwd in passwords:
            if len(pwd) < 8:
                continue

            has_upper = False
            has_digit = False
            has_special = False

            for ch in pwd:
                if ch.isupper():
                    has_upper = True
                elif ch.isdigit():
                    has_digit = True
                elif ch in "@#$":
                    has_special = True

            if has_upper and has_digit and has_special:
                strong.append(pwd)

        return strong
    

# ---- Question 2 ----
#  Product Stock Shortage Report
# Problem Description
# An inventory system stores product quantities in a dictionary.
# A product is considered low in stock if its quantity is less than 10.
# Your task is to return a list of all product names that are low in stock.
# Input
# Dictionary where:
# Key → Product Name
# Value → Quantity
# Output
# List of product names with stock < 10.

#code :-
class Solution:
    def low_stock_products(self, inventory):
        result = []
        
        for product, quantity in inventory.items():
            if quantity < 10:
                result.append(product)
                
        return result
    
# ---- Question 3 ----
# Consecutive Duplicate Word Detector
# Problem Description
# A text processing tool analyzes sentences to find consecutive duplicate words.
# If the same word appears next to each other, ignoring case differences, it should be recorded.
# Return a list of such duplicate words.
# Input
# A sentence string.
# Output
# List of duplicate consecutive words.

# code :-
class Solution:
    def find_duplicate_words(self, sentence):
        words = sentence.lower().split()
        duplicates = []
        
        for i in range(len(words)-1):
            if words[i] == words[i+1]:
                duplicates.append(words[i])
                
        return duplicates


# ---- Question 4 ----
# Unique Product Purchase Analyzer
# Problem Description
# An e-commerce company records the products purchased by customers during a sale. However, some products appear multiple times in the purchase list because multiple customers bought them.
# The company wants to generate a list of unique products that were purchased only once during the sale.
# You are given a list of product names representing purchases. Your task is to return a list containing products that appear exactly once in the list.
# Input
# A list of product names.
# Example
# ["Laptop","Mouse","Keyboard","Mouse","Monitor","Keyboard","Tablet"]
# Output
# ["Laptop","Monitor","Tablet"]

# code :-
class Solution:
    def unique_products(self, products):
        result = []
        
        for p in products:
            if products.count(p) == 1:
                result.append(p)

        return result