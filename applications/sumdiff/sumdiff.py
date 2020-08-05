"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)



def f(x):
    return x * 4 + 6

# q = (1, 3, 4, 7, 12)
# f(x) = x * 4 + 6
# f(q) = [10, 18, 22, 34, 54]
# ```
# f(1) + f(1) = f(12) - f(7)    10 + 10 = 54 - 34
# f(1) + f(4) = f(12) - f(4)    10 + 22 = 54 - 22
# f(4) + f(1) = f(12) - f(4)    22 + 10 = 54 - 22
# f(1) + f(7) = f(12) - f(1)    10 + 34 = 54 - 10
# f(4) + f(4) = f(12) - f(1)    22 + 22 = 54 - 10
# f(7) + f(1) = f(12) - f(1)    34 + 10 = 54 - 10
# f(3) + f(3) = f(12) - f(3)    18 + 18 = 54 - 18

#function that takes in a list
    #set up subtractions and additions table
    #loops over the list
        #inner loop on the list
            #grab all subtractions and additions
    #loop over additions table
        #loop over subtractions table
            #if the addition and the subtraciton are equal output the thing
#additions
# {
#     (1,1): 20
# }
#add_results
# {
#     20: [(1,1)]
# }


def sumdiff(list):
    subtractions = {}
    sub_results = {}
    additions = {}
    add_results = {}
    for num in list:
        for num2 in list:
            sub1result = f(num) - f(num2)
            subtractions[(num, num2)] = sub1result
            if sub1result not in sub_results:
                sub_results[sub1result] = [(num, num2)]
            else:
                sub_results[sub1result].append((num, num2))

            add1result = f(num) + f(num2)
            additions[(num, num2)] = add1result
            if add1result not in add_results:
                add_results[add1result] = [(num, num2)]
            else:
                add_results[add1result].append((num, num2))

    #loop through the add_results
        #grab the subtraction array
        #loop through the pairs of addends
            #loop through the pairs of subtractions
                #print everything
    for result in add_results:
        add_pair_array = add_results[result]
        if result in sub_results:
            sub_pair_array = sub_results[result]
        else:
            sub_pair_array = []
        for pair_of_addends in add_pair_array:
            for pair_of_subs in sub_pair_array:
                print(f"f({pair_of_addends[0]}) + f({pair_of_addends[1]}) = f({pair_of_subs[0]}) - f({pair_of_subs[1]})    {f(pair_of_addends[0])} + {f(pair_of_addends[1])} = {f(pair_of_subs[0])} - {f(pair_of_subs[1])}")

    # for pair_of_nums in additions:
        #find the result in the cache and print them all out
    # for second_pair_of_nums in subtractions:
        #     if additions[pair_of_nums] is subtractions[second_pair_of_nums]:
        #         # print(subtractions)
        #         print(f"f({pair_of_nums[0]}) + f({pair_of_nums[1]}) = f({second_pair_of_nums[0]}) - f({second_pair_of_nums[1]})    {f(pair_of_nums[0])} + {f(pair_of_nums[1])} = {f(second_pair_of_nums[0])} - {f(second_pair_of_nums[1])}")


print(sumdiff(q))