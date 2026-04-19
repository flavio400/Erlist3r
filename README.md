# erList3r

**Targeted Wordlist Generator for Brute-Force & Security Testing**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Version](https://img.shields.io/badge/Version-2026-orange?style=flat-square)
![Last Updated](https://img.shields.io/badge/Last%20Updated-April%202026-yellow?style=flat-square)

A powerful **targeted password list generator** designed for penetration testers, red teamers, and security researchers.

erList3r combines personal information (names, dates, numbers, etc.) with advanced mutation techniques such as leet speak, multiple combinations, separators, and common number patterns to create highly effective and realistic wordlists.

---

## Features

- Interactive mode with guided input
- Advanced **Leet Speak** generation
- Smart combinations: name + date + number (all possible orders)
- Support for separators (`_`, `-`, `.`, space)
- Optional integration with **RockYou top 200** passwords
- Ultra mode for more aggressive generation
- Automatic duplicate removal
- Timestamped output files
- Colorful and user-friendly terminal interface

---

## Usage Examples

```bash
# Basic interactive mode
python erlist3r.py -i

# Interactive mode + RockYou top 200
python erlist3r.py -i -r
