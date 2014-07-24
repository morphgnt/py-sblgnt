# py-sblgnt

The MorphGNT morphologically-tagged SBLGNT database has long been available as
a clonable git repository or downloadable zip / tar.gz file. However, Python
tools such as the [greek-reader](https://github.com/jtauber/greek-reader) that
make use of the MorphGNT SBLGNT typically instruct users to separately download
the data into an adjacent directory. Each tool has its own code for reading the
MorphGNT SBLGNT files.

**py-sblgnt** is designed to improve this greatly by providing a pip-installable
package that combines the database AND a Python API for accessing it.

This way, tools built on the MorphGNT SBLGNT can include **py-sblgnt** as a
requirement to be installed globally or into a virtualenv and no other set up
is necessary.

Note that, even though this repo and package contain the MorphGNT SBLGNT
database, the [morphgnt/sblgnt repo](https://github.com/morphgnt/sblgnt)
remains the authoritative source of the data.


## How to Use

Firstly, install with

```
pip install py-sblgnt
```

Then in your code...

```
from pysblgnt import morphgnt_rows

for row in morphgnt_rows(book_num):
    ...
```

where `book_num` is 1–27.

Each `row` will be a dictionary with the keys:

```
"bcv", "ccat-pos", "ccat-parse", "robinson", "text", "word", "norm", "lemma"
```

## License

The SBLGNT text itself is subject to the [SBLGNT EULA](http://sblgnt.com/license/)
and the morphological parsing and lemmatization is made available under a
[CC-BY-SA License](http://creativecommons.org/licenses/by-sa/3.0/).

All code is made available under an MIT License.
