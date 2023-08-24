from checkers import checkout, getout

def test_step1():
    assert checkout(f'cd {folderIn}; 7z a {folderOut}/arh1', "Everything is Ok"), "test1 FAIL"


def test_step2():
    assert checkout(f'cd {folderIn}; 7z u {folderOut}/arh1', "Everything is Ok"), "test2 FAIL"

def test_step3():
    assert checkout(f'cd {folderOut}; 7z l arh1.7z', "Compressed"), "test3 FAIL"

def test_step4():
    assert checkout(f'cd {folderOut}; 7z x -y arh1.7z', "Everything is Ok"), "test4 FAIL"

def test_step5():
    hash = getout(f"crc32 {folderOut}/arh1.7z").replace('\n', '').upper()
    assert checkout(f'cd {folderOut}; 7z h arh1.7z', hash), "test5 FAIL"

def test_step6():
    assert checkout(f'cd {folderIn}; 7z d {folderOut}/arh1', "Everything is Ok"), "test6 FAIL"

folderIn = '/home/user/tst'
folderOut = '/home/user/tstout'