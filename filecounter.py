import os
import argparse
from pathlib import Path

__author__ = "Christopher J. Blakeney"
__version__ = "0.1.0"


def count_files(detail, path, show_hidden, show_files):
    n = 0
    hidden_files = 0
    t_hidden_files = 0

    # walk through each sub-directory and file in given path
    for dirpath, dirname, filenames in os.walk(path):
        # count hidden files for each dir
        for f in filenames:
            if f[0] == ".":
                hidden_files += 1
                t_hidden_files += 1

        # if show hidden false, subtract files and dirs beginning with "." from the filenames and dirname list
        if show_hidden is False:
            for f in filenames:
                filenames = [f for f in filenames if not f[0] == "."]

        # real files and total
        c = len(filenames) - hidden_files
        n += c

        # cmd line option
        if detail:
            print(
                f"\nPATH: {dirpath}\n\n    >> {c} real files | {hidden_files} hidden | {c + hidden_files} total\n"
            )
        if show_files:
            for i in filenames:
                print(f"\n        - {i}")
        # reset hidden files for next loop
        hidden_files = 0

    print(
        f"\nTOTAL: {n} real files | {t_hidden_files} hidden | {n + t_hidden_files} total\n"
    )
    raise SystemExit(2)


def main():
    # CLI
    # create parser
    parser = argparse.ArgumentParser(
        prog="filecounter",
        description="Count the files within a directory",
        epilog="Thanks for using filecounter... Developed by Christopher Blakeney",
    )
    # add general output
    general = parser.add_argument_group("general output")
    general.add_argument("path", help="path to target directory")

    # add detailed output
    detailed = parser.add_argument_group("detailed output")
    detailed.add_argument(
        "-d",
        "--subdircount",
        action="store_true",
        default=False,
        help="list totals for each directory within path",
    )

    # add show filenames option
    parser.add_argument(
        "-f",
        "--showfilenames",
        action="store_true",
        default=False,
        help="list files within given path",
    )

    # set args and target dir to input path
    args = parser.parse_args()
    target_dir = Path(args.path)

    if not target_dir.exists():
        print("The target directory doesn't exist")
        raise SystemExit(1)

    filenames_flag = args.showfilenames
    detail_flag = args.subdircount
    show_hidden = True

    file_count = 0
    sub_dir_count = 0

    for dirpath, dirname, filenames in os.walk(target_dir):
        file_count += len(filenames)
        sub_dir_count += len(dirname)

    # deal with large numbers so output isn't infinite
    for dirpath, dirname, filenames in os.walk(target_dir):
        # if directory contains over 100 files and -f flag is selected, double check before proceeding
        if filenames_flag == True and file_count > 100:
            response = input(
                f"Directory and its children contain 100+ files, are you sure you want to list them? (y/n): "
            )
            if response in ("y", "Y", "Yes", "yes", "YES"):
                # call program function
                count_files(detail_flag, target_dir, show_hidden, filenames_flag)
                raise SystemExit(2)
            else:
                raise SystemExit(1)
        # if directory contains over 25 subdirs and -d is selected, double check before proceeding
        elif detail_flag == True and sub_dir_count > 15:
            response = input(
                f"Directory contains 15+ subdirectories, are you sure you want a detailed summary? (y/n): "
            )
            if response in ("y", "Y", "Yes", "yes", "YES"):
                # call program function
                count_files(detail_flag, target_dir, show_hidden, filenames_flag)
                raise SystemExit(2)
            else:
                raise SystemExit(1)
        elif detail_flag == False and filenames_flag == False:
            count_files(detail_flag, target_dir, show_hidden, filenames_flag)
            raise SystemExit(2)
        elif filenames_flag and file_count < 100 or detail_flag and sub_dir_count < 15:
            # count_files(detail_flag, target_dir, show_hidden, filenames_flag)
            print("Hey")


if __name__ == "__main__":
    main()
