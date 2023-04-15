def toSnake(text, separator):    
    text = [text[i].upper() if i > 0 and text[i-1] == separator else text[i] for i in range(len(text))] 
    text = [value for value in text if value != separator]
    text = ''.join(text) 
    return text

text, separator = "this_is_a_test", "_"
result = toSnake(text, separator)
print(result)



