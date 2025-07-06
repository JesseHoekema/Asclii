# ASCII Art Generator

A sleek, professional command-line tool for generating ASCII art from text or creating random ASCII patterns. Built with Python and designed for developers, artists, and anyone who loves terminal aesthetics.

## What does it do?

This tool lets you quickly convert text into beautiful ASCII art using various fonts and styles. You can also generate random ASCII patterns for decoration or inspiration. Everything runs in your terminal with a clean, modern interface.

## Features

- **Text to ASCII conversion** - Turn any text into stylized ASCII art
- **18 different fonts** - Choose from popular styles like slant, block, digital, gothic, and more
- **Random ASCII generation** - Create random patterns and decorative text
- **One-click clipboard copying** - Copy your creations instantly
- **Beautiful terminal interface** - Clean menus, progress bars, and styled panels
- **Cross-platform support** - Works on Windows, macOS, and Linux

## Installation

First, make sure you have Python 3.6+ installed. Then install the required packages:

```bash
pip install pyfiglet pyperclip rich
```

That's it!

## Usage

Just run the script:

```bash
python main.py
```

The tool will guide you through everything with its menus.

### 📦 Module Usage

You can also use it as a Python module in your projects:

```python
import [ folder name with asclii source].src.module as asclii

# Generate ASCII art from text with a specific style (font)
ascii_art = asclii.generateAscii("slant", "Hello World")
print(ascii_art)

# Generate a random ASCII art surprise
random_art = asclii.randomAscii()
print(random_art)
```

Make sure you have cloned this repo into your project folder


### Main Menu Options

1. **Generate ASCII from text** - Convert your text to ASCII art
2. **Generate random ASCII art** - Create random patterns and designs
3. **Exit** - Close the application

### Text to ASCII Workflow

1. Choose from 18 available fonts (slant, block, standard, digital, etc.)
2. Enter your text
3. Preview the generated ASCII art
4. Copy to clipboard or generate another

### Random ASCII Mode

Generates creative patterns and random text with random fonts - perfect for inspiration or decoration.

## Available Fonts

The tool includes these popular ASCII fonts:
- slant, block, standard, digital, big, small
- banner, doom, ghost, gothic, graffiti, isometric1
- larry3d, mini, script, shadow, speed, starwars

## Example Output

```
     ____  ____  ____  ____  ____  ____  ____  ____  ____  ____
    /    \/    \/    \/    \/    \/    \/    \/    \/    \/    \
   /  /\  \    /  /\  \    /  /\  \    /  /\  \    /  /\  \    /
  /  /__\  \  /  /__\  \  /  /__\  \  /  /__\  \  /  /__\  \  /
 /  ______  \/  ______  \/  ______  \/  ______  \/  ______  \/
/__/      \__\__/      \__\__/      \__\__/      \__\__/      \__\
```

## Requirements

- Python 3.6 or higher
- Terminal/Command Prompt
- Internet connection (for initial package installation)

## Dependencies

- `pyfiglet` - ASCII art text generation
- `pyperclip` - Cross-platform clipboard operations
- `rich` - Beautiful terminal formatting and UI

## Contributing

Found a bug or want to add a feature? Feel free to submit an issue or pull request. I'm always open to improvements!

## License

This project is open source and available under the MIT License.

## Credits

Built with love using:
- [pyfiglet](https://github.com/pwaller/pyfiglet) for ASCII art generation
- [rich](https://github.com/Textualize/rich) for terminal styling
- [pyperclip](https://github.com/asweigart/pyperclip) for clipboard functionality
