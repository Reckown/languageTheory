# -----------------------------------------------------------------------------
# tokens = ['VICTORY', 'TURN', 'TURN_RECOVERY', 'LONG_CASTLE',
#           'SHORT_CASTLE', 'MOVE', 'HEADER', 'COMMENTARY']
#
#   log : game | empty
#
#   game : descriptor play result game | empty
#
#   descriptor : HEADER descriptor | empty
#
#   play : turn  play | empty
#
#   turn : TURN move_p1 com_p1 move_p2 com_p2 | empty
#
#   com_p1 : commentary TURN_RECOVERY | empty
#
#   com_p2 : commentary | empty
#
#   commentary : COMMENTARY
#
#   move_p1 : MOVE | LONG_CASTLE | SHORT_CASTLE
#
#   move_p2 : MOVE | LONG_CASTLE | SHORT_CASTLE
#
#   result : VICTORY
#
# -----------------------------------------------------------------------------

def createParser():
    def p_start(p):
        """start : game | """
        p[0] = p[1] + p[3]

    def p_game(p):
        """expression : expression MINUS term"""
        p[0] = p[1] - p[3]

    def p_descriptor(p):
        """expression : term"""
        p[0] = p[1]

    def p_play(p):
        """term : term TIMES factor"""
        p[0] = p[1] * p[3]

    def p_turn(p):
        """term : term DIVIDE factor"""
        p[0] = p[1] / p[3]

    def p_comm1(p):
        """term : factor"""
        p[0] = p[1]

    def p_comm2(p):
        'factor : NUMBER'
        p[0] = p[1]

    def p_commentary(p):
        """factor : LPAREN expression RPAREN"""
        p[0] = p[2]

    # Error rule for syntax errors
    def p_move1(p):
        print("Syntax error in input!")

    # Error rule for syntax errors
    def p_move2(p):
        print("Syntax error in input!")

    # Error rule for syntax errors
    def p_win(p):
        print("Syntax error in input!")

    # Error rule for syntax errors
    def p_error(p):
        print("Syntax error in input!")
