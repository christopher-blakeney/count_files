import os

__author__ = "Christopher J. Blakeney"
__version__ = "0.1.0"
__license__ = ""


def print_to_txt(path, output):
    with open(f"{path}/directory_summary.txt", "w") as f:
        f.write(str(output))


def count_files(path, exclude_hidden=False, show_files=True):
    n = 0
    hidden_files = 0
    t_hidden_files = 0
    for dirpath, dirname, filenames in os.walk(path):
        # count hidden files for each dir
        for f in filenames:
            if f[0] == ".":
                hidden_files += 1
                t_hidden_files += 1
        # if show hidden false, subtract files and dirs beginning with "." from the filenames and dirname list
        if exclude_hidden == True:
            for f in filenames:
                filenames = [f for f in filenames if not f[0] == "."]

        c = len(filenames) - hidden_files
        n += c
        dir_output = (
            dirpath,
            "\n>> ",
            c,
            " real files | ",
            hidden_files,
            " hidden | ",
            c + hidden_files,
            "total\n",
        )

        if show_files == True:
            for i in filenames:
                print("        - ", i)
            print("\n")

        # reset hidden files for next dir in loop
        hidden_files = 0
    total_output = print(
        "\nTOTALS: ",
        n,
        " real files | ",
        t_hidden_files,
        " hidden | ",
        n + t_hidden_files,
        " total\n",
    )
    return dir_output, total_output


def main():
    # replace with path to be counted
    path = "/Users/christopher/Desktop/Peter Mac/Penny Ad Hoc/Pubs_found/Penny_pubs"
    print_to_txt(path, count_files(path))

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
