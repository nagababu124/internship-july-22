# merge_the_tools
def merge_the_tools(string, k):
    i = 0
    while(i < len(string)):
        a = string[i:i+k]
        output = ""
        for x in a:
            if (x not in output):
                output += x
        print (output)
        i += k