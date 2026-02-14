# Напишете следните функции : Лице на цвадрат, лице на куб, обем на куб
def print_sqrt(a):
    return a * a

def print_v_kube(a):
    return print_sqrt(a) * a

def print_s_kube(a):
    return print_sqrt(a) * 6

if __name__ == "__main__":
    a = int(input())
    print(print_sqrt(a))
    print(print_v_kube(a))
    print(print_s_kube(a))

