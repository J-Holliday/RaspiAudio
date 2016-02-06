# RaspiAudio - shiraitodai 

====

## Overview

[master]
[mitaka]
[musashikoganei]->[shinkoganei]->[tama]->[shiraitodai]

Shiraitodai try to make sendmail system.
And trying to do refactoring news.

!CAUTION ISSUE
I tried to use julius input mode without mic.
But that didn't cause expected achivement.
Process is thrown into SHIRAITODAI-BUF directory.

## Status

I have created sendmail system.
I have done refactoring of news.

News process management is below.

News Start:
[raspisan.py]->[newsparser.py]->[class"speaker"]->[func"playnews"]->[playnewsLoop.sh]->[call.py]->[func"playnewsSingle"]

News Stop:
[raspisan.py]->[newsparser.py]->[class"speaker"]->[func"stopnews"]->["$ pkill -f 'playnewsLoop.sh'"]

Key Point is via sh.

## Description

Mitaka has below policy.

1. Separate class from main module.
2. Define constant value to conf-file.

## Licence

https://github.com/J-Holliday/

http://icrus.org/iida/

## Author

https://github.com/J-Holliday
