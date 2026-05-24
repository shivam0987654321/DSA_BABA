count = 0 

def function_count():
    global count
    if count == 5:
        return 
    count = count + 1
    function_count()
    print("shivam")


function_count()