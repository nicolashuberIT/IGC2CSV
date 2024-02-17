# IGC2CSV

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

---

## Development

### Conventions

Static type annotations are used in this project. The codebase has been tested using the `pytest` module. The recent CI/CD status can be found at the top of this page. Click [here](https://github.com/nicolashuberIT/IGC2CSV/actions) for a detailed overview and unit testing logs. The code is formatted and linted in VS Code using the Black Formatter Extension and Pylint.

### Changelog

- **[1.0.0]** - Not released yet.

---

## License & Intellectual Property

Please note: This repository was forked from the original **IGC2KML** application by OverloadUT linked [here](https://github.com/OverloadUT/IGC2CSV) and is only partly Nicolas Huber's work. Thanks for noticing._

The source code of this application is licensed under the license linked [here](LICENSE.md) (MIT License).

To improve code quality and speed up workflows, tools like GitHub Copilot and ChatGPT were used. AI generated content is flagged with the following notes: 

- For documentation files: _This document { TITLE } has been written by { SOURCE } and verified by Nicolas Huber on { DATE }._
- For code snippets: _# AI content ({ SOURCE }, { DATE }), verified and adapted by Nicolas Huber._

AI tools are a powerful and valuable addition to improve the development workflow, as long as sources and contents are scientifically listed. Thus, it's valued a lot to provide proper listings. The following utilities have been used: [GitHub Copilot](https://github.com/features/copilot), [ChatGPT](https://chat.openai.com/).

In consideration of the `LICENSE.md`, the licensee, who is considered as such at the point of downloading this application, agrees to respect the terms and conditions. The licensee undertakes to show respect for OverloadUT's & Nicolas Huber's intellectual property.

Thanks for noticing! 

---

_© 2024, [Nicolas Huber](https://nicolas-huber.ch). All rights reserved._