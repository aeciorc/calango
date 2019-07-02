import re
from lexer.token_kinds import SpecTokens, UnspecTokens, load_pausers
from lexer.token import Token

PAUSERS = load_pausers()

def tokenize(filename):
    tokens = []
    with open(filename) as code:
        line_number = 1
        code_line = code.readline()
        while code_line:
            line_tokens = tokenize_line(code_line, line_number)
            line_tokens and tokens.append(line_tokens)
            code_line = code.readline()
    return tokens

# token_value can be a char array or a string
def create_token(token_value):
    token_string = ''.join(token_value)
    if token_string in SpecTokens.TOKENS:
        return Token(token_string, SpecTokens.TOKENS[token_string])
    else:
        for key in UnspecTokens.TOKENS:
            if re.match(key, token_string):
                return Token(token_string, UnspecTokens.TOKENS[key])
    raise Exception("Unexpected token: {}".format(token_string))


def tokenize_line(code_line, line_number):
    line_tokens = []
    current_token = []  # temp char array
    for char in code_line:
        if char == '\n':
            if current_token:
                try:
                    line_tokens.append(create_token(current_token))
                    break
                except Exception as e:
                    raise Exception("{} at line {}".format(e, line_number))
        if current_token and current_token[-1] in PAUSERS and char not in PAUSERS:
            try:
                line_tokens.append(create_token(current_token))
                current_token = [char]
            except Exception as e:
                raise Exception("{} at line {}".format(e, line_number))
        elif char == ' ':
            if current_token:
                try:
                    line_tokens.append(create_token(current_token))
                    current_token = []
                except Exception as e:
                    raise Exception("{} at line {}".format(e, line_number))
        elif char in PAUSERS:
            if not current_token:
                current_token.append(char)
            else:
                current_token_string = "".join(current_token)
                tentative_token = current_token_string + char
                if tentative_token in PAUSERS:
                    try:
                        line_tokens.append(create_token(tentative_token))
                        current_token = []
                    except Exception as e:
                        raise Exception("{} at line {}".format(e, line_number))
                else:
                    try:
                        line_tokens.append(create_token(current_token_string))
                        current_token = [char]
                    except Exception as e:
                        raise Exception("{} at line {}".format(e, line_number))
        else:
            current_token.append(char)

    return line_tokens
