# IGC2CSV

_Copyright notice: This repository was forked from the original **IGC2KML** application linked [here](https://github.com/OverloadUT/IGC2CSV) and is not my - Nicolas Huber - work. Thanks for noticing._

## Modifications



---

## Documentation

Reads an IGC file (a flight log used very commonly in hang gliding and paragliding) and spits out a CSV file with the flight data.

The intention is to make it much easier to look at the flight data in a program like Microsoft Excel without having to write your own parser.

The CSV output also has a bunch of data derived from the data, allowing quick and easy access to stats like distance traveled, per-second climb rate, total distance climbed, etc. Again, the idea here is to be able to pull this data in to Excel and start graphing it immediately without the need to do a bunch of formula work to get at the interesting statistics.

### Installation
The current version of IGC2CSV is a command-line tool that requires Python (tested with 2.7.5) to run. To install, simply extract the program to any convenient directory.

### Usage
You can specify either a single IGC file, or a directory full of IGC files:

    python IGC2CSV.py /path/to/file.igc
    python IGC2CSV.py /path/to/folder/with/igc/files/

The CSV files will be output in the current working directory

DashWare supports a variety of formats natively, but IGC is not one of them. The included DashWare DataProfile works alongside the output of IGC2CSV to give you access to all of your flight data, *including True Airspeed if your variometer supports it.*