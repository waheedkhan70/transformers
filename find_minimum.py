def find_minimum(a, b):
   
    results = []
    
    results.append(a+b)
    results.append(a-b)
    results.append(a*b)
    
    
    try:
        division_result = a/b
        results.append(division_result)
        
    except ZeroDivisionError:
        pass
        
    return min(results)
