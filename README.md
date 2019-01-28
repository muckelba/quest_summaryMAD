# A quest summary for MAD
A summary message of scanned quests by MAD sent to Telegram

## quest_config.txt
Rename `quest_config.txt.example` to `quest_config.txt` and define your settings here. Note, that you have to leave a empty line after every section.

## Languages
There are some hardcoded strings in english in the code. Adjust them to your needs. Everything else is taken from the `text.txt` file. Define your message with it.   
The `$date` variable will display the weekday in the locale you've defined in `quest_config.txt`. That's depending on your OS.

## Crontab
To run the script every day for example at 7am: `0 7 * * * cd PATHTODIR/quest_summary/ && /usr/local/bin/python3.6 quest_summary.py` The python path can be different, depending on your OS.
