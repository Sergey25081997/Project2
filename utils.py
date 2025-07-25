def get_user_choice(choices: set[int]) -> int:
    while True:
        try:
            user_input = int(input().strip())
            if user_input not in choices:
                raise ValueError
        except ValueError:
            print("Это не пункт меню! Попробуйте еще раз.")
        else:
            return user_input
