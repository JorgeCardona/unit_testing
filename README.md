# <center> **EJEMPLO DE PRUEBAS UNITARIAS EN PYTHON CON UNITTEST Y PYTEST**</center>
# **BASIC PACKAGES**
- Virtualenv - https://pypi.org/project/virtualenv/
- Unittest
- Pytest - https://pypi.org/project/pytest/
- Coverage - https://pypi.org/project/coverage/
- pytest-cov - https://pypi.org/project/pytest-cov/
- black - https://pypi.org/project/black/
- pre-commit - https://pypi.org/project/pre-commit/

# **DOCUMENTATION - REFERENCES**
- Virtualenv - https://virtualenv.pypa.io/en/latest/user_guide.html
- Unittest - https://docs.python.org/3/library/unittest.html
- Pytest - https://docs.pytest.org/en/latest/getting-started.html
- Coverage - https://coverage.readthedocs.io/en/latest
- pytest-cov - https://pytest-cov.readthedocs.io/en/latest/index.html
- black - https://black.readthedocs.io/en/stable/
- pre-commit - https://pre-commit.com/
- emojis - https://gist.github.com/rxaviers/7360908


# **RESPOSITORY STRUCTURE**

```
UNIT_TESTING
├── .git
│   ├── branches
│   ├── COMMIT_EDITMSG
│   ├── config
│   ├── description
│   ├── HEAD
│   ├── hooks
│   │   ├── applypatch-msg.sample
│   │   ├── commit-msg.sample
│   │   ├── fsmonitor-watchman.sample
│   │   ├── post-update.sample
│   │   ├── pre-applypatch.sample
│   │   ├── pre-commit
│   │   ├── pre-commit.sample
│   │   ├── pre-merge-commit.sample
│   │   ├── prepare-commit-msg.sample
│   │   ├── pre-push.sample
│   │   ├── pre-rebase.sample
│   │   ├── pre-receive.sample
│   │   └── update.sample
│   ├── index
│   ├── info
│   │   └── exclude
│   ├── logs
│   │   ├── HEAD
│   │   └── refs
│   │       ├── heads
│   │       │   ├── feat
│   │       │   │   └── validado
│   │       │   └── main
│   │       └── remotes
│   │           └── origin
│   │               └── HEAD
│   ├── ORIG_HEAD
│   ├── packed-refs
│   └── refs
│       ├── heads
│       │   ├── feat
│       │   │   └── validado
│       │   └── main
│       ├── remotes
│       │   └── origin
│       │       └── HEAD
│       └── tags
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├──📂 operations
|  ├──🐍 addition.py
|  ├──🐍 subtraction.py
|  ├──🐍 multiplication.py
|  └──🐍 division.py
└──📂 test
   ├──🚨 test_addition.py
   ├──🔎 test_subtraction.py
   ├──🔎 test_multiplication.py
   └──🚨 test_division.py
   └──⚠️ __init__.py
```

# **PROJECT STRUCTURE**
```
👻:\python-code-for-testing
├──📂 operations
|  ├──🐍 addition.py
|  ├──🐍 subtraction.py
|  ├──🐍 multiplication.py
|  └──🐍 division.py
└──📂 test
   ├──🚨 test_addition.py
   ├──🔎 test_subtraction.py
   ├──🔎 test_multiplication.py
   └──🚨 test_division.py
   └──⚠️ __init__.py
💎 .pre-commit-config.yaml
📈 requeriment.txt
```

# **DELETE ALL __pycache__ DIRECTORIES FROM PROJECT**

```
👻:\python-code-for-testing
├──📂 operations
|  ├──⛔ 📂__pycache__
|  ├──🐍 addition.py
|  ├──🐍 subtraction.py
|  ├──🐍 multiplication.py
|  └──🐍 division.py
└──📂 test
   ├──⛔ 📂__pycache__
   ├──🚨 test_addition.py
   ├──🔎 test_subtraction.py
   ├──🔎 test_multiplication.py
   └──🚨 test_division.py
   └──⚠️ __init__.py
💎 .pre-commit-config.yaml
📈 requeriment.txt
```
# **UPGRADE PIP LOCAL ENVIRONMENT**
```
python.exe -m pip install --upgrade pip
```

# **INSTALL VIRTUALENV**
```
pip install virtualenv
```

# **CREATES VIRTUALENV**
```
virtualenv .venv
```

# **ACTIVATE VIRTUALENV**

## **WINDOWS**
```
.venv\Scripts\activate
```
## **LINUX**
```
source .venv\bin\activate
```

# **UPGRADE PIP VIRTUAL ENVIRONMENT**
```
python.exe -m pip install --upgrade pip
```

# **INSTALL DEPENDENCIES**
```
pip install -r requeriments.txt
```

# **CODE TO USE FOR TESTING**

## **addition.py**
```
def addition(x, y):



    return x + y
```

## **subtraction.py**
```
def subtraction(x, y):


    return x - y
```

## **multiplication.py**
```
def multiplication(x, y):



    return x * y
```

## **division.py**
```
def division(x, y):
    try:
        return x / y



    except ZeroDivisionError as err:
        print('Handling run-time error:', err)
```

# **UNIT TESTING FILES**

## **test_addition.py**
```
from operations.subtraction import subtraction

import pytest
import unittest

class TestPreProcessDataframe(unittest.TestCase):

    # Tests that subtraction works correctly for positive values of x and y.
    def test_happy_path_positive(self):
        assert subtraction(5, 3) == 2




    # Tests that subtraction works correctly for negative values of x and y.
    def test_happy_path_negative(self):
        assert subtraction(-5, -3) == -2




    # Tests that subtraction returns None when x or y is None.
    @unittest.expectedFailure
    def test_edge_case_none(self):
        assert subtraction(None, 3) == None
        assert subtraction(5, None) == None




    # Tests that subtraction works correctly when x is positive and y is negative.
    def test_general_behavior_positive_negative(self):
        assert subtraction(5, -3) == 8



    # Tests that subtraction works correctly when x is negative and y is positive.
    def test_general_behavior_negative_positive(self):
        assert subtraction(-5, 3) == -8

if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(TestPreProcessDataframe)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
```

## **test_subtraction.py**
```
from operations.subtraction import subtraction

import pytest
import unittest

class TestPreProcessDataframe(unittest.TestCase):

    # Tests that subtraction works correctly for positive values of x and y.
    def test_happy_path_positive(self):
        assert subtraction(5, 3) == 2





    # Tests that subtraction works correctly for negative values of x and y.
    def test_happy_path_negative(self):
        assert subtraction(-5, -3) == -2





    # Tests that subtraction returns None when x or y is None.
    @unittest.expectedFailure
    def test_edge_case_none(self):
        assert subtraction(None, 3) == None
        assert subtraction(5, None) == None





    # Tests that subtraction works correctly when x is positive and y is negative.
    def test_general_behavior_positive_negative(self):
        assert subtraction(5, -3) == 8




    # Tests that subtraction works correctly when x is negative and y is positive.
    def test_general_behavior_negative_positive(self):
        assert subtraction(-5, 3) == -8

if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(TestPreProcessDataframe)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
```

## **test_multiplication.py**
```
from operations.multiplication import multiplication

import unittest

class TestPreProcessDataframe(unittest.TestCase):

    # Tests that multiplication of two positive integers returns correct result.
    def test_happy_path_multiplication_integers(self):
        assert multiplication(2, 3) == 6





    # Tests that multiplication of zero with any integer returns zero.
    def test_edge_case_multiplication_zero(self):
        assert multiplication(0, 5) == 0




    # Tests that multiplication of two negative integers returns correct result.
    def test_edge_case_multiplication_negative(self):
        assert multiplication(-2, -3) == 6




    # Tests that multiplication of large numbers does not cause overflow.
    def test_important_multiplication_overflow(self):
        assert multiplication(999999999, 999999999) == 999999998000000001




    # Tests that multiplication of two positive floats returns correct result.
    def test_general_behavior_multiplication_floats(self):
        assert multiplication(2.5, 3.5) == 8.75




    # Tests that multiplication of a positive integer and a negative float returns correct result.
    def test_general_behavior_multiplication_mixed(self):
        assert multiplication(-2, 3.5) == -7.0

if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(TestPreProcessDataframe)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
```

## **test_division.py**
```
from operations.division import division

import unittest
class TestPreProcessDataframe(unittest.TestCase):

    # Tests that division returns the correct result for happy paths.
    def test_happy_path_division(self):
        assert division(10, 2) == 5
        assert division(100, 25) == 4





    # Tests that division raises ZeroDivisionError when dividing by zero.
    def test_edge_case_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            division(10, 0)




    # Tests that division returns the correct result when x is infinity.
    def test_edge_case_division_inf(self):
        assert division(float('inf'), 2) == float('inf')
        assert division(float('-inf'), 2) == float('-inf')





     # Tests that division handles negative numbers correctly.
    def test_general_behavior_division_negative_numbers(self):
        assert division(-10, 2) == -5
        assert division(10, -2) == -5





    # Tests that division returns NaN when x is NaN.
    def test_edge_case_division_nan(self):
        assert division(float('nan'), 2) != division(float('nan'), 3)




    # Tests that division handles rounding errors correctly.
    def test_general_behavior_division_rounding_errors(self):
        assert division(1, 3) == pytest.approx(0.3333333333, 0.0001)
        assert division(1, 7) == pytest.approx(0.1428571428, 0.0001)

if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(TestPreProcessDataframe)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
```

# **ASSERTS TYPES**
| Method                                                                                                                 | Checks                                  | Version |
| ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------- | ------- |
| [assertEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual)                           | a == b                                  | 3.x     |
| [assertNotEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotEqual)                     | a != b                                  | 3.x     |
| [assertTrue](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTrue)                             | bool(x) is True                         | 3.x     |
| [assertFalse](https://docs.python.org/3/library/unittest.html#unittest.TestCase.ssertFalse)                            | bool(x) is False                        | 3.x     |
| [assertIs](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIs)                                 | a is b                                  | 3.x     |
| [assertIsNot](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNot)                           | a is not b                              | 3.x     |
| [assertIsNone](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNone)                         | x is None                               | 3.x     |
| [assertIsNotNone](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNotNone)                   | x is not None                           | 3.x     |
| [assertIn](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIn)                                 | a in b                                  | 3.x     |
| [assertNotIn](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotIn)                           | a not in b                              | 3.x     |
| [assertIsInstance](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsInstance)                 | is instance(a,b)                        | 3.x     |
| [assertNotIsInstance](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotIsInstance)           | not is instance(a,b)                    | 3.x     |
| [assertRaises](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises)                         | fun(\*args,\*\*kwds) raises exc         | 3.x     |
| [assertRaisesRegexp](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaisesRegexp)             | fun(\*args,\*\*kwds) raises exc(regex)  | 3.x     |
| [assertAlmostEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual)               | round(a-b,7) == 0                       | 3.x     |
| [assertNotAlmostEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotAlmostEqual)         | round(a-b,7) != 0                       | 3.x     |
| [assertGreater](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertGreater)                       | a > b                                   | 3.x     |
| [assertGreaterEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertGreaterEqual)             | a >= b                                  | 3.x     |
| [assertLess](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertLess)                             | a < b                                   | 3.x     |
| [assertLessEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertLessEqual])                  | a <= b                                  | 3.x     |
| [assertRegexpMatches](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRegexpMatches)           | r.search(s)                             | 3.x     |
| [assertNotRegexpMatches](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotRegexpMatches)     | not r.search(s)                         | 3.x     |
| [assertItemsEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertItemsEqual)                 | sorted(a) == sorted(b)                  | 3.x     |
| [assertDictContainsSubset](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertDictContainsSubset) | all the key/value pairs in a exist in b | 3.x     |
| [assertMultiLineEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertMultiLineEqual)         | strings                                 | 3.x     |
| [assertSequenceEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertSequenceEqual)           | sequences                               | 3.x     |
| [assertListEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertListEqual)                   | lists                                   | 3.x     |
| [assertTupleEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTupleEqual)                 | tuples                                  | 3.x     |
| [assertSetEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertSetEqual)                     | sets or frozensets                      | 3.x     |
| [assertDictEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertDictEqual)                   | dicts                                   | 3.x     |


# **FORMATTING THE CODE**
## **PRECOMMIT**
### **CREATE THE CONFIGURATION FILE**
#### **.pre-commit-config.yaml**
```
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: debug-statements
    -   id: double-quote-string-fixer
    -   id: name-tests-test
    -   id: requirements-txt-fixer
-   repo: https://github.com/psf/black
    rev: 22.10.0
    hooks:
    -   id: black
-   repo: https://github.com/asottile/setup-cfg-fmt
    rev: v2.2.0
    hooks:
    -   id: setup-cfg-fmt
-   repo: https://github.com/asottile/reorder_python_imports
    rev: v3.9.0
    hooks:
    -   id: reorder-python-imports
        exclude: ^(pre_commit/resources/|testing/resources/python3_hooks_repo/)
        args: [--py38-plus, --add-import, 'from __future__ import annotations']
-   repo: https://github.com/asottile/add-trailing-comma
    rev: v2.4.0
    hooks:
    -   id: add-trailing-comma
        args: [--py36-plus]
-   repo: https://github.com/asottile/pyupgrade
    rev: v3.3.2
    hooks:
    -   id: pyupgrade
        args: [--py38-plus]
-   repo: https://github.com/pre-commit/mirrors-autopep8
    rev: v2.0.2
    hooks:
    -   id: autopep8
-   repo: https://github.com/PyCQA/flake8
    rev: 6.0.0
    hooks:
    -   id: flake8
-   repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.2.0
    hooks:
    -   id: mypy
        additional_dependencies: [types-all]
        exclude: ^testing/resources/
```

## **Install the git hook scripts**
```
pre-commit install
```

## **RUN PRECOMMIT**
### **ORGANIZE**
```
pre-commit run --all-files
```
### **VALIDATES**
```
pre-commit run --all-files
```

## **RUN JUST CODE FORMATING**
### **BLACK**
```
python -m black .
```

# **EVADE PRE COMMIT VALIDATION**
```
git commit . -m 'no validates commit' --no-verify
```


# **COMMANDS FOR TESTING**

## **GENERATED COVERAGE FILE**
```
python -m coverage run -m unittest
```

## **SHOW REPORT ON PROMPT**
```
python -m coverage report
```

## **GENERATED REPORT INTO HTML FILE**
```
python -m coverage html
```

## **SHOW GENERATED REPORT ON BROWSER**
```
# go to directory when index.html was generated
👻:\python-code-for-testing\htmlcov\index.html
```
Coverage report: 86%
coverage.py v6.4, created at 2023-04-30 19:02 -0500
| Module                        | statements | missing | excluded | coverage |
| ------------------------------| ---------- | ------- | -------- | -------- |
| operations\\addition.py       | 2          | 0       | 0        | 100%     |
| operations\\division.py       | 5          | 0       | 0        | 100%     |
| operations\\multiplication.py | 2          | 0       | 0        | 100%     |
| operations\\subtraction.py    | 2          | 0       | 0        | 100%     |
| test\\__init__.py             | 0          | 0       | 0        | 100%     |
| test\\test_addition.py        | 26         | 4       | 0        | 85%      |
| test\\test_division.py        | 25         | 3       | 0        | 88%      |
| test\\test_multiplication.py  | 20         | 3       | 0        | 85%      |
| test\\test_subtraction.py     | 20         | 4       | 0        | 80%      |
| Total	                        | 102	     | 14	   | 0        |	86%      |
coverage.py v6.4, created at 2023-04-30 19:02 -0500
