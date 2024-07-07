# fun_snake_to_camel.py
def fun_snake_to_camel(name):
    return ''.join(word.title() for word in name.split('_'))

print(fun_snake_to_camel('snake_case_string'))
