import sys


def parse_cli_arguments():
    """
    Parse the dataset path as a position CLI argument
    """
    if len(sys.argv) < 2:
        raise Exception("Please provide the path to the dataset as an argument")
    return sys.argv[1]
