

'''
DocString:
'''

def target_as_array_elements_sum( array, target ):
       
    return helper_dp( array, target, 0 )
    

def helper_dp( array, target, start ):

    local_count = 0

    if( target == 0 ):
        return 1
    if( start > len(array)-1 ):
        return 0

    local_count += helper_dp( array, target, start+1 )
    local_count += helper_dp( array, target-array[start], start+1 )

    return local_count







global count
arr = [2, 4, 6, 10, 12]
print(f'Count of ways we can get the target is : {target_as_array_elements_sum(arr, 12)}')