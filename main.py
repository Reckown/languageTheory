import lexer
from constants import pgnInputs
import ply.yacc as yacc
from test.lexerTest import test_lexer
import parser


def createLexer():
    lex = lexer.Lexer()
    lex.createLexer()
    lex.test(pgnInputs.inputOne)


def createParser():
    lex = lexer.Lexer()
    lex.createLexer()
    lex.test(pgnInputs.inputOne)
    # Use token
    pars = parser.Parser()
    result = pars.parser.parse(pgnInputs.inputFour)
    print(result)


# testRegEx()
# createLexer()
createParser()
# test_lexer()
