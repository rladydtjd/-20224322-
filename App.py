def decimal_to_binary():
    # 사용자로부터 10진수 입력 받기
    decimal_number = input("10진수를 입력하세요: ")

    # 입력값 검증
    try:
        decimal_number = int(decimal_number)
        if decimal_number < 0:
            raise ValueError("음수는 지원되지 않습니다.")
    except ValueError as ve:
        print(f"유효하지 않은 입력입니다: {ve}")
        return

    # 2진수로 변환 (내장 함수 사용)
    binary_representation = bin(decimal_number)[2:]  # '0b' 접두사 제거

    # 변환 결과 출력
    print(f"{decimal_number}의 2진수 표현: {binary_representation}")

# 함수 실행
decimal_to_binary()
