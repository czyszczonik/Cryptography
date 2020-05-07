import argparse

from key_util import getKey, getDefaultKey


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", help="Encryption mode", default="CBC")
    parser.add_argument("--path", help="Path to keystore")
    parser.add_argument("--password", help="Keystore password")
    parser.add_argument("--alias", help="Key alias")
    parser.add_argument("--challenge", action="store_true", help="Enable challenge mode (Oracle is default)")
    subparsers = parser.add_subparsers(help='Type of Input')
    file_parser(subparsers)
    message_parser(subparsers)
    verify_input(parser)
    return parser.parse_args(), is_file_mode(parser)

def verify_input(parser):
    messages = vars(parser.parse_args()).get("messages")
    files = vars(parser.parse_args()).get("files")
    if files is None and messages is None:
        print("You don't pass any argument!")
        exit(-1)

def is_file_mode(parser):
    message = vars(parser.parse_args()).get("messages")
    return message is None

def file_parser(subparser):
    file_parser = subparser.add_parser("file")
    file_parser.add_argument("files", type=argparse.FileType("r"), nargs="+", default=None)

def message_parser(subparser):
    message_parser = subparser.add_parser("message")
    message_parser.add_argument("messages", nargs="+")

def get_key(args):
    if args.path is None or args.password is None or args.alias is None:
        print("Using default key!")
        key = getDefaultKey()
    else:
        key = getKey(args.path, args.alias ,args.password)
    return key

def get_files(args):
    messages = []
    for file in args.files:
        messages.append(file.read().replace('\n', ''))
    return messages

def get_messages(args):
    return args.messages
