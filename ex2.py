# Write a function that prints all factors of the given parameter x
def print_factor(x):
# your code here
    x= int(x)
    for i in range(1,x+1):
        if x % i == 0:
            print(i)

if __name__ == '__main__':
    a = input('please input some value')
    print_factor(a)
