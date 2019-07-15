import re
from lexer.token_kinds import Symbols, Identifiers, Keywords, Numbers
from lexer.token import Token
from more_itertools import peekable


class SyntaxError(Exception):
    """Unexpected token"""
    pass


doublet_pieces = Symbols.double_tokens_singlets()


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


def tokenize_line(code_line, line_number):
    line_tokens = []
    line = peekable(code_line)
    ch = next(line)

    while ch != "\n":

        # Case 0: whitespace
        if ch == " ":
            pass

        #  Case 1: doublet symbols
        elif ch in doublet_pieces and ch + line.peek('') in Symbols.DOUBLETS:
            line_tokens.append(Token(ch + next(line), Symbols.NAME))

        #  Case 2: singlet symbols
        elif ch in Symbols.SINGLETS:
            line_tokens.append(Token(ch, Symbols.NAME))

        #   Case 3: identifier or keyword
        elif ch.isalpha():
            token_chars = [ch]
            while ''.join(line.peek('')).isalnum():
                token_chars.append(next(line))
            token = ''.join(token_chars)
            line_tokens.append(Token(token, Keywords.NAME if token in Keywords.VALUES else Identifiers.NAME))

        #   Case 4: number
        elif ch.isdigit():
            token_chars = [ch]
            while ''.join(line.peek('')).isdigit():
                token_chars.append(next(line))
            else:
                if line.peek('') == '.':
                    token_chars.append(next(line))
                    while ''.join(line.peek('')).isdigit():
                        token_chars.append(next(line))
            #  A letter immediately after a number is a syntactic error

            if ''.join(line.peek('')).isalpha():
                raise SyntaxError("Malformed number at line {}".format(line_number))

            line_tokens.append(Token(''.join(token_chars), Numbers.NAME))

        else:
            raise SyntaxError("Unexpected token {} at line {}".format(ch, line_number))

        ch = next(line)

    return line_tokens
