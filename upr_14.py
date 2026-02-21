
def my_function():
    return 2 ** 2

nums = [2, 3, 4, 5]
if __name__ == '__main__':
    lambda_function = lambda x: x ** 2
    print(lambda_function(4))

    squared = list(map(lambda x: x ** 2, nums))
    
    for num in squared:
        print(f"{num}", end=" ")