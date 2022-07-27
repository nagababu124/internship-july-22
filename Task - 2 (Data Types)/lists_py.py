
if __name__ == '__main__':
    N = int(input())
    
    l = []
    for _ in range(N):
        s = input().split()
        command = s[0]
        arguments = s[1:]
        if command !="print":
            command += "("+ ",".join(arguments) +")"
            eval("l."+command)
        else:
            print(l)