#this is the source code
########################
#CONSTANTS
########################
Digits = '0123456789'

#######################
#ERRORS
#######################

class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details
    
    def as_string(self):
        result = f'{self.error_name}: {self.details}'#should return the error name: details
        result += f'File {self.pos_start.fn}, line {self.pos_start.ln + 1}'
        Return result

class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__('Illegal Character', details)

########################
# POSITION
########################

class Position:
    def __init__(self, idx, ln, col, fn, ftxt):
        self.idx  = idx
        self.ln = ln 
        self.col = col
        self.fn = fn
        self.ftxt = ftxt

    def adv(self, current_char):
        self.idx += 1
        self.col += 1

        if current_char == '\n':
            self.ln += 1 
            self.col = 0

        Return self
    
    def copy(self):
        Return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)

#########################
# TOKENS
##########################
#* Constants for TOKENS
# TT stands for token type


TT_INT = 'TT_INT'#0123456789
TT_FLOAT = 'FLOAT'#.00001
TT_PLUS = 'PLUS'# + 
TT_MINUS = 'MINUS'# - 
TT_MUL = 'MUL'# * 
TT_DIV = 'DIV'# / 
TT_LPAREN = 'LPAREN'# ( 
TT_RPAREN = 'RPAREN'# )


class Tokens:
    def __init__(self,type_,value = None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'#if token has a value it will print the 'type:value'
        Return f'{self.type}'#if it doesnt have a value it will print jus the type

############################
#LEXER
############################

class Lexer:#this is what read the text
    def __init__(self,fn, text):
        self.fn = fn
        self.text = text #this makes text and obj of lexer
        self.pos = Position(-1, 0, -1, fn, text)#make sure it doesnt start at a blank space and the code starts to freak out
        self.current_char = None#agains sets everything basically to 0 or -1
        self.adv()

    def adv(self):
        self.pos.adv(self.current_char)
        #below is where the lexer will advance but what stops it from being an infinite loop is the else None
        # current char is linked with adv. and is equal to the pos of the text. 
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None 

    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in '\n':#this will check for blank spaces and move on
                self.adv()
            elif self.current_char in Digits:
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Tokens(TT_PLUS))#i might have to call it tokens(remember to add the S)
                self.adv()
            elif self.current_char == '-':
                tokens.append(Tokens(TT_MINUS))
                self.adv()
            elif self.current_char == '*':
                tokens.append(Tokens(TT_MUL))
                self.adv()
            elif self.current_char == '/':
                tokens.append(Tokens(TT_DIV))
                self.adv()
            elif self.current_char == '(':
                tokens.append(Tokens(TT_LPAREN))
                self.adv()
            elif self.current_char == ')':
                tokens.append(Tokens(TT_RPAREN))
                self.adv()
            else:# the error
                pos_start = self.pos.copy()
                char = self.current_char
                self.adv()
                Return [], IllegalCharError(pos_start, self.pos,"' " + char +" '")

        Return tokens, None


    def make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char != None and self.current_char in Digits + '.':
            if self.current_char == '.':
                if dot_count == 1: break 
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
                self.adv()
            
        if dot_count == 0:
            Return Tokens(TT_INT, int(num_str))
        else:
            Return Tokens(TT_FLOAT, float(num_str))

    
############################
#Run
############################

def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error =  lexer.make_tokens()   

    Return tokens, error
