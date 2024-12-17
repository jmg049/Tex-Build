# LaTeX Build Tool

A command-line interface (CLI) tool for compiling LaTeX documents and managing auxiliary files. The tool simplifies the LaTeX compilation process by handling the build and cleanup in one step.

## Features

- Compile LaTeX documents using pdflatex
- Multiple options for handling auxiliary files:
  - Move them to a specified directory
  - Delete them after compilation
  - Leave them in place
- Optional automatic PDF opening after successful compilation
- Cross-platform support (Windows, macOS, Linux)

## Prerequisites

- Python 3.0 or higher
- pdflatex installed and accessible from the command line
- Operating system: Windows, macOS, or Linux

## Installation

You can install the package (after cloning) using either pip or poetry. 
To install from source:

```bash
git clone https://github.com/jmg049/Tex-Build.git
```

Using pip:

```bash
pip install /path/to/tex-build
```

Using poetry:

```bash
poetry add /path/to/tex-build
```

1. Clone the repository
2. Navigate to the project directory
3. Run `poetry install` or `pip install .`

## Usage

Basic usage:

```bash
tex-build -i your_document.tex
```

### Command-line Arguments

- `-i, --input`: Input TEX file (required)
- `-o, --output-method`: How to handle auxiliary files (optional)
  - `move`: Move auxiliary files to output directory (default)
  - `delete`: Delete auxiliary files after compilation
  - `no_op`: Leave auxiliary files in place
- `--output-dir`: Directory for auxiliary files when using 'move' method (default: `./.tex_out`)
- `--open`: Open the generated PDF after compilation (optional)

### Examples

Compile and move auxiliary files to a custom directory:

```bash
tex-build -i document.tex --output-dir ./build_files
```

Compile and delete auxiliary files:

```bash
tex-build -i document.tex -o delete
```

Compile and automatically open the PDF:

```bash
tex-build -i document.tex --open
```

## Auxiliary Files Handled

The tool manages the following LaTeX auxiliary file types:

- `.aux` - Auxiliary files
- `.log` - Log files
- `.toc` - Table of contents files
- `.blg` - BibLaTeX log files
- `.bbl` - BibLaTeX bibliography files
- `.fdb_latexmk` - Latexmk database files

## Future Improvements

- Support for additional LaTeX engines (XeLaTeX, LuaLaTeX)
- Multiple compilation passes for references and citations
- Custom configuration file support
- Handling additional auxiliary file types
- Watch mode for automatic recompilation
- BibTeX/BibLaTeX support

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
