# IGC2CSV

![Python](https://img.shields.io/badge/Python-3.9,3.10,3.11,3.12-blue)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license--intellectual-property)
![Testing](https://github.com/nicolashuberIT/IGC2CSV/actions/workflows/testing.yaml/badge.svg)
![Formatting](https://img.shields.io/badge/formatting-Black-black)
![Linting](https://img.shields.io/badge/linting-Pylint-yellow)

_Please note: This repository was forked from the original **IGC2KML** application by OverloadUT linked [here](https://github.com/OverloadUT/IGC2CSV) and is only partly Nicolas Huber's work. Thanks for noticing._

## Modifications

Modifications are listed in the source code of this python package, which can be found [here](/src/IGC2CSV_modified/IGC2CSV.py). Please note that the `IGC2CSV` class is encorporated as an external package in the `flight-analyzer` application, which can be seen [here](https://github.com/nicolashuberIT/flight-analyzer). Both the modifications as well as the unit testing of this package are meant to make sure that the output of the `IGC2CSV` utility matches the requirements of the `flight-analyzer` tool and its algorithms.

---

## Original Documentation

The original documentation can be found [here](https://github.com/OverloadUT/IGC2CSV).

---

## Development

### Conventions

Static type annotations are used in this project. The code is formatted and linted in VS Code using the Black Formatter Extension and Pylint.

### Testing

The codebase has been tested using the `pytest` module. The recent CI/CD status can be found at the top of this page. Click [here](https://github.com/nicolashuberIT/IGC2CSV/actions) for a detailed overview and unit testing logs. Windows causes problems with file permissions, which is why it's excluded from testing and not officially supported.

### Changelog

- **[1.0.0]** - Not released yet.

---

## License & Intellectual Property

_Please note: This repository was forked from the original **IGC2KML** application by OverloadUT linked [here](https://github.com/OverloadUT/IGC2CSV) and is only partly Nicolas Huber's work. Thanks for noticing._

The source code of this application is licensed under the license linked [here](LICENSE.md) (MIT License).

To improve code quality and speed up workflows, tools like GitHub Copilot and ChatGPT were used. AI generated content is flagged with the following notes: 

- For documentation files: _This document { TITLE } has been written by { SOURCE } and verified by Nicolas Huber on { DATE }._
- For code snippets: _# AI content ({ SOURCE }, { DATE }), verified and adapted by Nicolas Huber._

AI tools are a powerful and valuable addition to improve the development workflow, as long as sources and contents are scientifically listed. Thus, it's valued a lot to provide proper listings. The following utilities have been used: [GitHub Copilot](https://github.com/features/copilot), [ChatGPT](https://chat.openai.com/).

In consideration of the `LICENSE.md`, the licensee, who is considered as such at the point of downloading this application, agrees to respect the terms and conditions. The licensee undertakes to show respect for OverloadUT's & Nicolas Huber's intellectual property.

Thanks for noticing! 

---

_© 2024, [Nicolas Huber](https://nicolas-huber.ch). All rights reserved._