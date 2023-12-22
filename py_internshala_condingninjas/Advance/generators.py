
def My_gen():
    for num in range(50):
        yield num**num
        # hii=num**num
        # print(hii)
# My_gen()


# new=My_gen()
# all=list(new)
# print(all)

for new in My_gen():
    print(new)   # one by one into My_gen() and into new

