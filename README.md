# py-sblgnt

The MorphGNT morphologically-tagged SBLGNT database has long been available as
a clonable git repository or downloadable zip / tar.gz file. However, Python
tools such as the [greek-reader](https://github.com/jtauber/greek-reader) that
make use of the MorphGNT SBLGNT typically instruct users to separately download
the data into an adjacent directory. Each tool has its own code for reading the
MorphGNT SBLGNT files.

**py-sblgnt** is designed to improve this greatly by provided a pip-installable
package that combines the database AND a Python API for accessing it.

This way, tools built on the MorphGNT SBLGNT can include **py-sblgnt** as a
requirement to be installed globally or into a virtualenv and no other set up
is necessary.
