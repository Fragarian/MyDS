from communication import Person, Attacker

# 정상인과 공격자 생성
Alice = Person('Alice')
Bob = Person('Bob')
Eve = Attacker('Bob') # 공격자는 Bob인것처럼 신원 위장

# Bob이 Alice에게 정상 패키지를 전송 -> 서명 일치
package = Bob.create_package("Transfer $100 from Alice's account (123-4567-1111-9999) to Bob's account (123-3456-2222-8888).")
Bob.send(Alice, package)

print("\nEve's tampered message and original signature:")
# 패키지를 입수한 Eve가 Bob으로 위장해서 패키지의 메세지만 변조해서 재전송 -> 서명 불일치
Eve.attack(Alice, package,
           tampered_message="Transfer $100 from Alice's account (123-4567-1111-9999) to Bob's account (123-6789-3333-7777).")

print()
# 다시 Bob이 같은 메세지를 Alice에게 전송함 -> 서명 일치
Bob.send(Alice, package)