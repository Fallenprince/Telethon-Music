import os

class Config(object):
    API_ID = int(os.environ.get("20710361"))
    API_HASH = os.environ.get("015239d491a1d99b8e1eb4fb49c6bf76)
    BOT_TOKEN = os.environ.get("6532915174:AAHAU2C1Xu4XdeV6xgvZCH8o_RxKfIng-OI", None)
    STRING_SESSION = os.environ.get("1BVtsOJEBu734qSLYKqN8bwZxG02DedE91fEusYKhAOuURJg33IT53CW4KTmQ9Hi8LF5XiKrPSTSri3akLUKM6HMR0Yv5QS1n61GORyQzFpHyGK51GAMLwVZSuIrHHBl7HUYytEIqUZRIIBwpBuE-09S8chSvfaPY-CTLF0BuwoTCTqY6dW-nXG2DaS2VpcfkdBHzIn458Glp7QtozWOeLLkqSXxbAYSmHoYu44ew7SsacGVKLf82hmOi2Dc4ZAcUDJJH17fEUfM9BZBDG_Wvet8YaQKDwcyPK93kTelJZYNUymD_zzELxvawckaDepJz3P-EMAH_CRPwX5pu-4WldasOHh-cTvE=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "https://t.me/fallen_prince) # Your Support
    CHANNEL = os.environ.get("CHANNEL", "https://t.me/nighthunters108) # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
