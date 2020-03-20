import ast
import tokenize

import discord
from discord.ext.commands import Cog, Context, command

from doci.shortcuts import STOP, as_code, escape, requirement

MAX_CODE_LENGTH = 200


class PyDump(Cog):
    async def verify_code(self, ctx, code):
        if code is None:
            await ctx.send(requirement("code"))
            return STOP

        code = escape(code)
        if len(code) > MAX_CODE_LENGTH:
            await ctx.send(requirement("maximum code length"))
            return STOP

        return code

    @command()
    async def maketree(self, ctx, *, code: str):
        code = await self.verify_code(ctx, code)
        if code is STOP:
            return STOP

        try:
            tree = ast.parse(code, filename="<doci>")
        except SyntaxError as exc:
            await ctx.send(exc)
            return STOP
        else:
            representation = ast.dump(tree, indent=4)

        await ctx.send(as_code(representation))

    @command()
    async def tokenize(self, ctx, *, code: str):
        code = await self.verify_code(ctx, code)
        if code is STOP:
            return STOP

        await ctx.send(
            as_code(
                "\n".join(
                    repr(token_info)
                    for token_info in tokenize.generate_tokens(
                        iter(code.splitlines()).__next__
                    )
                )
            )
        )


def setup(bot):
    bot.add_cog(PyDump())
