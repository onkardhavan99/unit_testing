class TestClass:
    @classmethod
    def setup_class(cls):
        print("Setup class.")

    @classmethod
    def teardown_class(cls):
        print("Teardown class.")

    def setup_method(self, function):
        if function == self.test1:
            print("\nSetting up test1.")
        elif function == self.test2:
            print("\nSetting up test2.")
        else:
            print("\nSetting up unknown test.")

    def teardown_method(self, function):
        if function == self.test1:
            print("\nTearing down test1.")
        elif function == self.test2:
            print("\nTearing down test2.")
        else:
            print("\nTearing down unknown test.")

    def test1(self):
        print("Execution test1.")
        assert True

    def test2(self):
        print("Execution test2.")
        assert True