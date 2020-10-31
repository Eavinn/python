from collections.abc import Iterable

print(isinstance([], Iterable))

def fib(n):
    current = 0
    num1, num2 = 0, 1
    while current < n:
        yield num1  # 假如函数中有yield，则不再是迭代器，而是生成器
        num1, num2 = num2, num1 + num2
        current += 1


if __name__ == '__main__':
    # 假如函数中有yield，则不再是函数，而是一个生成器
    gen = fib(5)

    # 取得生成器的下一个值
    print(next(gen))
    print(next(gen))
    print(next(gen))