# DSA Notes

This repo contains my beginner DSA practice in Python.
Each file is a small concept-based example that I can revise later.

## Day 1: Basics (`Eg1` to `Eg4`)

### Core idea

Most number-based problems follow this pattern:

1. Extract the last digit
2. Process the digit
3. Reduce the number

### Important operations

Extract the last digit:

```python
digit = num % 10
```

Remove the last digit:

```python
num = num // 10
```

### Files covered

- `Eg1_reverse.py`: reverse digits by printing the last digit step by step
- `Eg2_count.py`: count digits using a loop and with `log10`
- `Eg3_palidrome.py`: check whether a number is a palindrome
- `Eg3.1_validpalidrome.py`: extra palindrome-related practice
- `Eg4_armstong.py`: check whether a number is an Armstrong number

## Day 2: Prime, Frequency, and Hashing (`Eg5` to `Eg8.2`)

### 1. Prime number check

File:
- `Eg5prime.py`

Notes:
- A prime number has exactly two factors: `1` and itself.
- Brute force checks divisibility from `2` to `n - 1`.
- The optimized approach checks only up to `sqrt(n)`.
- If any divisor is found, the number is not prime.

Useful pattern:

```python
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        return False
```

### 2. Frequency counting with dictionary

File:
- `EG6frequency.py`

Notes:
- Use a dictionary to count how many times each number appears.
- If the key already exists, increase its count.
- A shorter approach is `dict.get(key, 0) + 1`.

Useful pattern:

```python
freq[num] = freq.get(num, 0) + 1
```

### 3. Hashing with list for fixed range

File:
- `EG7_hashlist.py`

Notes:
- A hash list works well when values are in a small fixed range.
- Store frequency directly at the index equal to the number.
- This is fast for queries, but only practical when the range is small.

Useful pattern:

```python
hash_list = [0] * 11
hash_list[num] += 1
```

### 4. Hashing with dictionary

File:
- `EG8_hashing.py`

Notes:
- Dictionary-based hashing works even when values are sparse or large.
- It avoids creating a large list for unused values.
- For queries, use `dict.get(value, 0)` to safely handle missing keys.

### 5. Hashing with `Counter`

File:
- `EG8.1_hashing.py`

Notes:
- `collections.Counter` is a shortcut for frequency problems.
- It reduces manual counting code and keeps the solution clean.

Useful pattern:

```python
from collections import Counter

count_n = Counter(n)
print(count_n.get(num, 0))
```

### 6. String hashing / character frequency

File:
- `Eg8.2_hashingstring.py`

Notes:
- The same frequency idea also works for strings.
- `Counter` can count characters directly from a string.
- This is useful for query-based character count problems.

Useful pattern:

```python
from collections import Counter

count = Counter(s)
print(count.get(ch, 0))
```

## Summary

From `Eg5` to `Eg8.2`, the main ideas I practiced were:

- prime checking
- frequency counting
- hashing with arrays
- hashing with dictionaries
- hashing with `Counter`
- character frequency in strings
