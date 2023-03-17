import lexer
import pgnInputs
from regExTest import testRegEx
import ply.yacc as yacc


def createLexer():
    lex = lexer.createLexer()
    # we can run lex() in debug mode as follows:
    # lexer = lex.lex(debug=True)
    lex.input(pgnInputs.inputOne)
    while True:
        tok = lex.token()
        print(tok)
        if not tok: break
    # Use token


def createParser():
    lex = lexer.createLexer()
    # we can run lex() in debug mode as follows:
    # lexer = lex.lex(debug=True)
    lex.input(pgnInputs.inputOne)
    while True:
        tok = lex.token()
        print(tok)
        if not tok: break
    # Use token
    parser = yacc.yacc()
    result = parser.parse(tok)
    print(result)


# testRegEx()
# createLexer()
createParser()
