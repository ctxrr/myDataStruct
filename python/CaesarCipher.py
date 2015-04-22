class CaesarCipher:
    """Class for doing encryption and decryption using Caesar cipher"""

    def __init__(self,shift):
        """Construct Caesar cipher using given integer shift for rotation"""
        encoder = [None]*26
        decoder = [None]*26
        for k in range(26):
            encoder[k] = chr((k+shift) % 26 + ord('A'))
            decoder[k] = chr((k-shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)

    def encrypt(self,message):
        """Return string representing encripted message"""
        return self._transform(message,self._forward)

    def decrypt(self,secret):
        """Return decrypted message given encrypted secret"""
        return self._transform(secret,self._backward)

    def _transform(self,original,code):
        """Utility to proform transformation based on given code string"""
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k])-ord('A')
                msg[k] = code[j]
        return ''.join(msg)

if __name__=='__main__':
    cipher = CaesarCipher(3)
    print cipher._forward
    print cipher._backward
    message = "THE EAGLE IS IN PLAY;MEET AT JOE'S"
    coded = cipher.encrypt(message)
    print('Secret:',coded)
    answer = cipher.decrypt(coded)
    print('Message:',answer)

