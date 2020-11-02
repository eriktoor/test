
"""

GET ALL PERMUTATIONS 

Alternatively, we could hypothetically use the itertools library 

"""


def permute(nums, size=2):
    def backtrack(first = 0):
        # if all integers are used up
        if first == n and nums[:size] not in output:  
            output.append(nums[:size])
        for i in range(first, n):
            # place i-th integer first 
            # in the current permutation
            nums[first], nums[i] = nums[i], nums[first]
            # use next integers to complete the permutations
            backtrack(first + 1)
            # backtrack
            nums[first], nums[i] = nums[i], nums[first]

    n = len(nums) 
    output = []
    backtrack()
    return output    


if __name__ == "__main__":
    import time 
    ts = time.time() 

    print("Is our NN, 3,2,2 w how many nodes per layer?")
    # THERE MIGHT BE A WAY TO DO THIS MORE QUICKLY

    ret_node = permute([1,2,3,4,5,6,7,0], size=1) # 8 bit precision would mean a permutation of size 2 
    print("Per Node: ", ret_node)
    print("Generated {} possibilities in {} seconds per node".format( len(ret_node), time.time() - ts))


    ret_layer_1 = permute(ret_node, size =3 )
    print("Generated {} possibilities in {} seconds for layer 1 of three nodes".format( len(ret_layer_1), time.time() - ts))


    ret_layer_2 = permute(ret_layer_1, size = 2)
    print("Generated {} possibilities in {} seconds per node".format( len(ret_layer_2), time.time() - ts))


    ret_layer_3 = permute(ret_layer_1, size = 2)
    print("Generated {} possibilities in {} seconds per node".format( len(ret_layer_3), time.time() - ts))

