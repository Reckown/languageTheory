import lexer
import constants.pgnInputs
import ply.yacc as yacc


# -----------------------------------------------------------------------------
# tokens = ['VICTORY', 'TURN', 'TURN_RECOVERY', 'LONG_CASTLE',
#           'SHORT_CASTLE', 'MOVE', 'HEADER', 'COMMENTARY']
#
#   log         : game
#               | error
#
#   game        : descriptor play result game
#               | empty
#
#   descriptor  : HEADER descriptor
#               | empty
#
#   play        : turn play
#               | empty
#
#   turn        : TURN move_p1 com_p1 move_p2 com_p2
#               | empty
#
#   com_p1      : commentary TURN_RECOVERY
#               | empty
#
#   com_p2      : commentary
#               | empty
#
#   commentary  : COMMENTARY
#
#   move_p1     : MOVE
#               | LONG_CASTLE
#               | SHORT_CASTLE
#
#   move_p2     : MOVE
#               | LONG_CASTLE
#               | SHORT_CASTLE
#
#   result      : VICTORY
#
#   empty       : pass
# -----------------------------------------------------------------------------

class Parser(object):
    tokens = lexer.Lexer.tokens

    def __init__(self):
        self.lexer = lexer.Lexer()
        self.parser = yacc.yacc(module=self)

    # Empty production
    def p_log(self, p):
        """log : game"""
        p[0] = ('game is present', p[1])

    def p_game(self, p):
        """game : descriptor play result game"""
        p[0] = ('game started', p[1], p[2], p[3], p[4])

    def p_game_empty(self, p):
        """game : empty"""
        p[0] = p[1]

    def p_descriptor(self, p):
        """descriptor : HEADER descriptor"""
        p[0] = ('descriptor', p[1], p[2])

    def p_descriptor_empty(self, p):
        """descriptor : empty"""
        p[0] = p[1]

    def p_play(self, p):
        """play : turn play"""
        p[0] = ('play', p[1], p[2])
    def p_play_empty(self, p):
        """play : empty"""
        p[0] = p[1]

    def p_turn(self, p):
        """turn : TURN move_p1 com_p1 move_p2 com_p2"""
        p[0] = ('turn', p[1], p[2], p[3], p[4], p[5])

    def p_turn_empty(self, p):
        """turn : empty"""
        p[0] = p[1]

    def p_com_p1(self, p):
        """com_p1 : commentary TURN_RECOVERY"""
        p[0] = ('com_p1', p[1], p[2])

    def p_com_p1_empty(self, p):
        """com_p1 : empty
           """
        p[0] = p[1]

    def p_com_p2(self, p):
        """com_p2 : commentary"""
        p[0] = ('com_p2', p[1])

    def p_com_p2_empty(self, p):
        """com_p2 : empty
           """
        p[0] = p[1]

    def p_commentary(self, p):
        """commentary : COMMENTARY"""
        p[0] = ('commentary content', p[1])

    def p_move_p1(self, p):
        #  TODO make conditional for castles
        """move_p1 : MOVE
                   | LONG_CASTLE
                   | SHORT_CASTLE"""
        p[0] = ('move_p1', p[1])

    def p_move_p2(self, p):
        #  TODO make conditional for castles +
        #   assess possibility for the move to be null.
        """move_p2 : MOVE
                   | LONG_CASTLE
                   | SHORT_CASTLE"""
        p[0] = ('move_p2', p[1])

    def p_result(self, p):
        """result : VICTORY"""
        p[0] = ('result', p[1])

    def p_error(self, p):
        print("Syntax error in input!")

    def p_empty(self, p):
        """empty :"""
        pass
    # Error rule for syntax errors


