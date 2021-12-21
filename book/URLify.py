def URLify(str1):
    str1 = str1.strip()
    str1 =  str1.replace(" ","%20")
    return str1


result = URLify("Mr John Smith    ")
print(result)