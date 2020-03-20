import traceback

import discord
from discord.ext.commands import Cog

from doci.shortcuts import InvalidState, as_code


class ErrorHandler(Cog):
    @Cog.listener()
    async def on_command_error(self, ctx, exception):
        if isinstance(exception, InvalidState):
            await ctx.send(
                "Please give an input that meets the requirement next time."
            )
        else:
            formatted_exception = traceback.format_exception(
                type(exception), exception, exception.__traceback__
            )
            await ctx.send(as_code("\n".join(formatted_exception)))


def setup(bot):
    bot.add_cog(ErrorHandler())
