import re, string


def is_strong_pass(
    passwd: str, 
    chars: int = 10, 
    lowers: int = 3, 
    uppers: int = 1, 
    digits: int = 1
    ):

    is_strong = re.search(
        (
            "(?=^.{%i,}$)"
            "(?=.*[a-z]{%i,})"
            "(?=.*[A-Z]{%i})"
            "(?=.*[0-9]{%i,})"
            "(?=.*[%s}]+)"
        ) % 
        (
            chars, lowers, uppers,
            digits, re.escape(string.punctuation)
        ),
        passwd
    )

    return True if is_strong else False


print(is_strong_pass("Your pass"))

