# Remember Random

A unix-like tool to notify you of text you mark to be remembered. Useful for wikis.

Config example:

Place the config in ~/.remember_config

```sh
global.tmp_file=/tmp/remember_random_file
glossary.file_path=/home/jean/projects/wiki/src/glossary.md
glossary.separator=new_line
remember.file_path=/home/jean/.remember
remember.separator=new_line
quotes.file_path=/home/jean/projects/wiki/src/quotes.md
quotes.separator=tree_dashes
wiki.file_path=/home/jean/projects/wiki/src
wiki.separator=emphasis_blocks
```

## Binaries

1. crawler.sh - is responsible to build a table with all notifications
2. get_remember.sh - returns a message to be remembered
3. notification_gui.py - optional gui for showing the message and change it's probability of showing up again


These scripts are made to be used with a cron to adjust the
frequencies of the notifications and crawling

## Example:

```cron
CONFIG_FILE=/home/jean/.remember_config
*/30 * * * * /home/jean/projects/remember_random/crawler.sh
*/5  * * * (cd /home/jean/projects/remember_random ; ./get_remember.sh | ./notification_gui.py )
```

