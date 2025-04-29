from collections import Counter

class Solution:
    _fact = None

    @classmethod
    def get_fact(cls):
        if cls._fact is None:
            cls._fact = [1] * 11
            for i in range(1, 11):
                cls._fact[i] = cls._fact[i-1] * i
        return cls._fact

    def countGoodIntegers(self, n, k):
        fact = self.get_fact()
        palindromes = self.generate_palindromes(n)
        seen_digit_sets = set()
        total_count = 0

        for pal in palindromes:
            if pal % k != 0:
                continue
            digits = tuple(sorted(str(pal)))
            if digits in seen_digit_sets:
                continue
            seen_digit_sets.add(digits)
            freq = Counter(digits)
            m = len(digits)
            total_perm = fact[m]
            for cnt in freq.values():
                total_perm //= fact[cnt]
            z = freq.get('0', 0)
            if z == 0:
                valid = total_perm
            else:
                perm_zero = fact[m-1]
                perm_zero //= fact[z-1]
                for d, cnt in freq.items():
                    if d == '0':
                        continue
                    perm_zero //= fact[cnt]
                valid = total_perm - perm_zero
            total_count += valid

        return total_count

    def generate_palindromes(self, n):
        palindromes = []
        if n == 1:
            return [i for i in range(1, 10)]
        half_length = (n + 1) // 2
        start = 10**(half_length - 1)
        end = 10**half_length
        for half in range(start, end):
            half_str = str(half)
            if n % 2 == 0:
                full = half_str + half_str[::-1]
            else:
                full = half_str + half_str[:-1][::-1]
            palindromes.append(int(full))
        return palindromes