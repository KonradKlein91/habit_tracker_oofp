import argparse

class habit:
    def __init__(self, name, periodicity):
        self.habit_name = name
        self.periodicity = periodicity

def say_hello(args):
    if args.name:
        print(f'Hello {args.name}!')

    else:
        print(f'Hallo Stranger')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name')
    args = parser.parse_args()
    say_hello(args)


if __name__ == '__main__':
    main()
