import os
import sys
from ast import dump

from deepgram import Deepgram
from dotenv import load_dotenv

from deepgram_cli.cli import parse_arguments
from deepgram_cli.deepgram_cli import DeepgramCLI

load_dotenv()


def main():
    """Download transcripts from Deepgram."""
    args = parse_arguments()

    dg_client = Deepgram(os.getenv("DEEPGRAM_API_KEY"))

    batch_file = []
    if args.batch_file and os.path.isfile(args.batch_file):
        with open(args.batch_file, "r") as f:
            batch_file = f.read().split("\n")

    app = DeepgramCLI(
        urls=args.urls,
        files=args.files,
        dump_json=args.dump_json,
        batch_list=batch_file,
        dg=dg_client,
    )
    app.run()


if __name__ == "__main__":
    print(23)
    sys.exit(main())
