def reverse_string(str):
    string1 = ""
    for i in str :
        string1 = i + string1
    return string1


a = str("hello world")
print(" the original :", a)
print("the reverse :", reverse_string(a))