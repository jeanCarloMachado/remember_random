# Remember Random

Remember random is a tool to notify you of text you mark to be
remembered. Useful for wikis.

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

crawler.sh - is responsible to build a table with all notifications
get_remember.sh - returns a message to be remembered
gui.py - optional gui for showing the message and change it's probability of showing up again


These scripts are made to be used with a cron to adjust the
frequencies of the notifications and crawling
Example:


```cron
CONFIG_FILE=/home/jean/.remember_config
*/30 * * * * /home/jean/projects/remember_random/crawler.sh
*/5 * * * *  deactivable_run  "$(/home/jean/projects/remember_random/get_remember.sh | /home/jean/projects/remember_random/gui.py )"
```
