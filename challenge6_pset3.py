from collections import Counter
def repeated_number():
    x=int(input("Enter the size of the array: "))
    if x % 2 != 0:
        print("Error: Array size should be even (2n)")
        return None
    nums = list(map(int, input().split()))
    if len(nums)!=x:
        print("Size of the array does not match the input size.")
        return
    
    count=Counter(nums)
    n=x//2
    for key,values in count.items():
        if values==n:
            return key

print(repeated_number())