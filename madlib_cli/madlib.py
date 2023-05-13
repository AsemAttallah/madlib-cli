def intro():
    '''
    Welcoming message
    '''
    return   '''
    ********************************
    ** Welcome to the madlib-game **
    ********************************
    '''
def read_template(file_path):
    '''
    Read file from file path
    '''
    try:
        with open(file_path, mode="r") as f:
            res=f.read()
            return (res) 
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found at path: {file_path}")

def parse_template(input_str):
    '''
    Take a words between curly brakets,And make it empty  
    
    '''
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
    '''
    Merging user input words with empty spaces in the paragraph 
    '''
    global output 
    output = text.format(*user_values)
    return output

    
def take_values():
    '''
    Taking input from the user
    '''
    all_user_inputs=[]
    for i in range(len(expected_parts)):
        userInput=input(f"Please add {expected_parts[i]} :")
        all_user_inputs.append(userInput)
    return all_user_inputs

def text_writing(file_name,text):
    '''
    Writing the output in the specific file
    '''
    with open(file_name, mode="w") as f:
        f.write(text) 



if __name__=="__main__":
    file_path="assets/example.txt"
    res=read_template(file_path)

    expected_stripped=parse_template(res)[0]
    expected_parts=parse_template(res)[1]
    example_output_file="assets/example_output.txt"
    
    print(intro())
    
    print(merge(expected_stripped,take_values()))
    
    text_writing(example_output_file,output)
    
    
    





    

    




   
   
   
   
   





