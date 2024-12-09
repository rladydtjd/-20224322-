def decimal_to_binary():
    decimal_number = input("10진수를 입력하세요: ")

    try:
        decimal_number = int(decimal_number)
        if decimal_number < 0:
            raise ValueError("음수는 지원되지 않습니다.")
    except ValueError as ve:
        print(f"유효하지 않은 입력입니다: {ve}")
        return

    binary_representation = bin(decimal_number)[2:]  

    print(f"{decimal_number}의 2진수 표현: {binary_representation}")

decimal_to_binary()
