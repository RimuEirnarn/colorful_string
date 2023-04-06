# Colorful String

Yes, this package only wraps strings to ansi codes.

## Installation

```sh
pip install git+https://github.com/RimuEirnarn/colorful_string.git
```

**tips**: You can install from tags/release archive source (`zip` and `tar.gz`). Useful for cases where git is not installed or available on your system.

```sh
pip install https://github.com/RimuEirnarn/colorful_string/archive/refs/tags/<version>.tar.gz
```

If you want to use the latest development (not recommended), try this:

```sh
pip install https://github.com/RimuEirnarn/colorful_string/archive/refs/heads/main.zip
```

## Usage

```python
from colorful_string import Combination, Foreground, Italic, Bold

procedure = Combination(Foreground.Red, Italic, Bold)
print(procedure("Hello, World!"))
```

Naturally, Combination is optional.

```python
from colorful_string import Foreground, Italic, Bold

text = Bold(Italic(Foreground.Red("Hello, World!")))
print(text)
```

**Note**: Combination is formerly named CallLinks. I've added an alias to Combination for backward compatibility.

The second example does the same as the first example.

New feature after `v0.1.3`:

```python
from colorful_string import Combination

procedure = Combination.from_string("fg_Red+st_Italic+st_Bold")
print(procedure('Hello, World!'))
```

## Issues

Some functionality like `true colors` may not work for non-256color terminals.

**New**: There's an issue where if you try to put the same `Combination` or assign `Combination` to another `Combination` which already has the previous `Combination` attached, it'll most likely crash. (#1)

## Contribute

You can submit your issue and pull request.