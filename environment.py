import os
import time
from dotenv import dotenv_values
from selenium import webdriver
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from utilities.commons.exceptions import DriverSetupFailedException
from utilities.commons.context import Context
from utilities.scripts.script_executor import ScriptExecutor
import requests
from requests.exceptions import ConnectionError


def _get_env_values() -> dict:
    config = dotenv_values(".env")
    return {**config} if config else None


def _load_init_configs(context):
    env_values = _get_env_values()
    context: Context = context
    if env_values is not None:
        context.WEB_URL = env_values.get("WEB_URL")
        context.API_URL = env_values.get("API_URL")
    else:
        raise Exception(f"Env file/values are missing")


def _get_service() -> Service:
    try:
        service = Service(executable_path=ChromeDriverManager(path=os.path.dirname(__file__)).install())
    except DriverSetupFailedException:
        raise DriverSetupFailedException(msg="Failed to install driver or create service")
    return service


def _get_chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument("no-sandbox")
    options.add_argument("--verbose")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--allow-insecure-localhost")
    return options


def _get_local_webdriver():
    service: Service = _get_service()
    try:
        browser = Chrome(service=service, \
                         options=_get_chrome_options())
    except DriverSetupFailedException:
        raise DriverSetupFailedException(msg="Failed to initialize driver")
    return browser


def _build_selenium_remote_base_url(host):
    if host is None or len(host) > 1:
        return f"http://{host}:4444/"
    else:
        raise ValueError("host cannot be None or empty, please provide host")


def _get_remote_selenium_url(hosts: list) -> str:
    if len(hosts) < 1:
        raise ValueError("Please enter host(s) as list, at least one host is expected")
    retry = True
    max_retries = 5
    retry_attempt = 0
    while retry:
        retry_attempt += 1
        for host in hosts:
            try:
                selenium_remote_url = _build_selenium_remote_base_url(host)
                status_code = requests.get(selenium_remote_url).status_code
                if status_code == 200:
                    retry = False
                    return selenium_remote_url + "wd/hub"
                else:
                    print(f"request to {selenium_remote_url} failed due to status code: {status_code} ")
                    retry = False
            except ConnectionError:
                print(f"{selenium_remote_url} is not reachable \n")
                if hosts.index(host) + 1 < len(hosts):
                    print(f"now trying to reach selenium at:{_build_selenium_remote_base_url(hosts[hosts.index(host) + 1])}")
                if retry_attempt >= max_retries:
                    retry = False
                time.sleep(5)
        print(f"*** retry attempt:{retry_attempt} ***\n")


def _get_webdriver_from_remote():
    remote_selenium_url = _get_remote_selenium_url(hosts=["selenium", "localhost"])
    return webdriver.Remote(command_executor=remote_selenium_url, \
                            options=_get_chrome_options())


def before_scenario(context, scenario):
    _load_init_configs(context)
    context.browser = _get_local_webdriver() \
        if os.environ.get("RUN_ENV") == "local" \
        else _get_webdriver_from_remote()


def after_scenario(context, scenario):
    context.browser.quit()


def after_all(context):
    ScriptExecutor.delete_temp_files()


'''
#other available hooks

def before_step(context, step):
    pass


def after_step(context, step):
    pass


def before_feature(context, feature):
    pass


def after_feature(context, feature):
    pass


def before_tag(context, tag):
    pass


def after_tag(context, tag):
    pass


def before_all(context):
    pass

def after_all(context):
    pass
'''
