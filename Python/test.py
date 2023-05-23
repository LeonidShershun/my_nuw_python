
def write_employees_to_file(employee_list, path):
    fh = open(path, 'w+')
    for i in employee_list:
        if type(i) == list:
            for g in i:
                print(g)
                fh.write(str(g))
        
    fh.close()


path = 'test_for_file2.txt'
employee_list = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]

write_employees_to_file(employee_list, path)