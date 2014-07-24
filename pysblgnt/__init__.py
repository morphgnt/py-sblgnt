import os.path


def morphgnt_filename(book_num):
    """
    return the MorphGNT filename of the given book number.

    e.g. 1 will return "61-Mt-morphgnt.txt"
    """
    return "sblgnt/{}-{}-morphgnt.txt".format(
        60 + book_num, [
            None, "Mt", "Mk", "Lk", "Jn", "Ac", "Ro", "1Co", "2Co", "Ga",
            "Eph", "Php", "Col", "1Th", "2Th", "1Ti", "2Ti", "Tit", "Phm",
            "Heb", "Jas", "1Pe", "2Pe", "1Jn", "2Jn", "3Jn", "Jud", "Re"
        ][book_num]
    )


def morphgnt_rows(book_num):
    """
    yield a dict for each MorphGNT/SBLGNT row in the given book number.
    """
    filename = os.path.join(
        os.path.dirname(__file__),
        morphgnt_filename(book_num),
    )

    with open(filename) as f:
        for line in f:
            yield dict(zip(
                (
                    "bcv", "ccat-pos", "ccat-parse", "robinson",
                    "text", "word", "norm", "lemma"
                ),
                line.strip().split()
            ))
