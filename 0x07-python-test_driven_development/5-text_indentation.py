#!/usr/bin/python3
"""This module contains a function that prints a text with 2 new lines
after each of these characters:
    ``.``, ``?`` and ``:``

Attributes:
    text_indentation (def): print a text with 2 new lines
                            after each of these characters:
                            ``.``, ``?`` and ``:``
"""


def text_indentation(text):
    """Print a text with 2 new lines after each of these characters:
    ``.``, ``?`` and ``:``

    Args:
        text (str): string to print in a specail way

    Note:
        text must be a string, otherwise a ``TypeError`` exception is
        raised

    Usage:
        >>> text_indentation("hello.world?foo:time")
        ... #doctest: +REPORT_NDIFF
        hello.
        <BLANKLINE>
        world?
        <BLANKLINE>
        foo:
        <BLANKLINE>
        time
        """

    if not isinstance(text, str):
        raise TypeError('text must be a string')
    else:
        charset = ['.', '?', ':']
        step = 0
        text_len = len(text)
        while step < text_len:
            if text[step] in charset:
                print('{}\n\n'.format(text[step]), end='')
                step += 1
                if step >= text_len:
                    break
                # move to the next none-space character
                if text[step] == ' ':
                    while (text[step] == ' '):
                        step += 1
                        if step >= text_len:
                            break
            else:
                print(str(text[step]), end='')
                step += 1
