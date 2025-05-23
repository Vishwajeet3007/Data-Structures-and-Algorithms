def compress(chars):
    read = 0
    write = 0
    while read < len(chars):
        char = chars[read]
        count = 0
        # consecutive occurences
        while read < len(chars) and chars[read] == char:
            read += 1
            count += 1
        chars[write] = char
        write += 1

        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1
    return write
chars = ["a","a","b","b","c","c","c"]
print(compress(chars)) 
chars = ["a"]  
print(compress(chars)) 
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]   
print(compress(chars))