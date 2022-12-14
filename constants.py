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

# COMPARISON AND OPERATORS
TOKEN_EQUALS_EQUALS     = "EQUALS_EQUALS"
TOKEN_NOT_EQUALS        = "NOT_EQUALS"
TOKEN_LESS_THAN         = "LESS_THAN"
TOKEN_GREATER_THAN      = "GREATER_THAN"
TOKEN_LESS_EQUALS       = "LESS_OR_EQUALS"
TOKEN_GREATER_EQUALS    = "GREATER_OR_EQUALS"

# KEYWORDS
KEYWORDS = [
    "let",
    "const", # not implemented yet
    "and",
    "or",
    "not",
    "if",
    "then",
    "elif",
    "else",
]

# DIGITS
DIGITS = string.digits
LETTERS = string.ascii_letters
LETTERS_DIGITS = LETTERS + DIGITS
