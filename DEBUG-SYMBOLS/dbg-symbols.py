import os
import sys

def logo():
	print('██████╗░██████╗░░██████╗░░░░░░░░██████╗██╗░░░██╗███╗░░░███╗██████╗░░█████╗░██╗░░░░░░██████╗')
	print('██╔══██╗██╔══██╗██╔════╝░░░░░░░██╔════╝╚██╗░██╔╝████╗░████║██╔══██╗██╔══██╗██║░░░░░██╔════╝')
	print('██║░░██║██████╦╝██║░░██╗░█████╗╚█████╗░░╚████╔╝░██╔████╔██║██████╦╝██║░░██║██║░░░░░╚█████╗░')
	print('██║░░██║██╔══██╗██║░░╚██╗╚════╝░╚═══██╗░░╚██╔╝░░██║╚██╔╝██║██╔══██╗██║░░██║██║░░░░░░╚═══██╗')
	print('██████╔╝██████╦╝╚██████╔╝░░░░░░██████╔╝░░░██║░░░██║░╚═╝░██║██████╦╝╚█████╔╝███████╗██████╔╝')
	print('╚═════╝░╚═════╝░░╚═════╝░░░░░░░╚═════╝░░░░╚═╝░░░╚═╝░░░░░╚═╝╚═════╝░░╚════╝░╚══════╝╚═════╝░')

def Usage():
    print('rip / del / add Debug Symbols of a binary file')
    print('')
    print('-r : to rip of Debug symbols from a binary(copy the debug_symbols to a file)')
    print('-d : to delete Debug symbols from a binary')
    print('-a : to add Debug symbols to a binary')
    print('USAGE:')
    print('    Rip :- dbg-symbols.py -r binaryfile -o debug_symbols')
    print('    Del :- dbg-symbols.py -d binaryfile')
    print('    Add :- dbg-symbols.py -a binaryfile Debug_symbols_file')
    print(' ')
    print(' ')

logo()
print('')
print('dbg-symbols.py --help for usage')
print('')

if sys.argv[1] == '-r':
    os.system('objcopy --only-keep-debug ' + sys.argv[2] + ' ' + sys.argv[3])
    print('Ripped Successfully!')
elif sys.argv[1] == '-d':
    os.system('strip --strip-debug --strip-unneeded ' + sys.argv[2])
    print('Deleted Successfully!')
elif sys.argv[1] == '-a':
    os.system('objcopy --add-gnu-debuglink=' + sys.argv[3] + ' ' + sys.argv[2])
    print('Added Successfully')
elif sys.argv[1] == '--help':
	Usage()
