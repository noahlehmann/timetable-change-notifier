# Disclaimer

Credits go to the original project 
[amazon-notification-bot](https://github.com/dbrysiuk/amazon-notification-bot) by 
[dennisbrysiuk](https://github.com/dbrysiuk/amazon-notification-bot/commits?author=dennisbrysiuk).

This project strongly relies on the parts and explanations found in the corresponding 
[blog post](https://medium.com/twodigits/create-a-web-crawler-notification-bot-6cc354a9b04c).

# Timetable Change Notifier

A python bot which checks the website of hof university and searches for timetable changes for a configured study 
program and semester.
It will email each configured account if it finds new changes.

## Gmail Account Credentials

For using the mailer clone the repository and untrack the file changes of `selenium_bot/src/gmail_config.py` by using

`git update-index --assume-unchanged selenium_bot/src/gmail_config.py`. 

This will allow you to enter credentials and stop it from being updated in git. 

**DISCLAIMER**: Use at own risk!