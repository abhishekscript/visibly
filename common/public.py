
import random
import string

# using random.choices()
# generating random strings
def get_random_word_of_length_N(word_length: int) -> str:
    return ''.join(
        random.choices(string.ascii_letters + string.digits, k=word_length)
    )


def get_random_word_of_varying_length(low: int, high: int) -> str:
    k = random.randint(low, high)
    return ''.join(
        random.choices(string.ascii_letters + string.digits, k=k)
    )


def get_random_lower_case_word_of_varying_length(low: int, high: int) -> str:
    k = random.randint(low, high)
    return random.choice(string.ascii_lowercase) + ''.join(
        random.choices(string.ascii_lowercase + string.digits, k=k)
    )
