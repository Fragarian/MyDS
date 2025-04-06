import base64

class Package:
    """메세지(문자열)과 그 메세지의 전자서명을 합친 패키지를 추상화한 클래스.
    getter와 setter를 설정하여 편의와 보안을 향상했다.
    편의를 위해 message 설정 시 문자열만 입력해도 UTF-8 인코딩된 bytes 객체로 저장되고,
    보안을 위해 signatrue는 읽기만 가능하다."""
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

    def copy(self) -> 'Package':
        """깊은 복사 메서드."""
        return Package(self.__message.decode(encoding='UTF-8'), self.__signature)

    def __repr__(self):
        """패키지 출력 시 정돈된 출력이 나오도록 하는 메서드 오버라이드."""
        return (f"Message:\n {self.__message.decode(encoding='UTF-8')}\n"
                f"Signature:\n {base64.b64encode(self.__signature).decode(encoding='UTF-8')}")