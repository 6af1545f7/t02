"""
This is an example of using persistence.
"""

__author__ = "6af1545f7"
__copyright__ = "6af1545f7"
__license__ = "mit"

import struct
import dbm
import pickle
import shelve

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
    fn = 'tests/data/data.txt'
    file = open(fn, 'w')
    file.write('Hello file world!\n')
    file.write('Bye   file world.\n')
    file.close()

    open('tests/data/data.txt', 'a').write('Append file world!\n')

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
    fn = 'tests/data/data.txt'
    bfn = 'tests/data/data.bin'
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


def raFile() :
    """
    Demonstrates random access to binary flat files.

    Returns:
      dict: r.
    """
    recs = [bytes([char] * 8) for char in b'spam']
    bfn = 'tests/data/ra.bin'
    f = open(bfn, 'w+b')
    for rec in recs :
        s = f.write(rec)
    f.flush()
    pos = f.seek(0)
    d1 = f.read()
    f.close()
    f = open(bfn, 'r+b')
    d2 = f.read()
    rec = b'X' * 8
    f.seek(0)
    f.write(rec)
    f.seek(len(rec) * 2)
    f.write(b'Y' * 8)
    f.seek(8)
    d3 = f.read(len(rec))
    f.seek(0)
    d4 = f.read()
    r = {'ra1' : d1, 'size' : s, 'pos' : pos, 'ra2' : d2,
         'rec3' : d3, 'ra3' : d4}
    return r


def dbmFile() :
    """
    Demonstrates DBM files, which store as binary objects:
    - CRUD by key;
    - checking whether record with key exists;
    - getting keys.

    Returns:
      dict: r.
    """
    dbmf = 'tests/data/dbm'
    f = dbm.open(dbmf, 'c')
    f['Batman'] = 'Pow!'
    f.keys()
    r1 = f['Batman']
    who = ['Robin', 'Cat-woman', 'Joker']
    what = ['Bang!', 'Splat!', 'Wham!']
    for i in range(len(who)) :
        f[who[i]] = what[i]
    f.keys()
    ks1 = f.keys()
    r2 = {'len' : len(f), 'found' : 'Robin' in f,
          'Joker' : f['Joker']}
    f['Batman'] = 'Ka-Boom!'
    del f['Robin']
    ks2 = f.keys()
    f.close()
    r = {'r1' : r1, 'keys' : ks1, 'r2' : r2, 'keys-after' : ks2}
    return r


def pklFile() :
    """
    Demonstrates pickle file, which serialises objects:
    - Create and read binary.
    - Object returned is '==' not 'is'.

    Returns:
      dict: r.
    """
    pklf = 'tests/data/pkl.bin'
    o = {'a' : [1, 2, 3],
         'b' : ['spam', 'eggs'],
         'c' : {'name' : 'bob'}}
    f = open(pklf, 'wb')
    P = pickle.Pickler(f)
    P.dump('1234')
    pickle.dump(o, f)
    f.close()
    f = open(pklf, 'rb')
    U = pickle.Unpickler(f)
    o1 = U.load()
    o2 = pickle.load(f)
    f.close()

    r = {'p1' : o1, 'p2' : o2, '==' : o == o2, 'is' : o is o2}
    return r


def slvFile() :
    """
    Demonstrates shelf file, which serialises an object and stores it
    under a key.
    See also OODB, which may be better for storing class objects, and has more
    sophisticated query capabilities, including catalogues.
    For more general queries see SQL support.

    Returns:
      dict: r.
    """
    f = 'tests/data/slv'
    db = shelve.open(f)
    o1 = ['The', 'bright', ('side', 'of'), ['life']]
    o2 = {'name' : 'Brian', 'age' : 33, 'motto' : o1}

    db['brian'] = o2
    db['knight'] = {'name' : 'Knight', 'motto' : 'Ni!'}
    db.close()

    db = shelve.open(f)
    l1 = len(db)
    ks = list(db.keys())
    o3 = db['knight']
    db.close()

    r = {'len' : l1, 'keys' : ks, 'knight' : o3}
    return r


if __name__ == '__main__' :
    fn = 'tests/data/data.txt'
    bfn = 'tests/data/data.bin'
    b = open(fn, 'rb').read()
    print(open(fn, 'rb').read())

    open(bfn, 'wb').write(b'Spam\n')
    b = open(bfn, 'rb').read()
    print(open(bfn, 'rb').read())

    bf = open(fn, 'rb')

    file = open('tests/data/data.txt', 'r')
    for line in file.readlines() :
        print(line, end="")
        file.close()

    open('tests/data/data.txt', 'w').write('Overwrite file world!\n')

    with open('tests/data/data.txt', 'r') as myfile:
        lines = myfile.readlines()
        print(lines)
        for line in lines:
            print(line, end='')


def persistTest() :
    r = {'flatFile' : flatFile(), 'binFile' : binFile(),
         'randAccess' : raFile(), 'dbm' : dbmFile(),
         'pickle' : pklFile(), 'shelve' : slvFile()}
    return r
