from tkapp.Validator import DataType, Attribute, DataTypeDict, AttributeDict


class AttrTest:
    __attributes__ = {"test1", "test2"}


class Test:
    dtype = DataType(any, mode="r")
    attr = Attribute("test1", mode="r")
    ddict = DataType(DataTypeDict)
    adict = DataType(AttributeDict)

    def __init__(self):
        self.dtype = None
        self.attr = AttrTest()
        self.ddict = DataTypeDict(
            int, key_validate_data_types=(str, ),
            initial_values={"test": 1, "test2": 2}
        )
        self.adict = AttributeDict(
            "test2", key_validate_data_types=(str, ),
            initialize_values={"test": AttrTest}
        )


if __name__ == '__main__':
    print(Test().adict)
