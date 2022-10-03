import string

# TOKENS
TOKEN_INT               = "INT"
TOKEN_FLOAT             = "LOAT"
TOKEN_PLUS              = "PLUS"
TOKEN_MINUS             = "MINUS"
TOKEN_MULTIPLY          = "STAR"
TOKEN_DIVIDE            = "SLASH"
TOKEN_POWER             = "POWER"
TOKEN_RIGHT_PARENTHESIS = "RIGHT_PARENTHESIS"
TOKEN_LEFT_PARENTHESIS  = "LEFT_PARENTHESIS"
TOKEN_EOF               = "END_OF_FILE"

# VARIABLES RELATED STUFF
TOKEN_IDENTIFIER        = "IDENTIFIER"
TOKEN_KEYWORD           = "KEYWORD"
TOKEN_EQUALS            = "EQUALS"

# KEYWORDS
KEYWORDS = [
    "let"
]

# DIGITS
DIGITS = string.digits
LETTERS = string.ascii_letters
LETTERS_DIGITS = LETTERS + DIGITS
