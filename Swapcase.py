def swap_case(s):
    str1=list(s)
    i=0
    while i<len(str1):
        if(ord(str1[i]) >=65 and ord(str1[i]) <=90):
            str1[i]=chr(ord(str1[i])+32)
        elif(ord(str1[i]) >=97 and ord(str1[i]) <= 122):
            str1[i]=chr(ord(str1[i])-32)
        i=i+1
    result=""
    return result.join(str1)
            

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)