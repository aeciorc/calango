from lexer.tokenizer import Tokenizer

result_tokens = Tokenizer.tokenize('lexer/test_data')
print(result_tokens)

#  _echo(1-1+4)
#  Expected: [ [_echo, (,1,-,1,+,4,)]