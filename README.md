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

## License

Copyright (c) 2017, Jean Carlo Machado

All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice,
      this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright notice,
      this list of conditions and the following disclaimer in the documentation
      and/or other materials provided with the distribution.
    * Neither the name of RememberRandom nor the names of its contributors
      may be used to endorse or promote products derived from this software
      without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS

