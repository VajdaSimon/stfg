list_of_lines = open("sample.txt", "r").readlines()
list_of_lines[2] = "Line5\n"

a_file = open("sample.txt", "w")
a_file.writelines(list_of_lines)