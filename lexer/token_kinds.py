class SpecTokens:
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


class UnspecTokens:
    COMMAND = "command"  # external commands like "_echo"
    INTEGER_LITERAL = "integer_literal"

    #  Maps the regex expression that uniquely matches a token kind to its kind
    TOKENS = {
        "^([0-9]+)$": INTEGER_LITERAL,
        "^([0-9a-zA-Z]+)$": COMMAND

    }


def generate_stop_signals():
    stop_signs = set()
    for key, value in SpecTokens.TOKENS.items():
        if value == SpecTokens.SYMBOL:
            stop_signs.add(key)
            if len(key) > 1:
                for char in key:
                    stop_signs.add(char)

    return stop_signs
