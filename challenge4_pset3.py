def find_anagrams(s, p):
    result=[]
    len_s=len(s)
    len_p=len(p)
    
    if len_p>len_s:
        return result
    
    p_count=[0]*26
    window_count =[0]*26
    
    for char in p:
        p_count[ord(char)-ord('a')]+=1
    
    for i in range(len_p):
        window_count[ord(s[i])-ord('a')]+=1
    
    for i in range(len_s-len_p+1):
        if window_count == p_count:
            result.append(i)
        
        if i<len_s-len_p:
            window_count[ord(s[i])-ord('a')]-=1
            window_count[ord(s[i+len_p])-ord('a')]+=1
    
    return result

s = input("Enter string s: ").strip()
p = input("Enter string p: ").strip()
    
result = find_anagrams(s, p)
print("Starting indices of anagrams:", result)