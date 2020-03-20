import re


class InvalidState(Exception):
    pass


STOP = InvalidState()


def requirement(content):
    return f"Requirement '{content}' didn't meet."


def escape(content):
    content = content.strip("`")
    if re.match("py(thon)?\n", content):
        content = "\n".join(content.splitlines()[1:])
    return content


def as_code(content, lang=""):
    return f"```{lang}\n{escape(content)}```"
