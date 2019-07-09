class CommonTokens:
    KEYWORD = "keyword"  # not yet used
    SYMBOL = "symbol"  # + -  ( ) [ ] ..

    #  Maps the string literal of a token to its kind
    TOKENS = {
        '+': SYMBOL,
        '-': SYMBOL,
        '(': SYMBOL,
        ')': SYMBOL,
        ']': SYMBOL,
        '[': SYMBOL,
        '..': SYMBOL,
    }


class Identifiers:
    COMMAND = "command"  # external commands like "_echo"
    INTEGER_LITERAL = "integer_literal"

    #  Maps the regex expression that uniquely matches a token kind to its kind
    TOKENS = {
        "^([0-9]+)$": INTEGER_LITERAL,
        "^([0-9a-zA-Z]+)$": COMMAND

    }


def load_pausers():
    stop_signs = set()
    for key, value in CommonTokens.TOKENS.items():
        if value == CommonTokens.SYMBOL:
            stop_signs.add(key)
            if len(key) > 1:
                for char in key:
                    stop_signs.add(char)

    return stop_signs
