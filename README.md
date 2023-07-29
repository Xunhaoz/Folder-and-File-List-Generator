# Folder and File List Generator

A Python script that generates a hierarchical list of folders and files within a specified directory, excluding items
listed in the .gitignore file and the script file itself.

## How to Use

1. Clone the repository to your local machine.
2. Make sure you have Python installed.
3. Navigate to the project directory in the terminal.

## Usage

```shell
python folder_file_list.py
```

## Output

The script will generate a file named "structure.md" in the project directory, containing the folder and file list in a
hierarchical format.

```
├── README.md
├── test
|	├── test_1
|	|	├── test_1_1
|	|	|	├── 123.py
|	|	|	├── 456.py
|	|	|	├── 789.py
|	|	|	└── __init__.py
|	|	└── __init__.py
|	└── __init__.py
├── test1
|	├── test1_1
|	└── test1_2
└── test2
	└── 123.py
```

## Configuration

By default, the script will not display debugging information. If you want to see the output as the script processes,
set the `debug` parameter to True when creating the Lister object.

```python
lister = Lister(debug=True)
```

## .gitignore

The script takes into account the .gitignore file present in the project directory, excluding the listed folders and
files from the generated structure.

## License

This project is licensed under the MIT License.