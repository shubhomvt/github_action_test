from src.math_operations import add,sub

##this will be my testcases that we run
##assert statement checks if its equal
##these are my unit use cases that I want to execute
##pytest lib will look at it

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    

def test_sub():
    assert sub(5,3)==0
    assert sub(4,3)==1
    assert sub(3,3)==0
    assert sub(2,3)==-1