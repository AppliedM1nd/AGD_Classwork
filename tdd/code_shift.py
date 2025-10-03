def code(message,shift):
#    if not str(shift).isnumeric():
 #       return  'Enter a numeric shift'
    if isinstance(message, str):
        message = message.lower()
    else:
        return 'Enter a string'
    if isinstance(shift, str):
        return 'Enter an integer'
    codedMessage = ''
    for x in message:
        if x in 'abcdefghijklmnopqrstuvwxyz':
            num = ord(x)
            num += shift
            if num > ord('z'):
                num -= 26
            char = chr(num)
            codedMessage += char
        else:
            codedMessage += x
    return codedMessage

if __name__ == '__main__':
    shift = int(input('Enter your shift: '))
    msg = input('Enter your message: ')
    codedMessage = code(msg,shift)
    print('The encoded message is: ', codedMessage)