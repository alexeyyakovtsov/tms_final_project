import pytest
import requests
import tests.api_tests.headers as headers
import tests.api_tests.api_urls as urls
import tests.api_tests.randomaizer as randomaizer
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from json import loads, dumps
from random import randint


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default=None,
        help="browser can be: chrome or firefox",
    )


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")

    #geckodriver_path = "tms_final_project\\geckodriver.exe"
    #chromedriver_path = "d:\\Programming\\chromedriver"


    f_type = (
        "application/pdf"
        "vnd.ms-excel,"
        "application/vnd.ms-excel.addin.macroenabled.12,"
        "application/vnd.ms-excel.template.macroenabled.12,"
        "application/vnd.ms-excel.template.macapplication/vnd.ms-excel.sheet.binaryroenabled.12,"
        "application/vnd.ms-excel.sheet.macroenabled.12,"
        "application/octet-stream"
    )

    if browser == "firefox":
        options = FirefoxOptions()
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.helperApps.alwaysAsk.force", False)
        profile.set_preference("browser.download.useDownloadDir", True)
        profile.set_preference("pdfjs.disabled", True)
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", f_type)
        # driver = webdriver.Firefox(
        #     profile, executable_path=geckodriver_path, options=options
        # )

        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
        driver.maximize_window()

        yield driver
        driver.quit()

    elif browser == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-setuid-sandbox")
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # driver = webdriver.Chrome(
        #     executable_path=chromedriver_path, options=chrome_options
        # )
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        driver.maximize_window()

        yield driver
        driver.quit()

    elif browser == 'selenoid_firefox':
        capabilities = {
            "browserName": "firefox",
            "browserVersion": "",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False
            }
        }

        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities=capabilities)

        driver.maximize_window()
        yield driver
        driver.quit()

    elif browser == 'selenoid_chrome':
        capabilities = {
            "browserName": "chrome",
            "platform": "ANY", 
            "version": "",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False
            }
        }

        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities=capabilities)

        driver.maximize_window()
        yield driver
        driver.quit()


@pytest.fixture()
def auth_token():
    data = {
        "username": "admin",
        "password": "password123"
    }

    response = requests.post(
        url=urls.AUTH_CREATE_TOKEN,
        data=dumps(data),
        headers=headers.HEADERS)

    assert response.status_code == 200
    assert response.json() is not None
    return response.json()["token"]


@pytest.fixture()
def create_booking():
    random_data = randomaizer.RandomData()
    random_word = random_data.generate_word(5)

    data = {
        "firstname": random_word,
        "lastname": random_word,
        "totalprice": randint(1, 100),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": random_word
    }

    return data


@pytest.fixture()
def path_update_booking():
    random_data = randomaizer.RandomData()
    random_word = random_data.generate_word(5)

    data = {
        "firstname": random_word,
        "lastname": random_word
    }

    return data


@pytest.fixture()
def get_last_booking(auth_token):
    response_get = requests.get(
        url=urls.GET_BOOKING_IDS,
        headers=headers.HEADERS_AUTH.update({'token': auth_token})
    )

    resp_get = response_get.json()[-1]
    return resp_get['bookingid']
