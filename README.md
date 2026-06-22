# Python for DevOps

This repository contains beginner Python practice scripts focused on the basics needed for a DevOps learning path. The examples are small, readable, and organized by day so each file can be run independently.

## Repository Structure

```text
python-for-DevOps/
`-- day1/
    |-- basic-math-float-x-int.py
    |-- hello.py
    |-- lenghtcheck.py
    |-- port-update.py
    |-- regex-match.py
    |-- regex-replace-findall-split.py
    |-- regex-search.py
    |-- spliit.py
    |-- str-concat.py
    |-- str-search.py
    |-- str-split.py
    |-- string_lowercase.py
    `-- textreplace.py
```

## What This Repo Covers

The `day1` folder introduces core Python concepts that are useful before moving into automation, scripting, cloud, and DevOps tools.

| File | Topic | What it demonstrates |
| --- | --- | --- |
| `hello.py` | Basic variables and addition | Stores two numbers and prints their sum. |
| `basic-math-float-x-int.py` | Arithmetic operations | Performs addition, subtraction, multiplication, and division with floats and integers. |
| `port-update.py` | Configuration values | Defines server settings such as server name, port, HTTPS status, and max connections, then updates values. |
| `lenghtcheck.py` | String length | Uses `len()` to count the number of characters in a string. |
| `str-concat.py` | String concatenation | Combines strings with and without spaces. |
| `str-search.py` | String search | Checks whether a word exists inside a sentence using the `in` keyword. |
| `str-split.py` | Split and strip methods | Splits text into a list and removes unwanted spaces or characters with `strip()`. |
| `spliit.py` | Splitting structured strings | Splits sentences and an AWS ARN-like string to extract specific parts. |
| `string_lowercase.py` | Case conversion | Uses `upper()` and `lower()` to change text case. |
| `textreplace.py` | String replacement | Uses `replace()` to modify part of a string and concatenate values. |
| `regex-match.py` | Regex match | Uses `re.match()` to find a pattern at the beginning of a string. |
| `regex-search.py` | Regex search | Uses `re.search()` to find a pattern anywhere in a string. |
| `regex-replace-findall-split.py` | Regex utilities | Uses `re.sub()`, `re.findall()`, and `re.split()` for replacement, matching, and splitting. |

## Requirements

- Python 3 installed on your system
- A terminal or code editor such as VS Code

No external Python packages are required. The regex examples use Python's built-in `re` module.

## How to Run

From the repository root, run any script with:

```bash
python3 day1/hello.py
```

For example:

```bash
python3 day1/port-update.py
python3 day1/str-split.py
python3 day1/regex-search.py
```

If your system uses `python` instead of `python3`, run:

```bash
python day1/hello.py
```

## Learning Path

A good order for studying the current files is:

1. Start with `hello.py` to understand variables and printing.
2. Practice number operations with `basic-math-float-x-int.py`.
3. Learn configuration-style values with `port-update.py`.
4. Study string operations using the `str-*`, `string_lowercase.py`, `textreplace.py`, and `lenghtcheck.py` files.
5. Move to regular expressions with the `regex-*` files.

## Notes

- Each script is independent and can be edited or run separately.
- Some filenames such as `lenghtcheck.py` and `spliit.py` keep the current repository naming. They may later be renamed to `lengthcheck.py` and `split.py` for cleaner spelling.
- This repo is a good base for adding future DevOps automation examples such as file handling, environment variables, JSON/YAML parsing, API calls, and shell command automation.

## Next Suggested Topics

- Reading and writing files
- Working with environment variables
- Parsing JSON and YAML
- Using command-line arguments
- Automating Linux commands with Python
- Writing reusable functions
- Creating small DevOps utility scripts
