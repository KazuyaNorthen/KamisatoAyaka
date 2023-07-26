class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 27776767
    API_HASH = "e7b0d8f7b037df9ff8b300816e90080b"

    CASH_API_KEY = "JG8MXDJVLPQCIP84"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://cpdrwphc:LXuKxTftoPMnZ575JTP479F9Sf7f8XXg@tyke.db.elephantsql.com/cpdrwphc"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001960654405)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = ""  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/40eb1ed850cdea274693e.jpg"

    SUPPORT_CHAT = "PegasusFederation2"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = ""  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = ""  # Get this value from https://timezonedb.com/api

    OWNER_ID = 6044333279  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
