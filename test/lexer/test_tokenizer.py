import unittest
from unittest.mock import mock_open, patch

from lexer.tokenizer import tokenize
from lexer.token import Token


class TestTokenizer(unittest.TestCase):
    def test_valid_input_single_line(self):
        code_mock = "echo([1..4])\n"

        expected_result = [
            [Token('echo', 'command'), Token('(', 'symbol'), Token('[', 'symbol'), Token('1', 'integer_literal'),
             Token('..', 'symbol'), Token('4', 'integer_literal'), Token(']', 'symbol'), Token(')', 'symbol')]]

        with patch('lexer.tokenizer.open',
                   new=mock_open(read_data=code_mock)) as _file:
            result = tokenize('path')
            self.assertListEqual(expected_result, result)

    def test_valid_input_multiple_lines(self):
        code_mock = "echo([1..4])\n" \
                    "echo(1-1+4)\n"

        expected_result = \
            [
                [Token('echo', 'command'), Token('(', 'symbol'), Token('[', 'symbol'), Token('1', 'integer_literal'),
                 Token('..', 'symbol'), Token('4', 'integer_literal'), Token(']', 'symbol'), Token(')', 'symbol')],

                [Token('echo', 'command'), Token('(', 'symbol'), Token('1', 'integer_literal'),
                 Token('-', 'symbol'), Token('1', 'integer_literal'), Token('+', 'symbol'),
                 Token('4', 'integer_literal'), Token(')', 'symbol')]
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
                self.assertIsNone(result)
