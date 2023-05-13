def intro():
    return   '''
    ********************************
    ** Welcome to the madlib-game **
    ********************************
    '''
def read_template(file_path):
    with open(file_path, mode="r") as f:
        res=f.read()
        return (res) 


def parse_template(input_str):
    originStr=input_str
    deleted_words = []
    while '{' in input_str and '}' in input_str:
        start_index = input_str.index('{')
        end_index = input_str.index('}')
        deleted_word = input_str[start_index+1:end_index]
        deleted_words.append(deleted_word)
        input_str = input_str[:start_index] + input_str[end_index+1:]
    deleted_words = tuple(deleted_words)
    for word in deleted_words:
        originStr=originStr.replace(word,'')
    expected_stripped=originStr
    expected_parts=deleted_words
    return expected_stripped,expected_parts

    
def merge(text,user_values):
    global output 
    output = text.format(*user_values)
    return output

    
def take_values():
    all_user_inputs=[]
    for i in range(len(expected_parts)):
        userInput=input(f"Please add {expected_parts[i]} :")
        all_user_inputs.append(userInput)
    return all_user_inputs

def text_writing(file_name,text):
    with open(file_name, mode="w") as f:
        f.write(text) 



if __name__=="__main__":
    class FileNotFoundError(Exception):
        def __init__(self, file_path):
            super().__init__()
    file_path_new = input('Enter file_path without " ":')
    file_path="assets/example.txt"
    try: 
        if file_path_new!=file_path:
            raise FileNotFoundError(file_path_new)
        else:
            res=read_template(file_path)
    except FileNotFoundError:
        print (f"please fix this file path: {file_path_new}")
    
    # try:
    #     file_path="assets/example.txt"
    #     res=read_template(file_path)
    # except FileNotFoundError:
    #     print(f"**File not found please check the file path:{file_path}**")
    
    expected_stripped=parse_template(res)[0]
    expected_parts=parse_template(res)[1]
    example_output_file="assets/example_output.txt"
    
    print(intro())
    
    print(merge(expected_stripped,take_values()))
    
    text_writing(example_output_file,output)
    
    
    





    

    




   
   
   
   
   





