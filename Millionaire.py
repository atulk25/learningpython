import sys

def count_questions():
    """
    Returns the number of questions required to win million dollars
    :return:
    """
    question_count = 1
    question_earning = 0.01
    total_earnings = 0.0
    while True:
        if total_earnings > 1000000.0:
            break

        total_earnings += question_earning

        print("{:2d} {:6.2f} {:6.2f}".format(question_count, question_earning, total_earnings))

        question_earning *= 2
        question_count += 1

    return question_count



