from bot import Bot


def main():
    bot = Bot("https://www.hof-university.de/studierende/info-service/stundenplanaenderungen.html",
              "Master Informatik",
              "1u2 - WS 2021")
    bot.check_changes()


if __name__ == '__main__':
    main()
