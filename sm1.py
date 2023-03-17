def replace_char(input_str):
    n = int(input_str[0])
    name = input_str[1:]    
    name_list = list(name)
    for i in range(n-1, len(name_list), n):
        name_list[i] = 'e'
    
    
    modified_name = ''.join(name_list)
    
    return modified_name


input_str = "4jawaeth"
output_str = replace_char(input_str)
print(output_str)  
