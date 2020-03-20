from pathlib import Path

import discord
from discord.ext import commands

EXTENSIONS_DIR = Path(__file__).parent / "extensions"


class Doci(commands.Bot):
    def load_extensions(self):
        for extension in EXTENSIONS_DIR.glob("**/*.py"):
            if extension.stem == "__init__":
                continue
            self.load_extension(f"doci.extensions.{extension.stem}")
