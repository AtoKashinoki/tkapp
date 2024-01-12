from tkapp.descriptor.Validator import DataType, Attribute


class AttrTest:
    __attributes__ = {"test"}


class Test:
    dtype = DataType(any, mode="r")
    attr = Attribute("test", mode="r")

    def __init__(self):
        self.dtype = None
        self.attr = AttrTest()


if __name__ == '__main__':
    Test()
