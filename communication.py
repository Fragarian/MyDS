"""
통신에 사용되는 메세지+전자서명 조합과
통신을 주고받는 인물을 추상화한 클래스들.
"""
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey

from digital_signature import Signer, Verifier
from message import Package

class Person:
    """메세지를 송수신하는 인물 객체를 추상화한 클래스."""
    def __init__(self, name):
        self.name = name
        self.__private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        self.__signer = Signer(self.__private_key)
        self.public_key = self.__private_key.public_key()
        self.keyring = dict()

    def add_key(self, name: str, key: RSAPublicKey) -> None:
        """keyring에 key를 추가하는 메서드. key의 구분자는 Person:name"""
        self.keyring[name] = key

    def create_package(self, message: str) -> Package:
        """메세지에 전자서명을 추가해서 패키지를 생성하는 메서드."""
        return self.__signer.sign(message)

    def send(self, recipient: 'Person', package: Package) -> None:
        """메세지를 송신하는 메서드."""
        
        # 만약 아직 키 교환을 하지 않았을 경우 일단 키 교환부터 수행 (이름을 기준으로, 이름이 아직 등록되지 않았다면 그 이름으로 키 등록)
        if self.name not in recipient.keyring:
            recipient.add_key(self.name, self.public_key)

        # 패키지 출력
        print(f"{self.name} sent a message to {recipient.name}:")
        print(package)

        recipient.receive(self, package)

    def receive(self, sender: 'Person', package: Package) -> None:
        """메세지를 수신하는 메서드."""
        print(f"Verifying the original message and signature(by public key of {sender.name}):")

        # 미리 상호 교환한 public key로 서명을 인증하고 인증 결과 출력
        if Verifier(self.keyring[sender.name]).verify(package):
            print("Signature is valid.")
        else:
            print("Signature is invalid.")


class Attacker(Person):
    """공격자(Eve)를 추상화한 클래스."""
    def attack(self, recipient: 'Person', original_package: Package, tampered_message: str) -> None:
        """원본 패키지의 메세지를 변조해서 공격 대상자에게 위조된 메세지를 보내는 메서드."""
        tampered_package = Package(tampered_message, original_package.signature)
        self.send(recipient, tampered_package) # 메세지만 변조해서 재전송



