# Write a program that be able to find all factors of the numbers in the list l
l = [52633, 8137, 1024, 999]
# your code here
def print_factor(x):
# your code here
    x= int(x)
    for i in range(1,x+1):
        if x % i == 0:
            print(i)

if __name__ == '__main__':
    for i in l:
        print_factor(i)
