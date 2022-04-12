<p>
  <div align="center">
  <h1>
    deepgram-cli for batch transcribing files/urls<br /> <br />
    <a href="https://pypi.python.org/pypi/deepgram-cli">
      <img
        src="https://img.shields.io/pypi/v/deepgram-cli.svg?cacheSeconds=360"
        alt="Python Package"
      />
    </a>
    <a href="https://pypi.python.org/pypi/deepgram-cli">
      <img
        src="https://img.shields.io/pypi/wheel/deepgram-cli"
        alt="Python Wheel"
      />
    </a>
    <a href="https://pypi.python.org/pypi/deepgram-cli">
      <img
        src="https://img.shields.io/github/workflow/status/skyme5/deepgram-cli/build?cacheSeconds=360"
        alt="CI"
      />
    </a>
    <!-- <a href="https://codecov.io/gh/skyme5/deepgram-cli">
      <img
        src="https://img.shields.io/codecov/c/github/skyme5/deepgram-cli?cacheSeconds=360"
        alt="Code Coverage"
      />
    </a> -->
    <a href="https://codecov.io/gh/skyme5/deepgram-cli">
      <img
        src="https://img.shields.io/pypi/pyversions/deepgram-cli"
        alt="Python Versions"
      />
    </a>
    <a href="https://github.com/psf/black">
      <img
        src="https://img.shields.io/badge/code%20style-black-000000.svg"
        alt="The Uncompromising Code Formatter"
      />
    </a>
    <a href="https://opensource.org/licenses/MIT">
      <img
        src="https://img.shields.io/badge/License-MIT-blue.svg"
        alt="License: MIT"
      />
    </a>
  </h1>
  </div>
</p>


## Installation

```
pip install git+https://github.com/skyme5/deepgram-cli.git
```

Also set your `DEEPGRAM_API_KEY` for it to work.

## Usage

```bash
usage: deepgram-cli [-h] [-f [FILES ...] | -u [URLS ...] | -i BATCH_FILENAME] [-d] [-q]

options:
  -h, --help            show this help message and exit
  -f [FILES ...], --file [FILES ...]
                        At least one or more audio file path to transcribe.
  -u [URLS ...], --url [URLS ...]
                        At least one or more urls to transcribe.
  -i BATCH_FILENAME, --batch-file BATCH_FILENAME
                        Read files/orls from batch file (one per line).
  -d, --dump-json       Save metadata to a JSON file.
  -q, --quiet           Do not print anything except errors to the console.
```

# License

MIT
