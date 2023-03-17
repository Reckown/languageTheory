import ply.lex as lex

from regExConstants import REGEX_END_GAME, REGEX_TURN, REGEX_TURN_SECOND, REGEX_ROC_LONG, REGEX_ROC_SHORT, \
    REGEX_DESCRIPTORS, REGEX_COMMENTARY, REGEX_ACTION


class Lexer:
    # List of token names.
    # Regular expression rules for simple tokens
    t_VICTORY = REGEX_END_GAME

    t_TURN = REGEX_TURN

    t_TURN_RECOVERY = REGEX_TURN_SECOND

    t_LONG_CASTLE = REGEX_ROC_LONG

    t_SHORT_CASTLE = REGEX_ROC_SHORT

    t_MOVE = REGEX_ACTION

    t_HEADER = REGEX_DESCRIPTORS

    t_COMMENTARY = REGEX_COMMENTARY

    t_ignore = ' \t'

    tokens = ['VICTORY', 'TURN', 'TURN_RECOVERY', 'LONG_CASTLE', 'SHORT_CASTLE',
              'MOVE', 'HEADER', 'COMMENTARY']

    # Error handling rule
    def t_error(self, t):
        print(f'Illegal character {t.value[0]!r}')
        if self.lastErrorPos is None:
            self.lastErrorPos = t.lexpos
            self.lastErrorLine = t.lineno
            self.error.append(t.value[0])
        else:
            if self.lastErrorPos == t.lexpos-1:
                self.error[self.numberError] += t.value[0]
            else:
                self.numberError = self.numberError + 1
                self.error[self.numberError] += t.value[0]
            self.lastErrorPos = t.lexpos
            self.lastErrorLine = t.lineno
            t.lexer.skip(1)

    def __init__(self):
        self.lexer = None
        self.error = []
        self.lastErrorPos = None
        self.lastErrorLine = None
        self.numberError = 0
        self.tokenList = []

    def createLexer(self):
        self.lexer = lex.lex(module=self, )

    # Test it output
    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            self.tokenList.append(tok)
            if not tok:
                break
            print(tok)
        print(self.tokenList)