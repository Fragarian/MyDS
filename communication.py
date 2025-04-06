"""
통신에 사용되는 메세지+전자서명 조합과
통신을 주고받는 인물을 추상화한 클래스들.
"""

class Package:
    def __init__(self, message:str, signature:bytes):
        self.__message: bytes = message.encode(encoding='UTF-8')
        self.__signature: bytes = signature

    @property
    def message(self):
        return self.__message

    @property
    def signature(self):
        return self.__signature

    @message.setter
    def message(self, value: str):
        self.__message = value.encode(encoding='UTF-8')

    def __repr__(self):
        return (f"Message:\n {self.__message.decode(encoding='UTF-8')}\n"
                f"Signature:\n {self.__signature.decode(encoding='ASCII')}")

class Person:
    def __init__(self, name):
        self.name = name # TODO: key pair 생성 동작 추가

    def exchange_key(self, another: 'Person'):
        pass # TODO: 키 교환 동작 추가

    def send(self, recipient: 'Person', message: Package):
        recipient.receive(self, message)

    def receive(self, sender: 'Person', message: Package):
        pass # TODO: 메세지 수신 동작 추가




