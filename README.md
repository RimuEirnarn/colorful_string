# Colorful String

Yes, this package only wraps a string to some certain codes.

## Installation

```sh
pip install git+https://github.com/RimuEirnarn/colorful_string.git
```

**tips**: You can install from tags/release archive source (`zip` and `tar.gz`). This may be for a case where git is not installed.

```sh
pip install https://github.com/RimuEirnarn/colorful_string/archive/refs/tags/<version>.tar.gz
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

**Note**: Combination is formely named CallLinks, i've added alias to Combination for backward compatibility.

This (second example) does the same as the first example.

On `v0.1.3` or later, another solution was added:

```python
from colorful_string import Combination

procedure = Combination.from_string("fg_Red+st_Italic+st_Bold")
print(procedure('Hello, World!'))
```

## Issues

Some functionality like true colors might not working for non-256color terminals. Or even some styles may not work.

## Contribute

You can submit your issue and pull request and i'll try to watch that.

## License

This package is licensed in MIT.
