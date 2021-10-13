from bot import Bot

if __name__ == '__main__':
    # pass timetable-changes url in the bot constructor
    amazon_bot = Bot("https://www.hof-university.de/studierende/info-service/stundenplanaenderungen.html",
                     "Master Informatik",
                     "1u2 WS 2021")
    amazon_bot.check_product_by_name()
