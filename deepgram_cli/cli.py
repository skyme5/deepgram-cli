import argparse
import sys


def parse_arguments():
    """Console script for deepgram_cli."""
    parser = argparse.ArgumentParser(prog="deepgram-cli")

    any_one_group = parser.add_mutually_exclusive_group()

    any_one_group.add_argument(
        "-f",
        "--file",
        action="store",
        nargs="*",
        help="At least one or more audio file path to transcribe.",
        dest="files",
        default=[],
    )

    any_one_group.add_argument(
        "-u",
        "--url",
        action="store",
        nargs="*",
        help="At least one or more urls to transcribe.",
        dest="urls",
        default=[],
    )

    any_one_group.add_argument(
        "-i",
        "--batch-file",
        action="store",
        help="Read files/orls from batch file (one per line).",
        metavar="BATCH_FILENAME",
        dest="batch_file",
        default=None,
    )

    parser.add_argument(
        "-d",
        "--dump-json",
        action="store_true",
        help="Save metadata to a JSON file.",
        dest="dump_json",
    )

    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="Do not print anything except errors to the console.",
    )

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    return parser.parse_args()
