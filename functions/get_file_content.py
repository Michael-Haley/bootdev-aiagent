import os

from config import MAX_CHARS


def get_file_content(working_directory: str, file_path: str) -> str:
    working_dir_abs: str = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    # Will be True or False
    valid_target_dir = (
        os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
    )

    if not valid_target_dir:
        return (
            f'Error: Cannot read "{file_path}" as it is outside the permitted '
            'working directory'
        )

    try:
        with open(target_file) as file:
            content = file.read(MAX_CHARS)
            # After reading the first MAX_CHARS...
            if file.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    except OSError:
        return "ERROR: File cannot be opened."

    return content