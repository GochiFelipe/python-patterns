import string
from random import choice
from unittest import TestCase
from unittest.main import main

from pytterns.Builder import Builder


class BuilderTests(TestCase):
    def __get_random_string(self):
        letters = string.ascii_lowercase
        return ''.join(choice(letters) for i in range(14))

    def setUp(self):
        class TestBuilder:
            def __init__(self) -> None:
                self.test_attribute_1 = None
                self.test_attribute_2 = None

        self.builder = Builder(TestBuilder)

    def test_build(self):
        attribute_1 = self.__get_random_string()
        attribute_2 = self.__get_random_string()

        test_builder = (self.builder()
                        .test_attribute_1(attribute_1)
                        .test_attribute_2(attribute_2)
                        .build
                        )

        self.assertEqual(test_builder.test_attribute_1, attribute_1)
        self.assertEqual(test_builder.test_attribute_2, attribute_2)


if __name__ == '__main__':
    main()
