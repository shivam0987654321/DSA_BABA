# Print shivam 5 times 

count = 0 

def function_count():
    global count
    if count == 5:
        return
    print("shivam")
    count+= 1
    function_count()
    
function_count()