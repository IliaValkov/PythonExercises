
# def sqaure_nums(nums): 
#     for i in nums: 
#         yield (i*i)

# my_nums = sqaure_nums([1,2,3,4,5])

my_nums = (n*n for n in [1,2,3,4,5])

print(my_nums)

#print(list(my_nums))

for num in my_nums: 
    print(num)