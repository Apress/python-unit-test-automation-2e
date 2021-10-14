from nose2.tools import params

@params("Test1234", "1234Test", "Dino Candy")
def test_starts_with(value):
    assert value.startswith('Test')

if __name__ == '__main__':
    import nose2
    nose2.main()
