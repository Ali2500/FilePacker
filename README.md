# FilePacker

Small and simple API for packing an arbitrary directory tree into a 'filepack'. The API then lets you 'read' the filepack as if it's a standard directory tree on disk without loading the entire filepack to RAM. Any file inside the filepack can still be looked up in O(1) time without having to traverse the entire filepack.

**Primary Use-case:** Efficiently iterating over large datasets with millions of files on high performance compute nodes. The filesystems on these nodes often discourage having a large number of small files.

**Requirements:** No external packages needed. Should work fine on any Python3.

## Features

:heavy_check_mark: Seamlessly pack arbitrary directory tree  
:heavy_check_mark: Concurrent processes can read from the same file pack safely  
:heavy_check_mark: Entire filepack is not in RAM  
:heavy_check_mark: Any file can be looked up in O(1) (important for deep learning training)  
:heavy_check_mark: Reader returns a file-like object that can be used by directly given to python libraries  

:x: Filepack is not editable. If you want to add/remove files you have to remake it from scratch  
:x: No file size compression   

## Generate Filepack

First add the `file_packer` directory to your `$PYTHONPATH` variable:

```bash
export PYTHONPATH=/path/to/FilePacker:$PYTHONPATH
```

**Create filepack:** Run the `main` script by pointing it to the directory you want to pack and an output path for where the filepack will be written

```bash
python file_packer/main.py -i /path/to/directory -o /path/to/output.fpack
```

**Inspect filepack:** You can inspect the contents of a filepack by running:

```bash
python file_packer/main.py -i /path/to/output.fpack
```

If you have a lot of files in your filepack and want a condensed console output, you can add the `--directories-only` argument to the above command. This will only print the directory names.

## Read Filepack in code

Only a couple of lines are code are needed to read a file from inside the filepack

```python
from file_packer import FilePackReader
from file_packer import utils as fp_utils

# Initialize a reader instance
reader = FilePackReader("/path/to/a/filepack.fpack")

# 'mode' works similar to the native python 'open' function. 'rb' means bytes and 'r' means string.
# filehandle has type BytesIO for 'rb' and StringIO for 'r'. 
# Both are so-called 'file-like' objects that most python libraries readily accept as input.
filehandle = reader.open("some/file.xyz", mode='rb')  # paths are relative to the base directory that was packed
```

The reader class implements several useful methods. Some of these are similar to functions in the native python `os` package to make it easy for you to integrate this API into existing code.

```python
# print the contents of a directory in the filepack
reader.listdir("some/dir")

# 'walk' inside the directory tree and print contents recursively
reader.walk("some/starting/dir")

# check if a file/dir exists
reader.exists("some/file/or/dir")
```







