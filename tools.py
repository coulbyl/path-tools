file_system = [
    (1024 ** 5, 'Po'), (1024 ** 4, 'To'), (1024 ** 3, 'Go'),
    (1024 ** 2, 'Mo'), (1024 ** 1, 'Ko'), (1024 ** 0, 'octet')
]

social_network_system = [
    (1000 ** 5, 'P'), (1000 ** 4, 'T'), (1000 ** 3, 'G'),
    (1000 ** 2, 'M'), (1000 ** 1, 'K'), (1000 ** 0, ''),
]

suffix = ''
factor = 1000 ** 0


def human_readable(number: int, is_file_sys=False) -> str:
    global factor, suffix

    system = file_system if is_file_sys else social_network_system

    for factor, suffix in system:
        if number >= factor:
            break

    result = number / factor

    return f'{int(result)} {suffix}' if result.is_integer() else f'{result:.1f} {suffix}'


# █
def progress_bar(iterable, decimals=1, length=50, fill='#', print_end="\r"):
    total = len(iterable)

    def print_progress_bar(iteration):
        try:
            percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
            filled_length = int(length * iteration // total)
            bar = fill * filled_length + '-' * (length - filled_length)
            print(f'\rProgress |{bar}| {percent}% Complete', end=print_end)
        except ZeroDivisionError:
            pass

    print_progress_bar(0)

    for i, item in enumerate(iterable):
        yield item
        print_progress_bar(i + 1)

    print()


def get_func_exec_time(func):
    from time import time

    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'It took {int(t2 - t1)} seconds\n')
        return result

    return wrapper
