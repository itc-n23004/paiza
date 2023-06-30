def run_vision_test():
    correct_answers = 0

    for i in range(5):
        test_input = input().split()
        displayed_direction = test_input[0]
        answer = test_input[1]

        if displayed_direction == answer:
            correct_answers += 1

    if correct_answers >= 3:
        print("OK")
    else:
        print("NG")


run_vision_test()
