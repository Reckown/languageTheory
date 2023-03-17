import sys
import ply.lex as lex

from regExConstants import REGEX_END_GAME, REGEX_TURN, REGEX_TURN_SECOND, REGEX_ROC_LONG, REGEX_ROC_SHORT, \
    REGEX_DESCRIPTORS, REGEX_COMMENTARY, REGEX_ACTION


def createLexer():
    # List of token names.
    tokens = ['VICTORY', 'TURN', 'TURN_RECOVERY', 'LONG_CASTLE', 'SHORT_CASTLE',
              'MOVE', 'HEADER', 'COMMENTARY']
    # Regular expression rules for simple tokens
    t_VICTORY = REGEX_END_GAME

    t_TURN = REGEX_TURN

    TURN_RECOVERY = REGEX_TURN_SECOND

    t_LONG_CASTLE = REGEX_ROC_LONG

    t_SHORT_CASTLE = REGEX_ROC_SHORT

    t_MOVE = REGEX_ACTION

    t_HEADER = REGEX_DESCRIPTORS

    t_COMMENTARY = REGEX_COMMENTARY

    t_ignore = ' \t'

    # Error handling rule
    def t_error(t):
        if t.lexpos < len(t.value):
            print("Illegal character '%s'" % t.value[t.lexpos], file=sys.stderr)
        t.lexer.skip(1)

    lexer = lex.lex()
    return lexer
