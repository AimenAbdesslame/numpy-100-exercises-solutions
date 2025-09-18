print(0 * np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(np.nan in set([np.nan]))
print(0.3 == 3 * 0.1)
nan
False
False
nan
True
False

1. print(0 * np.nan)

np.nan = special float meaning “Not a Number.”

Arithmetic with nan almost always produces nan.

Even though mathematically 0 × anything = 0, the IEEE-754 floating-point standard says:
0 × NaN = NaN (to preserve the fact that NaN contaminates all results).
Output: nan

2. print(np.nan == np.nan)

By definition, NaN is never equal to anything, even itself.

This is how IEEE-754 ensures NaNs don’t sneak through unnoticed.

The only safe way to check for NaN is np.isnan(x).
Output: False

3. print(np.inf > np.nan)

Comparisons involving NaN are always False (except !=, which is True).

Even though you might expect +∞ > NaN, the presence of NaN makes the result undefined.
Output: False

4. print(np.nan - np.nan)

Any arithmetic with NaN stays NaN.

“NaN minus NaN” = still not a number.
Output: nan

5. print(np.nan in set([np.nan]))

This one is subtle:

A set in Python uses hashes for membership tests.

nan is hashable (so you can store it in a set).

When checking nan in {...}, Python first compares hashes (which match), then does equality.

BUT: for NaN, equality is always False (nan == nan → False).

Python’s set.__contains__ special-cases this: if the object has the same hash and is the same object in memory, it considers it present.
→ Since np.nan is a single float object reused, it matches.
Output: True

6. print(0.3 == 3 * 0.1)

In floating-point arithmetic, 0.1 cannot be represented exactly in binary.

3 * 0.1 gives something like 0.30000000000000004.

0.3 is represented as 0.299999999999999988.

They’re very close but not exactly the same → comparison fails.
Output: False

(That’s why we use math.isclose() or np.isclose() for float comparisons.)
