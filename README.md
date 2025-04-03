# Caption2MD

A simple Python tool that converts SRT subtitle files to readable Markdown documents.

## Features

- Converts SRT subtitle files to clean Markdown format
- Removes timestamps while preserving subtitle text
- Batch processes multiple SRT files in a directory
- Automatically renames files by removing "（自动生成）" (auto-generated) tags
- Creates a flag file to indicate when processing is complete

## Installation

```bash
# Clone the repository
git clone https://github.com/kirklin/caption2md.git
cd caption2md

# Install dependencies
pip install pysrt
```

## Usage

1. Place your SRT files in the `srt` directory
2. Run the script:

```bash
python main.py
```

3. The converted Markdown files will be saved in the same directory as the SRT files

## Customization

You can change the input directory by modifying the `srt_directory` variable in `main.py`:

```python
# Change to your SRT files directory
srt_directory = './your_directory'
```

## Requirements

- Python 3.10+
- pysrt

## License

MIT

## Author

[Kirk Lin](https://github.com/kirklin) 
