# It was a {Adjective} and {Adjective} {Noun}.
print(
    '''
    ********************************
    ** Welcome to the madlib-game **
    ********************************
    ''')

def read_template(file_path):
    with open(file_path, mode="r") as f:
        res=f.read()
        return (res) 


def parse_template(x):
    j=x.replace(".",'' )
    a=j.split(" ")
    v=[]
    for i in range(len(a)):
        if a[i]=="{Adjective}" or a[i]=="{Noun}":
            k=a[i][1:-1]
            v.append(k)
            p=tuple(v)
        else:
            continue
    val1="Adjective"
    val2="Noun"
    h=x.replace(val1,'' ).replace(val2,'' )
    expected_stripped=h
    expected_parts=p
    return expected_stripped,expected_parts

expected_stripped=parse_template("It was a {Adjective} and {Adjective} {Noun}.")[0]
expected_parts=parse_template("It was a {Adjective} and {Adjective} {Noun}.")[1]

# print(parse_template("It was a {} and {} {}"))
# def parse_template(input_str):
#     originStr=input_str
#     deleted_words = []
#     while '{' in input_str and '}' in input_str:
#         start_index = input_str.index('{')
#         end_index = input_str.index('}')
#         deleted_word = input_str[start_index+1:end_index]
#         deleted_words.append(deleted_word)
#         input_str = input_str[:start_index] + input_str[end_index+1:]
#     deleted_words = tuple(deleted_words)
#     input_str = originStr
#     for word in deleted_words:
#         input_str = input_str.replace('{' + word + '}', '{}')
#     expected_stripped=input_str
#     expected_parts=deleted_words
#     return expected_stripped,expected_parts


    
def merge(x,y):
    return x.format(*y)
    
def take_values():
    list111=[]
    for i in range(len(expected_parts)):
        x=input(f"Please add {expected_parts[i]} :")
        list111.append(x)
    return list111

print(merge(expected_stripped,take_values())) 
# def read_template(path):
#     try:
#         with open(path, 'r') as file:
#             return file.read()
#     except FileNotFoundError:
#         print(f"File not found: {path}")
#         raise


   
   
   
   
   





