import re

def total_salary(path):
    fh = open(path, 'r')
    result = 0.00
    while True:
        line = fh.readline()
        print(line)
        if not line:
            break
        iterator = re.finditer(r"[0-9.]{1,}", line)
        for match in iterator:
            result += float(match.group())
    fh.close()   
    return result
    

    
path = 'test_for_file.txt'
print()
print(total_salary(path))
print()
