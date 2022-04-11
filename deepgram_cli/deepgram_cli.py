import asyncio
import json
import os
import platform
import re

from deepgram import Deepgram

from deepgram_cli.constants import AUDIO_MAPPINGS
from deepgram_cli.utils import get_ext
from deepgram_cli.utils import save_file


if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


class DeepgramCLI:
    """_summary_

    Returns:
        _type_: _description_
    """

    def __init__(
        self, urls: list, files: list, dump_json: bool, batch_list: list, dg: Deepgram
    ) -> None:
        self.dg = dg
        self.urls = urls
        self.files = files
        self.dump_json = dump_json
        self.batch_list = batch_list
        self.loop = asyncio.get_event_loop()

    async def remote(self, url):
        file_path = url.split("?")[0].split("/")[-1]
        source = {"url": url}
        options = {"punctuate": True, "language": "en-US"}

        response = await self.dg.transcription.prerecorded(source, options)
        max_confidence_result = response.get("results").get("channels")[0][0]
        save_file(max_confidence_result["transcript"], f"{file_path}.txt")
        if self.dump_json:
            save_file(json.dumps(response), f"{file_path}.txt")

    async def local(self, file_path):
        with open(file_path, "rb") as audio:
            source = {"buffer": audio, "mimetype": AUDIO_MAPPINGS[get_ext(file_path)]}
            options = {"punctuate": True, "language": "en-US"}

            response = await self.dg.transcription.prerecorded(source, options)
            max_confidence_result = response.get("results").get("channels")[0][
                "alternatives"
            ][0]
            save_file(max_confidence_result["transcript"], f"{file_path}.txt")

            if self.dump_json:
                save_file(json.dumps(response), f"{file_path}.txt")

    async def process(self):
        for file_path in self.files:
            await self.local(file_path)

        for url in self.urls:
            await self.remote(url)

        for f in self.batch_list:
            if re.match(r"^http", f):
                await self.remote(f)
            else:
                await self.local(f)

    def run(self):
        return self.loop.run_until_complete(self.process())
