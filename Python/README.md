# Python — CS50

This folder holds small Python scripts written while working through CS50's Python track. Each script is deliberately tiny — the point is the concepts, not the code.

## hello.py

A minimal "hello world" style program. It does three things:

1. **Shebang line** (`#!/usr/bin/env python3`) — tells the operating system which interpreter to use when the file is run directly. Not required on Windows, but harmless and good practice on macOS/Linux.

2. **`def main():`** — defines a function called `main`. CS50 teaches this pattern deliberately: keep all your program logic inside `main()`, and call it only from the bottom of the file. This makes the code easier to test and reuse later.

3. **`if __name__ == "__main__":`** — this is the key line. When Python runs a file, it sets a special variable called `__name__`. If the file is executed directly (e.g. `python hello.py`), `__name__` is set to `"__main__"`, so the block runs. If the file is *imported* by another script (e.g. `import hello`), `__name__` is set to the module's name instead, and the block is skipped. This lets you write code that works both as a standalone program and as a library.

### What the code inside does

- `name = "Michael"` — a simple variable assignment. Python is dynamically typed, so you don't declare the type; it figures out that `name` is a string from the value.
- `total = sum(range(1, 11))` — `range(1, 11)` generates the numbers 1 through 10 (the end value is exclusive), and `sum()` adds them up. This shows two built-in functions working together.
- `print(f"Hello, {name}! ...")` — an **f-string**. The `f` before the quote lets you embed expressions inside curly braces `{}`, which get evaluated and inserted into the text. This replaced the older `.format()` and `%` style formatting.

### How to run it

```bash
python hello.py
```

You should see: `Hello, Michael! The sum of 1 to 10 is 55.`

## Next steps

Once this feels comfortable, the natural progression in CS50's Python track is:

- **Conditionals** (`if`/`elif`/`else`) and comparison operators
- **Loops** (`for` and `while`)
- **Data structures** — lists, dictionaries, tuples, sets
- **Functions with parameters and return values**
- **File I/O** and **exceptions** (`try`/`except`)
- **Object-oriented programming** — classes and objects

Each of those builds directly on the patterns in this file.
