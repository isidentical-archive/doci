from pathlib import Path

import discord

EXTENSIONS_DIR = Path(__file__).parent / "extensions"


class Doci(discord.Client):
    def load_extensions(self):
        for extensions in EXTENSIONS_DIR.glob("**/*.py"):
            self.load_extension(extension)
