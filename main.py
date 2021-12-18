import sys

from ints import (
    is_const_diff_ints,
    get_const_diff_ints,
    is_const_ratio_ints,
    get_const_ratio_ints,
    is_fibonacci_ints,
    get_fibonacci_ints,
    is_parabolic_ints,
    cal_parabolic_coefficients,
    get_parabolic_ints,
    get_random_ints,
)


def predict_next_ten_ints(ints):
    """Predict the next ten integers based on the given first few integers

    Note that the order of check function like `is_foo_ints` matters. A integer
    sequence could satisfy more than two of those checks. This case, the
    previous one would be chosen.
    """
    length=len(ints)
    if is_const_diff_ints(ints):
        whole = get_const_diff_ints(ints, length=length+10)
        next_ten = whole[length:]
        return next_ten
    if is_const_ratio_ints(ints):
        whole = get_const_ratio_ints(ints, length=length+10)
        next_ten = whole[length:]
        return next_ten
    if is_fibonacci_ints(ints):
        whole = get_fibonacci_ints(ints, length=length+10)
        next_ten = whole[length:]
        return next_ten
    if is_parabolic_ints(ints):
        whole = get_parabolic_ints(ints, length=length+10)
        next_ten = whole[length:]
        return next_ten
    next_ten = get_random_ints(minimum=min(ints), maximum=max(ints), length=10)
    return next_ten


def pull_ints_from_command_args():
    args = sys.argv[1:]
    if len(args) < 2:
        msg = "Please provide two or more ints separated by spaces."
        raise ValueError(msg)

    ints = []
    for arg in args:
        try:
            integer = int(arg)
        except ValueError:
            raise ValueError(f"The argument `{arg}` is not a integer.")
        else:
            ints.append(integer)
    return ints


def push_ints_into_console(ints):
    print(" ".join(str(integer) for integer in ints))


def main():
    ints = pull_ints_from_command_args()
    next_ten_ints = predict_next_ten_ints(ints)
    push_ints_into_console(next_ten_ints)


if __name__ == "__main__":
    main()
