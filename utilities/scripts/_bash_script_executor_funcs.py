import os
import subprocess
from utilities.commons.script_locations import ScriptLocation
from utilities.commons.exceptions import (BashScriptExecutionFailed, BashScriptPermissionsFailed)

BASE_PATH = os.path.relpath(os.path.dirname(__file__))


def _provide_permission_to_script(path, script_file_name):
    print(path, script_file_name)
    try:
        subprocess.run(
            f"chmod 777 {path}/{script_file_name}",
            shell=True)
    except Exception:
        raise BashScriptPermissionsFailed(
            f"failed to provide permissions to {BASE_PATH + ScriptLocation.GENERAL_SCRIPTS_DIR}/{script_file_name}")


def _del_temp_files():
    script_file_name = "delete_tmp_files.sh"
    script_location = BASE_PATH + ScriptLocation.GENERAL_SCRIPTS_DIR
    for attempt in range(0, 5):
        try:
            subprocess.run(
                f"{script_location}/{script_file_name}",
                shell=True)
            break
        except Exception:
            _provide_permission_to_script(script_location, script_file_name)
            print(f"to delete files,retrying attempt {attempt}")
            raise BashScriptExecutionFailed(
                f"failed to execute {ScriptLocation.GENERAL_SCRIPTS_DIR}/{script_file_name}")