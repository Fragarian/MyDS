class Signer:
    def __init__(self, private_key):
        pass # TODO: 클래스 초기화 구현

    def sign(self):
        pass # TODO: 서명 전체 기능 구현

    def encrypt(self):
        pass # TODO: 암호화 기능 구현

    def attach(self, message, signature):
        pass  # TODO: 서명 부착 기능 구현


class Verifier:
    def __init__(self, public_key):
        pass # TODO: 클래스 초기화 구현

    def verify(self):
        pass # TODO: 인증 전체 기능 구현

    def decrypt(self):
        pass # TODO: 복호화 기능 구현

    def detach(self, message):
        pass # TODO: 서명 추출 기능 구현

def generate():
    return Signer(None), Verifier(None) # TODO: 서명 모듈과 인증 모듈을 반환하는 함수 구현

