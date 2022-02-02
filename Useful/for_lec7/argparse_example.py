import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Searches for pattern in image')
    parser.add_argument('-a', '--a_arg', help='A-argument')
    parser.add_argument('-b', '--b_arg', help='B-argument')
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    print(f"{args.a_arg=}")
    print(f"{args.b_arg=}")
