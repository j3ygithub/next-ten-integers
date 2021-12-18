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
    if is_const_diff_ints(ints):
        diff = ints[1] - ints[0]
        return get_const_diff_ints(first=ints[-1] + diff, diff=diff)
    if is_const_ratio_ints(ints):
        ratio = int(ints[1] / ints[0])
        return get_const_ratio_ints(first=ints[-1] * ratio, ratio=ratio)
    if is_fibonacci_ints(ints):
        first = ints[-1] + ints[-2]
        second = first + ints[-1]
        return get_fibonacci_ints(first=first, second=second)
    if is_parabolic_ints(ints):
        a, b, c = cal_parabolic_coefficients(ints)
        parabolic_ints = get_parabolic_ints(a, b, c, length=len(ints) + 10)
        next_ten_ints = parabolic_ints[len(ints) :]
        return next_ten_ints
    return get_random_ints(minimum=min(ints), maximum=max(ints))


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
