import re
from lexer.token_kinds import SpecTokens, UnspecTokens, generate_stop_signals
from lexer.token import Token

STOP_SIGNALS = generate_stop_signals()


class Tokenizer:
    @staticmethod
    def tokenize(filename):
        tokens = []
        with open(filename) as code:
            line_number = 1
            code_line = code.readline()
            while code_line:
                line_tokens = Tokenizer.tokenize_line(code_line, line_number)
                line_tokens and tokens.append(line_tokens)
                code_line = code.readline()
        return tokens

    @staticmethod
    def tokenize_line(code_line, line_number):
        line_tokens = []
        current_token = []  # temp char array
        for char in code_line:
            if char == '\n':
                if current_token:
                    try:
                        line_tokens.append(Tokenizer.create_token(current_token))
                        break
                    except Exception as e:
                        raise Exception("{} at line {}".format(e, line_number))
            if char == ' ':
                if current_token:
                    try:
                        line_tokens.append(Tokenizer.create_token(current_token))
                        current_token = []
                    except Exception as e:
                        raise Exception("{} at line {}".format(e, line_number))
            elif char in STOP_SIGNALS:
                if not current_token:
                    current_token.append(char)
                else:
                    current_token_string = "".join(current_token)
                    tentative_token = current_token_string + char
                    if tentative_token in STOP_SIGNALS:
                        try:
                            line_tokens.append(Tokenizer.create_token(tentative_token))
                            current_token = []
                        except Exception as e:
                            raise Exception("{} at line {}".format(e, line_number))
                    else:
                        try:
                            line_tokens.append(Tokenizer.create_token(current_token_string))
                            current_token = [char]
                        except Exception as e:
                            raise Exception("{} at line {}".format(e, line_number))
            else:
                current_token.append(char)

        return line_tokens

    @staticmethod
    def create_token(token_chars):
        token_string = ''.join(token_chars)
        if token_string in SpecTokens.TOKENS:
            return Token(token_string, SpecTokens.TOKENS[token_string])
        else:
            for key in UnspecTokens.TOKENS:
                if re.match(key, token_string):
                    return Token(token_string, UnspecTokens.TOKENS[key])
        raise Exception("Unexpected token: {}".format(token_string))
