import example

def text_compare():
    a = example.Vector(1,2)
    b = example.Vector(3,4)

    assert a.x == b.x
    assert a.y == b.y
    assert a == b
