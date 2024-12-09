def is_prime(num):
    """주어진 숫자가 소수인지 확인합니다."""
    if num < 2:
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    while True:
        try:
            user_input = int(input("숫자를 입력하세요: "))
            break  # 유효한 입력이 들어오면 루프를 빠져나갑니다
        except ValueError:
            print("유효하지 않은 입력입니다. 숫자를 입력해주세요.")
    
    if is_prime(user_input):
        print(f"{user_input}는 소수입니다.")
    else:
        print(f"{user_input}는 소수가 아닙니다.")

if __name__ == "__main__":
    main()
