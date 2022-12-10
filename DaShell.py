#this is the shell
import SC


while True:
    text = input('SC >')
    result, error = SC.run('<stdin>', text)

    if error: print(error.as_string())
    else:
        print(result)