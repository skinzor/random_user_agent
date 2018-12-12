from enum import Enum


class SoftwareNames(Enum):
    ALERTSITE_MONITORING_BOT = 'alertsite-monitoring-bot'
    ANDROID = 'android-browser'
    AWESOMIUM = 'awesomium'
    BLACKBERRY = 'blackberry-browser'
    CATCHPOINT_ANALYSER = 'catchpoint-analyser'
    CHROME = 'chrome'
    CHROMIUM = 'chromium'
    COSMOS_CRAWLER = 'cosmos-crawler'
    DOTCOM_MONITOR_BOT = 'dotcom-monitor-bot'
    EDGE = 'edge'
    FIREFOX = 'firefox'
    FIREFOX_FOCUS = 'firefox-focus'
    GOOGLE_APP_ENGINE = 'google-app-engine-software'
    INTERNET_ARCHIVER_BOT = 'internet-archiver-bot'
    INTERNET_CHANNEL = 'internet-channel'
    INTERNET_TV = 'internet-tv-browser'
    K_MELEON = 'k-meleon'
    NETSCAPE_NAVIGATOR = 'netscape-navigator'
    NETSURF = 'netsurf'
    NOKIA = 'nokia-browser'
    OBIGO = 'obigo'
    OMNIWEB = 'omniweb'
    ONEBROWSER = 'onebrowser'
    OPERA = 'opera'
    OPERA_MINI = 'opera-mini'
    PALE_MOON = 'pale-moon'
    QUPZILLA = 'qupzilla'
    ROCKMELT = 'rockmelt'
    SKYFIRE = 'skyfire'
    SPEEDCURVE_SPEED_TESTER = 'speedcurve-speed-tester'
    UC_BROWSER = 'uc-browser'
    WEBKIT = 'webkit-based-browser'
    WEBTV = 'webtv'
    YANDEX = 'yandex-browser'
    YANDEX_SEARCH_BOT = 'yandex-search-bot'
    YODAOBOT_SEARCH_BOT = 'yodaobot-search-bot'


class OperatingSystems(Enum):
    UNIX = 'a-unix-based-os'
    ANDROID = 'android'
    BADA = 'bada'
    BEOS = 'beos'
    BLACKBERRY = 'blackberry-os'
    CHROMEOS = 'chromeos'
    FIRE_OS = 'fire-os'
    FREEBSD = 'freebsd'
    HAIKU = 'haiku'
    IOS = 'ios'
    LINUX = 'linux'
    MAC = 'mac'
    MAC_OS_X = 'mac-os-x'
    MACOS = 'macos'
    OPENBSD = 'openbsd'
    SUNOS = 'sunos'
    SYMBIAN = 'symbian'
    WEBOS = 'webos'
    WINDOWS = 'windows'
    WINDOWS_MOBILE = 'windows-mobile'
    WINDOWS_PHONE = 'windows-phone'


class SoftwareEngines(Enum):
    BLINK = 'Blink'
    GECKO = 'Gecko'
    GOANNA = 'Goanna'
    PRESTO = 'Presto'
    WEBKIT = 'WebKit'


class HardwareTypes(Enum):
    COMPUTER = 'computer'
    LARGE_SCREEN__GAME_CONSOLE = 'large-screen -> game-console'
    LARGE_SCREEN__MEDIA_PLAYER = 'large-screen -> media-player'
    LARGE_SCREEN__TV = 'large-screen -> tv'
    MOBILE = 'mobile'
    MOBILE__EBOOK_READER = 'mobile -> ebook-reader'
    MOBILE__HANDHELD_GAME = 'mobile -> handheld-game'
    MOBILE__MUSIC_PLAYER = 'mobile -> music-player'
    MOBILE__PHONE = 'mobile -> phone'
    MOBILE__TABLET = 'mobile -> tablet'
    SERVER = 'server'


class SoftwareTypes(Enum):
    APPLICATION__SOFTWARE_LIBRARY = 'application -> software-library'
    BOT__ANALYSER = 'bot -> analyser'
    BOT__CRAWLER = 'bot -> crawler'
    BOT__SITE_MONITOR = 'bot -> site-monitor'
    WEB_BROWSER = 'browser -> web-browser'


class Popularity(Enum):
    MOST_POPULAR = "very common"
    POPULAR = "common"
    AVERAGE = "average"
    UNPOPULAR = "uncommon"
