def swap_case(s):
    res = ''
    for i in s:
        if i.isupper()==True:
            res += i.lower()
        elif i.islower()==True:
            res += i.upper()
        else:
            res += i
    return res