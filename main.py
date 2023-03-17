import lexer
import pgnInputs
import parser
from regExTest import testRegEx
import ply.yacc as yacc


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
#createLexer()
createParser()
