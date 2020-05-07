from Crypto.Random import get_random_bytes

class InitialGenerator():

    def __init__(self, isPredictable = False, length = 16, startIv = None):
        self.store = []
        def _getPreditableIVGenerator(self, length, startIv):
            if startIv == None:
                startIv = get_random_bytes(length)
            iv = int(startIv.hex(),base = 16)
            while True:
                yield iv.to_bytes(length, byteorder= 'big')
                self.store.append(iv)
                iv += 1
        self.isPredictable = isPredictable
        self.startIv = startIv
        if isPredictable:
            self.predictableGenerator = _getPreditableIVGenerator(self, length, startIv)

    def getIV(self,length = 16):
        if self.isPredictable:
            iv = next(self.predictableGenerator)[-length:]
        else:
            iv = get_random_bytes(length)
        self.store.append(iv)
        return iv

    def getNonce(self, length = 15):
        nonce = get_random_bytes(length)
        while nonce in self.store:
            nonce = get_random_bytes(length)
        self.store.append(nonce)
        return nonce

    def getPrevious(self):
        return self.store[-1]
