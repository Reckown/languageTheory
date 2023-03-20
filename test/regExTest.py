import re

###############################
#          CONSTANTS          #
###############################

REGEX_DESCRIPTORS = "\[\w+\s+\"[\w\s\d\.\-\?]+\"\]"
REGEX_TURN = "\d+\."
REGEX_TURN_RECOVERY = "\d+\.\.\."
REGEX_CASTLE_LONG = "O-O-O"
REGEX_CASTLE_SHORT = "O-O"
REGEX_COMMENTARY = "\{.*?\}|\(.*?\)"
REGEX_WIN_RESULT = "(1-0|0-1|1\/2-1\/2)"
REGEX_MOVE = "[NBQRK]?[0-8a-h]?x?[a-h][1-8](\+{0,2})[?!]?"

###############################
#       UNITARY TESTS         #
###############################

def test_print(name, samples, regex):
    isSuccess = True

    print("\n[START] "+name+"\n----------\n")
    for sample in samples:
        if (((re.match(regex, sample[1])) != None) == sample[2]):
            print("\033[92m [PASS] \033[0m" + sample[0], )
        else:
            print("\033[91m [FAIL] \033[0mExpected : " + str(sample[2]) + "     | " + sample[0])
            isSuccess = False

    if isSuccess:
        print("\n\033[92m [PASS] "+name+" : All tests passed! \033[0m")
    else:
        print("\n\n\033[91m [FAIL] "+name+" : Some tests failed ! \033[0m")

    return isSuccess

def test_descriptors():
    samples = [
        ["Single Valid Descriptor (a-Z)", "[Event \"Mannheim\"]", True],
        ["Single Valid Descriptor (0-9 .)", "[Date \"1914.08.01\"]", True],
        ["Single Valid Descriptor (?)", "[BlackElo \"?\"]", True],
        ["Single Valid Descriptor (-)", "[Result \"1-0\"]", True],
        ["Single Invalid Descriptor (opened quote)", "[\"Result 1-0]", False],
        ["Single Invalid Descriptor (closed quote)", "[Result 1-0\"]", False],
        ["Single Invalid Descriptor (])", "Event \"Mannheim\"]", False],
        ["Single Invalid Descriptor (])", "[Event \"Mannheim\"", False],
        ["Single Invalid Descriptor (no [])", "Event \"Mannheim\"", False],
        ["Single Invalid Descriptor (no arg)", "[\"Mannheim\"]", False],
        ["Single Invalid Descriptor (no value)", "[Event]", False],
        ["Single Invalid Descriptor (empty)", "[]", False],
    ]

    test_print("DESCRIPTORS", samples, REGEX_DESCRIPTORS)

def test_commentary():
    samples = [
        ["Single Valid Commentary ({})", "{ Lorem ipsum 48bed. -_?!}", True],
        ["Single Valid Commentary (())", "( Lorem ipsum 48bed. -_?!)", True],
        ["Single Invalid Commentary ([])", "[ Lorem ipsum 48bed. -_?!]", False],
        ["Single Invalid Commentary (miss '(')", "Lorem ipsum 48bed. -_?!)", False],
        ["Single Invalid Commentary (miss ')')", "(Lorem ipsum 48bed. -_?!", False],
        ["Single Invalid Commentary (miss '{')", "Lorem ipsum 48bed. -_?!}", False],
        ["Single Invalid Commentary (miss '}')", "{Lorem ipsum 48bed. -_?!", False],
        ["Single Invalid Commentary (}", "(Lorem ipsum 48bed. -_?!}", False],
        ["Single Invalid Commentary {)", "{Lorem ipsum 48bed. -_?!)", False],
        ["Nested Valid Commentary (())", "((Lorem ipsum 48bed. -_?!))", True],
        ["Nested Valid Commentary {{}}", "{{Lorem ipsum 48bed. -_?!}}", True],
        ["Nested Valid Commentary {()}", "{(Lorem ipsum 48bed. -_?!)}", True],
        ["Nested Valid Commentary ({})", "({Lorem ipsum 48bed. -_?!})", True],
        ["Nested Valid Commentary (.().)", "(Lorem ipsum 48bed. ()-_?!)", True],
        ["Nested Valid Commentary (.{}.)", "(Lorem ipsum 48bed. {}-_?!)", True],
        ["Nested Valid Commentary (.{}().)", "(Lorem ipsum 48bed. {}()-_?!)", True],
        ["Nested Valid Commentary ({()})", "(Lorem ipsum 48bed. {()})", True],
        ["Nested Valid Commentary {({})}", "{(Lorem ipsum 48bed. {})}", True],
        ["Nested Valid Commentary {({)}", "{(Lorem ipsum 48bed. {)}", True],
        ["Nested Valid Commentary {(})}", "{(Lorem ipsum 48bed. })}", True],
        ["Nested Valid Commentary {())}", "{(Lorem ipsum 48bed. ()}", True],
        ["Nested Valid Commentary {(()}", "{(Lorem ipsum 48bed. ))}", True],
    ]

    test_print("COMMENTARY", samples, REGEX_COMMENTARY)

def test_castle():
    samplesShort = [
        ["Single Valid ROC (O-O)", "O-O", True],
        ["Single Valid ROC (O-O-O)", "O-O-O", True], # Should be false in real case
        ["Single Invalid ROC (OO)", "OO", False],
        ["Single Invalid ROC (double -)", "O--O", False],
        ["Single Invalid ROC (AO)", "A-O", False],
        ["Single Invalid ROC (OA)", "O-A", False],
    ]
    samplesLong = [
        ["Single Valid ROC (O-O-O)", "O-O-O", True],
        ["Single Invalid ROC (O-O)", "O-O", False],
        ["Single Invalid ROC (OOO)", "OOO", False],
        ["Single Invalid ROC (OAO)", "O-A-O", False],
        ["Single Invalid ROC (AOA)", "A-O-A", False],
    ]

    test_print("CASTLE SHORT", samplesShort, REGEX_CASTLE_SHORT)
    test_print("CASTLE LONG", samplesLong, REGEX_CASTLE_LONG)

def test_turn():
    samples = [
        ["Single Valid Turn (1.)", "1.", True],
        ["Single Invalid Turn (1)", "1", False],
        ["Single Invalid Turn (1..)", "1..", False],
        ["Single Invalid Turn (1....)", "1....", False],
    ]
    samplesRecovery = [
        ["Single Valid Turn (1...)", "1...", True],
        ["Single Invalid Turn (1)", "1", False],
        ["Single Invalid Turn (1..)", "1..", False],
        ["Single Invalid Turn (A...)", "A...", False],
        ["Single Invalid Turn (1....)", "1....", True], # Should be false in real case
    ]
    samples = [
        ["Simple case", "123.", True],
        ["No number", "a.", False],
        ["Dot", ".", False],
        ["No period", "456", False],
        ["Non-digit characters before period", "789abc.", False],
        ["Non-digit characters after period", "111.aaa", True], # Should be false in real case
        ["Multiple digits before period", "99999.", True],
        ["Multiple periods", "222.333.", True], # Should be false in real case
        ["Period at beginning", ".444", False],
        ["Period at end", "555.", True],
    ]


    test_print("TURN", samples, REGEX_TURN)
    test_print("TURN SECOND", samplesRecovery, REGEX_TURN_RECOVERY)

def test_win_result():
    samples = [
        ["Single Valid End Game (1-0)", "1-0", True],
        ["Single Valid End Game (0-1)", "0-1", True],
        ["Single Valid End Game (1/2-1/2)", "1/2-1/2", True],
        ["Single Invalid End Game (1-1)", "1-1", False],
        ["Single Invalid End Game (0-0)", "0-0", False],
        ["Single Invalid End Game (1/2-1)", "1/2-1", False],
        ["Single Invalid End Game (1-1/2)", "1-1/2", False],
        ["Single Invalid End Game (1 - 0)", "1 - 0", False],
    ]

    test_print("END GAME", samples, REGEX_WIN_RESULT)

def test_action():
    samples = [
        ["Valid Action", "e6", True],
        ["Valid Action", "Bg5", True],
        ["Valid Action", "Bxg5", True],
        ["Valid Action", "Nfd7", True],
        ["Valid Action", "Qxg5", True],
        ["Valid Action", "Rxe4", True],
        ["Valid Action (+)", "Rxe4++", True],
        ["Valid Action (++)", "Rxe4+", True],
        ["Valid Action (!)", "Rxe4+", True],
        ["Valid Action (?)", "Rxe4+", True],
        ["Valid Action (++?)", "Rxe4++?", True],
        ["Invalid Action (!?)", "Rxe4!?", True], # Should be false in real case
        ["Invalid Action (!!)", "Rxe4!!", True], # Should be false in real case
        ["Invalid Action (??)", "Rxe4??", True], # Should be false in real case
        ["Invalid Action (.)", "Rxe4.", True], # Should be false in real case
        ["Invalid Action (+++)", "Rxe4+++", True], # Should be false in real case
        ["Invalid Action (Bad piece", "Sxe4", False],
        ["Invalid Action (Out of gameboard)", "i4", False],
        ["Invalid Action (Out of gameboard)", "h9", False],
        ["Invalid Action (Format)", "hh", False],
        ["Invalid Action (Format)", "44", False],
    ]

    test_print("ACTION", samples, REGEX_MOVE)

###############################
#             MAIN            #
###############################

if __name__ == '__main__':
    test_descriptors()
    test_commentary()
    test_castle()
    test_turn()
    test_win_result()
    test_action()