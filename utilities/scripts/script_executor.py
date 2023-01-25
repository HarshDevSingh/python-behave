from ._bash_script_executor_funcs import _del_temp_files


class ScriptExecutor:
    @staticmethod
    def delete_temp_files():
        _del_temp_files()