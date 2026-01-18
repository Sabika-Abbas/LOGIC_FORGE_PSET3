def find_anagrams(s, p):
    result = []
    len_s = len(s)
    len_p = len(p)
    
    if len_p > len_s:
        return result
    
    p_count = [0] * 26
    window_count = [0] * 26
    
    for char in p:
        p_count[ord(char) - ord('a')] += 1
    
    for i in range(len_p):
        window_count[ord(s[i]) - ord('a')] += 1
    
    for i in range(len_s - len_p + 1):
        if window_count == p_count:
            result.append(i)
        
        if i < len_s - len_p:
            window_count[ord(s[i]) - ord('a')] -= 1
            window_count[ord(s[i + len_p]) - ord('a')] += 1
    
    return result

if __name__ == "__main__":
    import sys
    import io
    test_input = """cbaebabacd
abc"""
    sys.stdin = io.StringIO(test_input)
    
    s = input().strip()
    p = input().strip()
    
    result = find_anagrams(s, p)
    print(result)