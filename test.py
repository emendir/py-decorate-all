from decorate_all import decorate_all_functions


def test_function():
    print("Hello there")


def test():
    def demo_decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return "Decorator was here!"
        return wrapper

    decorate_all_functions(demo_decorator, __name__)
    assert test_function() == "Decorator was here!"


if __name__ == "__main__":
    test()
