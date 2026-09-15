import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    working_dir_abs: str = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

    if os.path.isdir(target_dir) == False:
        return f'Error: "{directory}" is not a directory'

    # Will be True or False
    valid_target_dir = (
        os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    )

    if valid_target_dir == False:
        return (
            f'Error: Cannot list "{directory}" as it is outside '
            "the permitted working directory"
        )

    file_info_list = []
    dir_contents: list = os.listdir(target_dir)

    for file in dir_contents:
        file_path = os.path.normpath(os.path.join(target_dir, file))
        is_dir = os.path.isdir(file_path)
        size = os.path.getsize(file_path)
        file_info_list.append(f'- {file}: file_size={size}, is_dir={is_dir}')

    return '\n'.join(file_info_list)
    
