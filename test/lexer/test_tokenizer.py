import unittest
from unittest.mock import mock_open, patch

from lexer.tokenizer import tokenize, SyntaxError
from lexer.token_kinds import *
from lexer.token import Token


class TestTokenizer(unittest.TestCase):
    def test_valid_input_single_line(self):
        code_mock = "echo([1 .. 4])\n"

        expected_result = [
            [Token('echo', Identifiers.NAME), Token('(', Symbols.NAME), Token('[', Symbols.NAME),
             Token('1', Numbers.NAME),
             Token('..', Symbols.NAME), Token('4', Numbers.NAME), Token(']', Symbols.NAME), Token(')', Symbols.NAME)]]

        with patch('lexer.tokenizer.open',
                   new=mock_open(read_data=code_mock)) as _file:
            result = tokenize('path')
            self.assertListEqual(expected_result, result)

    def test_valid_input_multiple_lines(self):
        code_mock = "echo([1 .. 99])\n" \
                    "echo(1 - 1+ 4)\n"

        expected_result = \
            [
                [Token('echo', Identifiers.NAME), Token('(', Symbols.NAME), Token('[', Symbols.NAME),
                 Token('1', Numbers.NAME),
                 Token('..', Symbols.NAME), Token('99', Numbers.NAME), Token(']', Symbols.NAME),
                 Token(')', Symbols.NAME)],

                [Token('echo', Identifiers.NAME), Token('(', Symbols.NAME), Token('1', Numbers.NAME),
                 Token('-', Symbols.NAME), Token('1', Numbers.NAME), Token('+', Symbols.NAME),
                 Token('4', Numbers.NAME), Token(')', Symbols.NAME)]
            ]

        with patch('lexer.tokenizer.open',
                   new=mock_open(read_data=code_mock)) as _file:
            result = tokenize('path')
            self.assertListEqual(expected_result, result)

    def test_invalid_input(self):
        code_mock = "echo|1-1+4)\n"

        with patch('lexer.tokenizer.open',
                   new=mock_open(read_data=code_mock)) as _file:
            result = None
            try:
                result = tokenize('path')
            except Exception as e:
                self.assertIsInstance(e, SyntaxError)
