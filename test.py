name = input('Enter your name> ')
age = input('Enter your age> ')
color = input('Enter your favorite color')
status = ''
if color.lower() == 'blue':
    status = 'magical'
    print(f"""Hello Mr.{name} 
    Welcome to O'brien cooperation. 
    You are {age} years old we realised, and 
    we are glad to work with you. 
    You love {color} and that makes you look {status}""")