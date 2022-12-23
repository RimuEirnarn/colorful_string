# Colorful Text

Yes, this package only wraps a string to some certain codes.

## Installation

```sh
git clone https://github.com/RimuEirnarn/colorful_text
```

## Usage

```python
from colorful_text import CallLinks, Foreground, Italic, Bold

procedure = CallLinks(Foreground.Red, Italic, Bold)
print(procedure("Hello, World!"))
```

Naturally, CallLinks is optional.

```python
from colorful_text import Foreground, Italic, Bold

text = Bold(Italic(Foreground.Red("Hello, World!")))
print(text)
```

does the same as the first example.

## Issues

Some functionality like true colors might not working for non-256color terminals. Or even some styles may not work.

## Contribute

You can submit your issue and pull request and i'll try to watch that.

## License

This package is licensed in MIT.
