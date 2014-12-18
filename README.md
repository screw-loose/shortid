# ShortId [![Build Status](https://secure.travis-ci.org/corpix/shortid.png)](http://travis-ci.org/corpix/shortid) [![PyPI downloads](https://pypip.in/d/shortid/badge.png)](https://pypi.python.org/pypi/shortid)

Port of the [Dylang's](https://github.com/dylang/shortid) library to Python.

ShortId creates amazingly short non-sequential url-friendly unique ids.  Perfect for url shorteners, MongoDB and Reddis ids, and any other id users might see.

 * By default 7-14 url-friendly characters: `A-Z`, `a-z`, `0-9`, `_-`
 * Non-sequential so they are not predictable.
 * Can generate any number of ids without duplicates, even millions per day.
 * Perfect for games, especially if you are concerned about cheating so you don't want an easily guessable id.
 * Apps can be restarted any number of times without any chance of repeating an id.

- - -

## Install

```shell
$ pip install shortid
```

- - -

## Usage

```python
from shortid import ShortId

sid = ShortId()
print(sid.generate()) # dsHaFGMTL2id
```

- - -

## License

(The MIT License)

Copyright (c) 2014 Dmitry Moskowski <me@corpix.ru>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
