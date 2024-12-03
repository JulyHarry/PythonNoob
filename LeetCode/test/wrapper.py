import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                    filename=f'log/wrapper_log_{time.strftime('%Y%m%d', time.localtime())}.log', filemode='a')


def timer_log(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        execute_time = time.time() - start_time
        content = f"Function '{func.__name__}' took {execute_time} seconds to execute"
        # print(content)
        logging.info(content)
        return result

    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        execute_time = time.time() - start_time
        content = f"Function '{func.__name__}' took {execute_time} seconds to execute"
        print(content)
        return result

    return wrapper
