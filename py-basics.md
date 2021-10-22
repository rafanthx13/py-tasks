# Py Basics

## IF TERNÁRIO

````python
separator, op_system = ('\\','windows') if os.name == 'nt' else ('/', 'linux')
````

## USO DE FILTER,MAP,REDUCE

Requer por um `list` no final

```python
all_dirs = list(filter(lambda x: os.path.isdir(x) and x !='.ipynb_checkpoints',
                           all_directory_files_contents))
```

## TRY .. CATCH

```python
try:

except Exception as err:
```

# Snippets de manipulação de pastas

```python
def check_os_and_separator():
    """Check if is linux and windows, and retorn separator"""
    separator, op_system = ('\\','windows') if os.name == 'nt' else ('/', 'linux')
    print(op_system)
    return separator
```



```python
def get_all_folders(path='.'):
    """Get all fodelrs, exlude .ipynb_checkpoints"""
    all_directory_files_contents = os.listdir(path)
    all_dirs = list(filter(lambda x: os.path.isdir(x) and x !='.ipynb_checkpoints',
                           all_directory_files_contents))
    return all_dirs
```



```python
def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            r.append(os.path.join(root, name))
    return r
```

