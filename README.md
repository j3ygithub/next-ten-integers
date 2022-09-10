# next-ten-integers
Some simple code snippets about predicting the next ten integers.

# How to run it?

```python
git clone https://github.com/thejimmylin/next-ten-integers
cd next-ten-integers

python3 main.py 1 2 3
4 5 6 7 8 9 10 11 12 13
```

Try more
```python
python3 main.py 1 2 4
5 6 7 8 9 10 11 12 13 14

python3 main.py 1 2 3 5
8 13 21 34 55 89 144 233 377 610
```

Provide at least two integers, or it will complain.

```python
python3 main.py 1    
Traceback (most recent call last):
  File "main.py", line 70, in <module>
    main()
  File "main.py", line 64, in main
    ints = pull_ints_from_command_args()
  File "main.py", line 46, in pull_ints_from_command_args
    raise ValueError(msg)
ValueError: Please provide two or more ints separated by spaces
```

# Make the prediction more accurate

The file `ints.py` is the library we use now for predicting the next integers.

It provides two kinds of functions, `get_foo_integers` and `is_foo_integers`. You may want to write more of these kinds of functions to make the prediction more accurate.

Just add more of them into the function `predict_next_ten_ints` in the `main.py`
```
def predict_next_ten_ints(ints):
    ...
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
    # Add your `is_foo_ints` and `get_foo_ints` logic here!
```

See `main.py` and `ints.py` for more details.

# TODO

Support an iterable as an integer sequence input of `predict_next_ten_ints` in `main.py` and generate an iterable as well.
