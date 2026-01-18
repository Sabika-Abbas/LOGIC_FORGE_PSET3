def longest_palindrome(s):
    if len(s) <= 1:
        return s
    max_len = 1
    for i in range(len(s)):
        left = i
        right = i

        while left >= 0 and right < len(s) and s[left] == s[right]:
            curr_len= right - left + 1
            if curr_len > max_len:
                max_len = curr_len
                start = left

            left -= 1
            right += 1

        left = i
        right = i+1

        while left>= 0 and right < len(s) and s[left] == s[right]:
            curr_len= right - left + 1
            if curr_len > max_len:
                max_len = curr_len
                start = left

            left -= 1
            right+=1
    
    return s[start:start+max_len]

print(longest_palindrome("babad"))  
    