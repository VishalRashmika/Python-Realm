# DEBUG-SYMBOLS
A Python tool to remove, add and extract debug symbols from a binary.

# Usage

> -r : to rip of Debug symbols from a binary(copy the debug_symbols to a file)

> -d : to delete Debug symbols from a binary

> -a : to add Debug symbols to a binary

    
- Rip :- dbg-symbols.py -r binaryfile -o debug_symbols
- Del :- dbg-symbols.py -d binaryfile
- Add :- dbg-symbols.py -a binaryfile Debug_symbols_file

```
Works only on Linux platforms
```
