def decorate(func):
    def wrapper(*args, **kwargs):
        # return uppercase

        print('Before')
        return func(*args, **kwargs).upper()
        print('After')
    return wrapper


@decorate
def sf():
    return 'hello'

if __name__ == '__main__':
    print(sf())
