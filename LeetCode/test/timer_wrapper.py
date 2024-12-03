import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        execute_time = time.time() - start_time
        content = f"Function '{func.__name__}' took {execute_time} seconds to execute"
        print(content)
        return result

    return wrapper
