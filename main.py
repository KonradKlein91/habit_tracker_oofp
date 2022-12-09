import fire

def hello(name):
    """
    This is a simple program that greets NAME for a total of NUMBER times.
    """
    print(f"Hello {name}")


if __name__ == "__main__":
    fire.Fire()  # Call main function
