from pathlib import Path
import shutil
# import sys

import folder_scanner as scan
import string_normalize


def check_new_name(folder: Path, fs_name_obj: Path) -> str:
    """
    Checks for the existence of a file in a folder 
    (after normalized if needed), and return freeing new_name(str).

        Parameters:
            folder(Path): Folder where name is checked.
            fs_name_obj(Path): Name of file|folder.

        Returns:
            A free name for file (str).
    """
    if fs_name_obj.is_dir() or not fs_name_obj.suffix:
        norm_name = fs_name_obj.name  # name w/o extension
        norm_name = string_normalize.normalize(norm_name)
        obj_candidate = folder.joinpath(norm_name)
    # elif fs_name_obj.is_file() and fs_name_obj.suffix:
    else:
        norm_name = fs_name_obj.name[:-len(fs_name_obj.suffix)]
        norm_name = string_normalize.normalize(norm_name)  # str file w/o ext
        obj_candidate = folder.joinpath(
            ''.join([norm_name, fs_name_obj.suffix]))

    new_counter = 0

    while obj_candidate.exists():
        new_counter += 1  # new number for new name
        # change number in filename, new name with number:
        norm_name = new_name(norm_name, new_counter)

        if fs_name_obj.is_file() and fs_name_obj.suffix:
            obj_candidate = folder.joinpath(
                ''.join([norm_name, fs_name_obj.suffix]))

        else:  # folder or len(fs_name_obj.suffix) == 0
            obj_candidate = folder.joinpath(norm_name)

    if fs_name_obj.is_file() and fs_name_obj.suffix:
        return ''.join([norm_name, fs_name_obj.suffix])

    else:
        return norm_name


def delete_empty_folder(folder: Path) -> None:
    """
    Delete empty folder.

        Parameters:
            folder(Path): A simple path of folder.

        Returns:
            None
    """
    try:
        folder.rmdir()

    except OSError:
        print(
            f'Can\'t delete {folder}, an error occurred. The directory must be empty.')


def freeing_name(main_directory: Path) -> None:
    """
    Freeing the reserved name for the sorting directory. 
    Existing objects(files) are renamed.

        Parameters:
            main_directory(Path): A simple path of start folder.

        Returns:
            None
    """
    for item_category in scan.file_paths_by_category:  # sort all categories
        new_counter = 0  # counter for new name if needed freeing for category name
        need_free_name = main_directory.joinpath(item_category)

        if need_free_name.is_file():
            # looking for a new name for the file
            obj_candidate = Path(str(need_free_name)+str(new_counter))
            while True:
                if obj_candidate.exists():
                    new_counter += 1  # new number for new name
                    # change number in dir-name, new name with adding number:
                    norm_name = new_name(obj_candidate.name, new_counter)
                    obj_candidate = main_directory.joinpath(norm_name)

                else:
                    break

            need_free_name.replace(obj_candidate)


def handle_archive(fullname: Path, target_folder: Path) -> None:
    """
    If not, creates a folder for archives. Unpack archive file 
    to the normalized name folder with normalized name of archive file.

        Parameters:
            fullname(Path): A full path of file.
            target_folder(Path): New destination category folder for 
                the archive folder.

        Returns:
            None
    """
    target_folder.mkdir(exist_ok=True, parents=True)
    name_without_extension = fullname.name[:fullname.name.rfind(
        scan.get_extension(fullname.name))-1]
    folder_for_file = target_folder.joinpath(name_without_extension)
    folder_for_file = target_folder.joinpath(
        check_new_name(target_folder, folder_for_file))
    folder_for_file.mkdir(exist_ok=True, parents=True)  # ()

    try:
        shutil.unpack_archive(str(fullname.resolve()),
                              str(folder_for_file.resolve()))

    except shutil.ReadError:
        print(f'The archive is damaged or it is not an archive: {fullname}!')
        folder_for_file.rmdir()

        return None
    # We delete the quasi-archive, it's junk
    fullname.unlink()


def handle_data(fullname: Path, target_folder: Path) -> None:
    """
    If not, creates a category folder. Moves the category file 
    with the normalized name to the category folder.

        Parameters:
            fullname(Path): A full path of file.
            target_folder(Path): New destination folder for the file.

        Returns:
            None
    """
    target_folder.mkdir(exist_ok=True, parents=True)
    new_name_ = check_new_name(target_folder, fullname)
    fullname.replace(target_folder.joinpath(new_name_))


def handle_other(fullname: Path) -> None:
    """
    Normalize name for unknown file (rename to normalized name).

        Parameters:
            fullname(Path): A full path of file.

        Returns:
            None
    """
    new_name_ = check_new_name(fullname.parent.resolve(), fullname)
    fullname.rename(fullname.parent.resolve().joinpath(new_name_))


def junk_sorter(folder: Path) -> None:
    """
    The main function checks the startup parameters and the presence of 
    a folder and starts the sorting process.

        Parameters:
            folder(Path): A simple path of folder.

        Returns:
            None
    """
    scan.scanning(folder)

    for category in scan.file_paths_by_category:

        if category == 'other':
            for file in scan.file_paths_by_category[category]:
                handle_other(file)

        elif category == 'archives':
            for file in scan.file_paths_by_category[category]:
                handle_archive(file, folder.joinpath(category))

        else:
            for file in scan.file_paths_by_category[category]:
                handle_data(file, folder.joinpath(category))

    # Reverse the list to delete all folders
    for folder in scan.FOLDERS[::-1]:
        delete_empty_folder(folder)


def new_name(try_new_name: str, add_cx: int) -> str:
    """
    Change number(add_cx) in filename(try_new_name).
    For examples: being "documents", new "1.documents";
        being "2.documents", new "3.documents";
        being "name.file10.txt", new "name.file11.txt".

        Parameters:
            try_new_name(str): Previous potential free name.
            add_cx(int): Counter for changing name

        Returns:
            A new potential free name. 
    """
    # for example: [1.docs], or ['name','file1','txt']:
    parts = try_new_name.split(".")

    return f'''{('.'.join(parts[:-1]))[:-len(str(add_cx-1))]}{add_cx}'''\
        f'''.{parts[len(parts)-1]}'''


def print_author():
    print(" Junk Sorter created by Denys TANTSIURA\n")


def main(*folder: str):
    # Start junk sorter. Run: python3 main.py "full folder path for sorting"
    if folder:
        # Make the path absolute
        folder_for_sorting = Path(folder).resolve()

        if folder_for_sorting.is_dir():
            print(f'Start sorting in folder: {folder_for_sorting}')
            freeing_name(folder_for_sorting)
            junk_sorter(folder_for_sorting)
            return f'All junk in folder "{folder}" sorted'

        else:
            return f'Sorry, but "{folder_for_sorting}" is NOT a folder! Bye!'

    else:
        return 'Sorry, but NO folder specified! Bye!'
        # for run with 'test' folder by default: junk_sorter(Path('D:\\test\\').resolve())


if __name__ == '__main__':
    main()
