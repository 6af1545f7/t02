"""
This is an example of using persistence.
"""

__author__ = "6af1545f7"
__copyright__ = "6af1545f7"
__license__ = "mit"

import struct

"""
flat files: open/close,
text 'r' or 'w';
binary 'rb'  or 'wb' - bytes.decode() str.encode()
read, readline, readlines ; ditto for write
seek, flushfileno
"""


def flatFile() :
    """
    Demonstrates writing to and reading from asci flat files:
    - open() in read, write and read/write modes;
    - close() and implicit closing;
    - realine(s)(), and seek() to truncate reading.

    Returns:
      dict: r of all strings read from file.
    """
    fn = 'tests/data.txt'
    file = open(fn, 'w')
    file.write('Hello file world!\n')
    file.write('Bye   file world.\n')
    file.close()

    open('tests/data.txt', 'a').write('Append file world!\n')

    with open(fn, 'r') as file:
        lns = file.readlines()

    file = open(fn, 'r+')
    ln1 = file.readline()
    ln2 = file.readline()
    ln2 = file.readline()
    file.seek(0)
    ln3 = file.readline(8)
    file.write('Overwrite file world!\n')
    file.close()

    with open(fn, 'r') as file:
        lns2 = file.readlines()

    r = {'lines' : lns, 'line1' : ln1, 'line3' : ln2, 'part' : ln3,
         'after' : lns2}
    return r


def binFile() :
    """
    Demonstrates writing to and reading from binary flat files:
    - Write in ascii and binary;
    - decode() to various representations;
    - en/decode using structpack() and unpack();
    - Read as binary with implicit and explicit translation.

    Returns:
      dict: r of all binary data read from file.
    """
    fn = 'tests/data.txt'
    bfn = 'tests/data.bin'
    b1 = open(fn, 'rb').read()
    print(open(fn, 'rb').read())

    open(bfn, 'wb').write(b'Spam\n')

    d = 'Sp\xe4m\n'
    """
    Ascii cannot represent binary, so throws and exception for:
    d.encode('ascii')
    """

    open(bfn, 'w', encoding='latin1').write(d)
    b2 = open(bfn, 'r', encoding='latin1').read()
    b3 = open(bfn, 'rb').read()

    ds = struct.pack('>i4shf', 2, b'spam', 3, 1.234)
    f = open(bfn, 'wb')
    f.write(ds)
    f.close()
    f = open(bfn, 'rb')
    ds = f.read()
    vs = struct.unpack('>i4shf', ds)
    f.close()

    r = {'binAscii' : b1, 'binFile' : open(bfn, 'rb').read(),
         'latin1' : b2, 'binlatin1' : b3,
         'encode' : {'latin1' : d.encode('latin1'),
                     'utf8' : d.encode('utf8'),
                     'utf16' : d.encode('utf16'),
                     'cp500' : d.encode("cp500")},
         'struct' : vs}
    return r


if __name__ == '__main__' :
    fn = 'tests/data.txt'
    bfn = 'tests/data.bin'
    b = open(fn, 'rb').read()
    print(open(fn, 'rb').read())

    open(bfn, 'wb').write(b'Spam\n')
    b = open(bfn, 'rb').read()
    print(open(bfn, 'rb').read())

    bf = open(fn, 'rb')

    file = open('tests/data.txt', 'r')
    for line in file.readlines() :
        print(line, end="")
        file.close()

    open('tests/data.txt', 'w').write('Overwrite file world!\n')

    with open('tests/data.txt', 'r') as myfile:
        lines = myfile.readlines()
        print(lines)
        for line in lines:
            print(line, end='')


def persistTest() :
    r = {'flatFile' : flatFile(), 'binFile' : binFile()}
    return r
