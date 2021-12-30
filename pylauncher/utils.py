from typing import Optional


def confirm(question: str, default: Optional[str] = "yes") -> bool:
    """
    Asks a confirmation question and returns True or False whether they answered yes or no

    :param question: The question to display to the user
    :param default: The default option to use if the user hits enter
    :return: True if answer is yes, False if answer is no
    """
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}

    if default is None:
        prompt = "[y/n]"
    elif default == "yes":
        prompt = "[Y/n] "
    elif default == "no":
        prompt = "[y/N] "
    else:
        raise ValueError("Invalid default")

    while True:
        answer = input(f"{question} {prompt}").lower()

        if default is not None and answer == "":
            return valid[default]
        elif answer in valid:
            return valid[answer]
        else:
            print("Invalid response, respond with 'yes' or 'no' (or 'y' or 'n')")
