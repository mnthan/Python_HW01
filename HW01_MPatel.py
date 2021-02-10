def classifyTriangle(x,y,z):
   
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(x,int) and isinstance(y,int) and isinstance(z,int)):
        return 'InvalidInput'

    # require that the input values be >= 0 and <= 200
    if x > 200 or y > 200 or z > 200:
        return 'InvalidInput'
        
    if x <= 0 or y <= 0 or z <= 0:
        return 'InvalidInput'
    
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (x >= (y + z)) or (y >= (x + z)) or (z >= (x + y)):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    if x == y and y == z:
        return 'Equilateral'
    elif ((x ** 2) + (y ** 2)) == (z ** 2) or ((x ** 2) + (z ** 2)) == (y ** 2) or ((y ** 2) + (z ** 2)) == (x ** 2):
        return 'Right'
    elif (x != y) and  (y != z) and (x != z):
        return 'Scalene'
    else:
        return 'Isoceles'
