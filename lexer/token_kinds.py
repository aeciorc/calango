class Symbols:
    NAME = "symbol"  # + -  ( ) [ ] ..

    #  Maps the string literal of a token to its kind
    SINGLETS = {
        '+',
        '-',
        '(',
        ')',
        ']',
        '[',

    }
    DOUBLETS = {
        '..'
    }

    #  returns the a set containing the individual chars that make up double tokens
    @staticmethod
    def double_tokens_singlets():
        singlets = set()
        for key in Symbols.DOUBLETS:
            for char in key:
                singlets.add(char)
        return singlets


class Identifiers:
    NAME = "identifier"


class Keywords:
    NAME = "keyword"
    VALUES = {'if', 'for', 'else'}


class Numbers:
    NAME = "number"
