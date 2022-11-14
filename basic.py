#basic
import sys,time

def delay_print(c):
    for s in c:
        sys.stdout.write(s)
        sys.stdout.flush()
        time.sleep(0.005)

##############################
#*******CONSTANTS
##############################

DIGITS = '0123456789'

##############################
#****ERRORS
##############################

class Error:
    def __init__(self,error_name,details):
        self.error_name = error_name
        self.details = details

    def as_string(self):
        result = f"{self.error_name}: {self.details}"
        return result

class IllegelCharError(Error):
    def __init__(self, error_name, details):
        super().__init__('Illegal Characters', details)


#############################
# ****TOKEN******
#############################

TT_INT = 'TT_INT'
TT_FLOAT = 'FLOAT'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL' 
TT_DIV = 'DIV'
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'
TT_BOOLEAN = 'BOOLEAN'

class Token:
    def __init__(self, type_,value = None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

        #this gives token a representive so when the token called on it'll print the type and then
        #the value and if it doesnt have a value itll print the type instead

##############################
### ********Lexer
#############################

class Lexer:
    def __init__(self,text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.adv()
    def adv(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in ' \t':
                self.adv() 
            elif self.current_char in DIGITS:
                tokens.append(self.make_number)
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS))
                self.adv()
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS))
                self.adv()
            elif self.current_char == '*':
                tokens.append(Token(TT_MUL))
                self.adv()
            elif self.current_char == '/':
                tokens.append(Token(TT_DIV))
                self.adv()
            elif self.current_char == '(':
                tokens.append(Token(TT_LPAREN))
                self.adv()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN))
                self.adv()
            else:
                char = self.current_char
                self.adv()
                return[], IllegelCharError("'" + char + "'")

        return tokens, None

def make_number(self):
    num_str = ''
    dot_count = 0

    while self.current_char != None and self.current_char in DIGITS + '.':
        if self.current_char == '.':
            if dot_count == 1: break
            dot_count += 1
            num_str += 1
        else:
            num_str += self.current_char
        self.adv()

    if dot_count == 0:
        return Token(TT_INT, int(num_str))
    else:
        return Token(TT_FLOAT, float(num_str))



################################
#* RUN
################################

def run(text):
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens()

    return tokens, error

delay_print('My First attempt at writing a program.\n(name is still top secrect.)\n')
delay_print('For now the program can use basic math operators.\n')
delay_print('|###      <<<...Still Under Construction###Caution>>>      ####\n')