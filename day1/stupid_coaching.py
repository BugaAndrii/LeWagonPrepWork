def coach_answer(your_message):
    """
    Provide a coach's answer based on the given message.

    Args:
        your_message (str): The message given to the coach.

    Returns:
        str: The coach's answer based on the message.
    """
    if your_message == "I am going to work right now!":
        return ""
    elif your_message[-1] == "?":
        return "Silly question, get dressed and go to work!"
    else:
        return "I don't care, get dressed and go to work!"


def coach_answer_enhanced(message):
    """
    Provide an enhanced coach's answer based on the given message.

    If the message is shouted, the coach will acknowledge the motivation before giving the regular answer.

    Args:
        message (str): The message given to the coach.

    Returns:
        str: The enhanced coach's answer based on the message.
    """
    if message == "I AM GOING TO WORK RIGHT NOW!":
        return ""
    elif message.isupper():
        return "I can feel your motivation! " + coach_answer(message)
    else:
        return coach_answer(message)


if __name__ == "__main__":
    # Test the coach_answer function
    print(coach_answer("Can I eat some pizza?"))
