from selenium.common.exceptions import WebDriverException


class DriverSetupFailedException(WebDriverException):
    pass

class BashScriptExecutionFailed(BaseException):
    pass

class BashScriptPermissionsFailed(BaseException):
    pass