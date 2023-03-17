import re

from regExConstants import REGEX_DESCRIPTORS, REGEX_COMMENTARY, REGEX_ROC_SHORT, REGEX_ROC_LONG, REGEX_TURN, \
    REGEX_TURN_SECOND, REGEX_END_GAME


###############################
#       UNITARY TESTS         #
###############################

def test_print(name, samples, regex):
    isSuccess = True

    print("\n[START] " + name + "\n----------\n")
    for sample in samples:
        if ((re.match(regex, sample[1])) != None) == sample[2]:
            print("\033[92m [PASS] \033[0m" + sample[0], )
        else:
            print("\033[91m [FAIL] \033[0mExpected : " + str(sample[2]) + "     | " + sample[0])
            isSuccess = False

    if isSuccess:
        print("\n\033[92m [PASS] " + name + " : All tests passed! \033[0m")
    else:
        print("\n\n\033[91m [FAIL] " + name + " : Some tests failed ! \033[0m")

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
        ["Single Invalid Commentary ([])", "[ Lorem ipsum 48bed. -_?!]", False],
        ["Single Invalid Commentary (())", "( Lorem ipsum 48bed. -_?!)", False],
        ["Nested Valid Commentary (all)", "{ Lorem {( Lorem ipsum {ea}{a}48bed. -_?!)}}", False],
        ["Nested Invalid Commentary (Missing {)", "{ Lorem {( Lorem ipsum }{a}48bed. -_?!)}}", False],
        ["Nested Invalid Commentary (Missing '}')", "{ Lorem {({ Lorem ipsum {a}48bed. -_?!)}}", False],
        ["Nested Invalid Commentary (Missing '(')", "{ Lorem {( Lorem ipsum ){a}48bed. -_?!)}}", False],
        ["Nested Invalid Commentary (Missing ')')", "{ Lorem {(( Lorem ipsum {a}48bed. -_?!)}}", False],
        ["Nested Invalid Commentary (Missing '[')", "{ Lorem {( Lorem ipsum ]{a}48bed. -_?!)}}", False],
        ["Nested Invalid Commentary (Missing ']')", "{ Lorem {([ Lorem ipsum {a}48bed. -_?!)}}", False],
    ]

    test_print("COMMENTARY", samples, REGEX_COMMENTARY)


def test_roc():
    samplesShort = [
        ["Single Valid ROC (O-O)", "O-O", True],
        ["Single Invalid ROC (O-O-O)", "O-O-O", False],
        ["Single Invalid ROC (OO)", "OO", False],
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

    test_print("ROC SHORT", samplesShort, REGEX_ROC_SHORT)
    test_print("ROC LONG", samplesLong, REGEX_ROC_LONG)


def test_turn():
    samples = [
        ["Single Valid Turn (1.)", "1.", True],
        ["Single Invalid Turn (1)", "1", False],
        ["Single Invalid Turn (1..)", "1..", False],
        ["Single Invalid Turn (1....)", "1....", False],
    ]
    samplesSecond = [
        ["Single Valid Turn (1...)", "1...", True],
        ["Single Invalid Turn (1)", "1", False],
        ["Single Invalid Turn (1..)", "1..", False],
        ["Single Invalid Turn (1....)", "1....", False],
    ]

    test_print("TURN", samples, REGEX_TURN)
    test_print("TURN SECOND", samplesSecond, REGEX_TURN_SECOND)


def test_end_game():
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

    test_print("END GAME", samples, REGEX_END_GAME)


###############################
#             MAIN            #
###############################

def testRegEx():
    test_descriptors()
    test_commentary()
    test_roc()
    test_turn()
    test_end_game()
