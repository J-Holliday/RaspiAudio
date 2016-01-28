# RaspiAudio - mitaka

====

## Overview

[master]
[mitaka]
[musashikoganei]->[shinkoganei]->[tama]

I should make Debug-Mode with using dummy-audio-input.
Dummy code give flow that if user input string to console of server, client got string message packet.
Instead of flow thet if user input voice of julius server, client got string message packet.

Then tama will deal with shinkoganei's problem.

## Status

I have separated yukkuri, and realized importing from other directory.

But I got points of improvement.
* I should refactoring musicPlayer.py and newsStation.py.
- I should use function without class.
- This problem is taken over to tama branch.
- After all, shinkoganei is not executable branch.

Current:
* audio and select is worked.
* news is not worked.
* confirm to work in raspi-voice, dawn-raw_input.

## Description

Mitaka has below policy.

1. Separate class from main module.
2. Define constant value to conf-file.

## Licence

https://github.com/J-Holliday/

http://icrus.org/iida/

## Author

https://github.com/J-Holliday
