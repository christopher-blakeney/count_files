import os

__author__ = "Christopher J. Blakeney"
__version__ = "0.1.0"
__license__ = ""


def count_files(path, excl_dirpath, show_hidden=False):
    n = 0
    hid = 0
    for dirpath, dirname, filenames in os.walk(path):
        # if show hidden false, subtract files beginning with "." from c
        if show_hidden == False:
            for f in filenames:
                filenames = [f for f in filenames if not f[0] == "."]
                dirname[:] = [d for d in dirname if not d[0] == "."]
            c = len(filenames)
        # if show hidden true, c is length of files
        else:
            c = len(filenames)
        # if dirpath is excluded, add excluded flag and minus from total
        if dirpath in excl_dirpath:
            n = n - c + hid
            print(
                dirpath,
                "\n>> [EXCLUDED] ",
                c,
                " files present | ",
                hid,
                " hidden | ",
                c + hid,
                " total\n",
            )
        else:
            n += c
            print(
                dirpath,
                "\n>> ",
                c,
                " files present | ",
                hid,
                " hidden | ",
                c + hid,
                "total" "\n                ",
            )
    print(n, " files in path", hid, " hidden files")


def main():
    # replace with path to be counted
    path = "/Users/christopher/Desktop/Peter Mac/Penny Ad Hoc/Pubs_found/Penny_pubs"
    count_files(
        path,
        # replace with paths to be excluded from total counts
        excl_dirpath=[
            "/Users/christopher/Desktop/Peter Mac/Penny Ad Hoc/Pubs_found/Penny_pubs/removed"
        ],
    )

    """
    usage = '\nReturn summary count of given directory.\nUsage: count_files.py [path]\n'
    if len(sys.argv) != 2:
        print(usage)
    elif not os.path.isdir(sys.argv[1]):
        print('\nInvalid path!\n')
    else:
        path = sys.argv[1]
        count_files(path)
    """


if __name__ == "__main__":
    # This is executed when run from the command line
    main()
