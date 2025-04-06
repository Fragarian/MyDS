from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

from message import Package


class Signer:
    def __init__(self, private_key: RSAPrivateKey):
        self.key: RSAPrivateKey = private_key

    def sign(self, message:str) -> Package:
        """메세지를 입력받고 메세지에 그 전자서명을 추가한 패키지를 반환하는 메서드."""
        signature = self.key.sign(
            message.encode(encoding='UTF-8'),
            padding.PSS(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )
        return Package(message, signature)


class Verifier:
    def __init__(self, public_key: RSAPublicKey):
        self.key: RSAPublicKey = public_key

    def verify(self, package: Package) -> bool:
        """메세지와 전자서명이 들어간 패키지를 받고 인증 결과를 반환하는 메서드."""
        try:
            self.key.verify(
                package.signature,
                package.message,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH,
                ),
                hashes.SHA256()
            )
            return True
        except InvalidSignature: # 예외 발생 시 인증 실패로 간주
            return False

