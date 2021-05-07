x = lambda a : a + 10
print(x(5))


def a(x):
    return x + 10

print(a(5))

x = lambda a, b : a * b
print(x(5, 6))


# list_of_lambdas = [lambda i=i: i*i for i in range(1, 6)]
# for f in list_of_lambdas:
#    print(f())
my_list = [4,2,5]
lambdas = [lambda: print(number)
           for number in my_list]

print(lambdas)
for function in lambdas:
    function()