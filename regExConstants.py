###############################
#          CONSTANTS          #
###############################

# REGEX_DESCRIPTORS = "\[\w+\s+\"[\w\s\d\.\-\?]+\"\]"
# REGEX_TURN = "\d+\."
# REGEX_TURN_SECOND = "\d+\..."
# REGEX_ROC_LONG = "\s*O-O-O"
# REGEX_ROC_SHORT = "\s*O-O"
# REGEX_COMMENTARY = "\{[^\{\}]*\}"
# REGEX_END_GAME = "(1-0|0-1|1\/2-1\/2)"

REGEX_DESCRIPTORS = "\[\w+\s+\"[\w\s\d\.\-\?]+\"\]"
REGEX_TURN = "\d+\.\s"
REGEX_TURN_SECOND = "\d+\.\.\."
REGEX_ROC_LONG = "O-O-O"
REGEX_ROC_SHORT = "(?<=\s)O-O(?=\s)"
REGEX_COMMENTARY = "\(([^()]+|())*\)|\{([^{}]+|())*\}"
REGEX_END_GAME = "(1-0|0-1|1\/2-1\/2)"
REGEX_ACTION = "(?<=\s)[NBQRK]?[0-8a-h]?x?[a-h][1-8](\+{0,2})(?=\s)"