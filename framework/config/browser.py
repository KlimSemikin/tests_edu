from framework.constants import browsers


class BrowserConfig(object):
    # Настройки браузера
    # Поддерживаемые браузеры: "chrome", "firefox"
    # Поддерживаемые локализации: "ru", "en", "es" и т.д
    BROWSER = browsers.BROWSER_CHROME
    CHROME_VERSION = "75.0"
    FIREFOX_VERSION = "66.0"
    LOCALE = 'en'


class Grid(object):
    USE_GRID = False
    GRID_HOST = "localhost"
    GRID_PORT = "5565"
    GRID_URL = "http://{host}:{port}/wd/hub"
    # .format(host=GRID_HOST, port=GRID_PORT)
    IS_VNC_ENABLED = True
    IS_VIDEO_ENABLED = False
