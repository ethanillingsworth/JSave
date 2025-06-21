from jsave import PickleFile
import os

if (not os.path.exists("pickles")):
    os.mkdir("pickles")

somedata = {"hello": "world"}

somedata2 = 2010494.1341

somedata3 = PickleFile("somecustomclass.data")

file1 = PickleFile("pickles/1.dat")
file2 = PickleFile("pickles/2.dat")
file3 = PickleFile("pickles/3.dat")

file1.pickle(somedata)
file2.pickle(somedata2)
file3.pickle(somedata3)

def test_file_1():
    assert somedata == file1.unpickle()

def test_file_2():
    assert somedata2 == file2.unpickle()

def test_file_3():
    assert somedata3 == file3.unpickle()
