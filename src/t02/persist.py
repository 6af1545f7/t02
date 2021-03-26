"""
This is an example of using persistence.
"""

__author__ = "6af1545f7"
__copyright__ = "6af1545f7"
__license__ = "mit"

"""
flat files: open/close,
text 'r' or 'w';
binary 'rb'  or 'wb' - bytes.decode() str.encode()
read, readline, readlines ; ditto for write
seek, flushfileno
"""


def flatFile() :
    """
    Example of writing to and reading from asci flat files:
    - open() in read, write and read/write modes;
    - close() and implicit closing;
    - realine(s)(), and seek() to truncate reading.
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


if __name__ == '__main__' :
    file = open('tests/data.txt', 'w')
    file.write('Hello file world!\n')
    file.write('Bye   file world.\n')
    file.close()

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
    r = {'flatFile' : flatFile()}
    return r
