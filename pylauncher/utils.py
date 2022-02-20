from typing import Optional


def confirm(question: str, default: Optional[str] = "yes") -> bool:
    """Confirms some user interaction

    Asks a confirmation question and returns True or False
    based on whether they answered yes or no.

    Args:
        question: The prompt to use.
        default: The default option, defaults to "yes".

    Returns:
        A boolean indicating whether the user answered yes or no.
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
