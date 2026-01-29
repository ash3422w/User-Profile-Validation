# User Profile Validation – Day 1 Challenge

## 📌 Overview
This project is a Python program developed as part of the **Day-1 Challenge**.  
The objective of this challenge is to validate user profile details using
basic Python concepts such as strings and conditional statements.

The program collects user information and checks whether the provided data
meets all the given validation rules. Based on the validation result, the
program displays whether the user profile is **VALID** or **INVALID**.

---

## 🧾 Problem Statement
Write a Python program that takes the following inputs from the user:
1. Full Name
2. Email ID
3. Mobile Number
4. Age  

The program validates each input based on predefined rules and prints the
final status of the user profile.

---

## ✅ Validation Rules

### 1. Full Name Validation
- Must contain **at least two words**
- Must not start or end with a space

### 2. Email ID Validation
- Must contain **'@'** and **'.'**
- **'@'** must not be the first character

### 3. Mobile Number Validation
- Must be **exactly 10 digits**
- Must contain **only numeric characters**
- Must **not start with 0**

### 4. Age Validation
- Age must be between **18 and 60** (inclusive)

---

## 🧠 Approach and Logic
- User inputs are stored as strings and integers.
- Each validation rule is checked using **conditional statements**.
- Simple string methods such as `len()`, `count()`, and `isdigit()` are used.
- If any validation fails, the profile is marked as **INVALID**.
- Only when all conditions pass, the profile is marked as **VALID**.

---

## 🛠️ Constraints Followed
- ❌ No loops
- ❌ No regular expressions
- ❌ No advanced libraries
- ✅ Used only:
  - Strings
  - Integers
  - Conditional statements
  - Allowed functions (`len()`, `count()`, `isdigit()`)

---

## 🧪 Sample Test Cases

### Test Case 1
**Input:**
- Full Name: Yasir Afaq  
- Email: yasir@gmail.com  
- Mobile: 9622949937  
- Age: 29  

Output:User Profile Is VALID

### Test Case 2
**Input:**
- Full Name: Yasir  
- Email: yasirgmail.com  
- Mobile: 0876543210  
- Age: 17  

Output:User Profile Is INVALID

