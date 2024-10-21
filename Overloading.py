def function(parameter):
    if isinstance(parameter, int):
        print(parameter, '| int')
    elif isinstance(parameter, str):
        print(parameter, '| str')
    else:
        print("Try again.")


function(10)      
function('hello') 