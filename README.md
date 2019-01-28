# A quest summary for MAD
A summary message of scanned quests by MAD sent to Telegram

## config.ini
Rename `config.ini.example` to `config.ini` and define your settings here. Use the [PokeAlarm](https://github.com/PokeAlarm/PokeAlarm) Wiki if you dont know hot to get an Token or a Chat_ID: https://pa.readthedocs.io/en/master/configuration/alarms/telegram.html#how-to-get-a-telegram-api-key 

## Languages
There are some hardcoded strings in english in the code. Adjust them to your needs. Everything else is taken from the `text.txt` file. Define your message with it.   
The `$date` variable will display the weekday in the locale you've defined in `config.ini`. That's depending on your OS.

## Crontab
To run the script every day for example at 7am: `0 7 * * * cd PATHTODIR/quest_summary/ && /usr/local/bin/python3.6 quest_summary.py` The python path can be different, depending on your OS.
