#!/bin/bash
# email
echo 'I will always be here for PLD' > tmp.txt | curl -s --url $1 --mail-from 'hr@holbertonschool.com' --mail-rcpt 'hr@holbertonschool.com' --upload-file tmp.txt
