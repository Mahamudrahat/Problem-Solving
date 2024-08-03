class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        prev_value = 0

        
        for i in range(len(s)):
            if i+1 < len(s) and roman_values[s[i]] < roman_values[s[i+1]]:
            	total -= value
                
            else:
                total += value
            
        
        return total