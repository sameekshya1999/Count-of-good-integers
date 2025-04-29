# LeetCode 3272 - Find the Count of Good Integers

## 🧠 Problem Overview

Given two integers `n` and `k`, the task is to find the number of n-digit integers whose digits can be rearranged to form a k-palindromic number (a number that is both a palindrome and divisible by k).

The integers must not have leading zeros after rearrangement.

---

## 💡 Approach

The solution involves the following main ideas:

1. **Precompute Factorials**:
   - Factorials up to 10 are precomputed for fast permutation calculations.

2. **Generate n-Digit Palindromic Numbers**:
   - Systematically create all palindromes with exactly `n` digits.

3. **Check for Divisibility by k**:
   - Only consider palindromic numbers that are divisible by `k`.

4. **Digit Frequency and Rearrangement**:
   - Sort digits and use a frequency counter to find unique digit sets.
   - Calculate the number of valid permutations using combinatorics.

5. **Handle Leading Zeros Carefully**:
   - Ensure permutations that would start with '0' are excluded.

6. **Avoid Duplicate Counting**:
   - Use a set to track already processed digit sets to avoid redundant calculations.

---

## 🛠 Step-by-Step Execution

- **Step 1**: Precompute factorial values from 1 to 10.
- **Step 2**: Generate all possible n-digit palindromic numbers.
- **Step 3**: For each palindrome:
  - If not divisible by `k`, skip.
  - Otherwise, sort its digits and represent as a tuple.
  - If this digit tuple is already processed, skip.
- **Step 4**: Count permutations:
  - Use factorial formula considering repeated digits.
  - Subtract cases with leading zeros.
- **Step 5**: Add valid permutations to the total count.
- **Step 6**: Return the total count of good integers.

---

## 📁 Code Structure

| File | Description |
|:---|:---|
| `count_good_integers.py` | Python script implementing the complete solution. |

---

## 📈 How to Run the Code

```bash
# Clone the repository
git clone https://github.com/sameekshya1999/leetcode-solutions.git

# Navigate into the project folder
cd leetcode-solutions

# Run the Python file
python count_good_integers.py
