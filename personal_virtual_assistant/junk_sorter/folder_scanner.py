import sys
from pathlib import Path

from junk_sorter.extensions import DATABASE_OF_EXTENSIONS
from junk_sorter import string_normalize

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()
# create empty lists for each file category
file_paths_by_category = {i: [] for i in DATABASE_OF_EXTENSIONS}
file_paths_by_category['other'] = []


def get_extension(filename: str) -> str:
    # Return the file extension (str input, return str).
    return Path(filename).suffix[1:]


def file_operations(folder: Path, filename: str) -> bool:
    """
    Determines whether the file type is known and saves the file path.

        Parameters:
            folder(Path): A simple path of folder where is file.
            filename(str): A file name with extension.

        Returns:
            True or False (bool): Successful file type recognition marker.
    """
    extension = get_extension(filename)
    fullpath = folder.joinpath(filename)  # full path to the file

    if not extension:  # if the file has no extension add to unknown
        file_paths_by_category['other'].append(fullpath)

    else:
        for category_ in DATABASE_OF_EXTENSIONS:
            if extension.lower() in DATABASE_OF_EXTENSIONS[category_]:
                EXTENSIONS.add(extension)
                file_paths_by_category[category_].append(fullpath)

                return True

        UNKNOWN.add(extension)
        file_paths_by_category['other'].append(fullpath)

    return False


def scanning(folder: Path) -> None:
    """
    Recursively scans the contents of folders and sub-folders,
    normalizing them and filling the file lists.

        Parameters:
            folder(Path): A simple path of folder.

        Returns:
            None
    """
    for item in folder.iterdir():
        # If the current element is a folder, then we normalize its name,
        # add it to the FOLDERS list and check the next element
        # (after scanning this new folder).
        if item.is_dir():
            # We check that the folder is not a category folder.
            if item.name not in file_paths_by_category:
                item = item.rename(item.parent.resolve().joinpath(
                    f'{string_normalize.normalize(item.name)}'))
                FOLDERS.append(item)
                scanning(item)

            continue

        # Working with a file if the element is not a folder
        file_operations(folder, item.name)


if __name__ == '__main__':
    # start scanner
    if len(sys.argv) == 2:
        # Make the path absolute
        folder_for_scan = Path(sys.argv[1]).resolve()

        if folder_for_scan.is_dir():
            print(f'Start scanning in folder: {folder_for_scan}')
            scanning(Path(folder_for_scan))

            for category, file_paths in file_paths_by_category.items():
                for file in file_paths:
                    print(f'"{category}": {file.name}')

            print(f'\nTypes of files in folder: {EXTENSIONS}\n')
            print(f'Unknown files of types: {UNKNOWN}\n')
            print(FOLDERS[::-1])

        else:
            print(f'Sorry, but "{folder_for_scan}" is NOT a folder! Bye!')

    else:
        print('Sorry, but NO folder specified! Bye!')
