import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        if os.path.isdir(directory) == False:
            return f'Error: "{directory}" is not a directory'

        working_dir_abs: str = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        # Will be True or False
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

        if valid_target_dir == False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        return f'Success: "{directory}" is within the working directory'
    except (OSError, TypeError, ValueError):
        return "Error: call to get_files_info failed"