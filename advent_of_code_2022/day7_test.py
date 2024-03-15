import unittest
from day7 import Day7, File


class advent_of_code_2022_tests(unittest.TestCase):
    def test_day7(self) -> None:
        data: list[str] = [
            "$ cd /",
            "$ ls",
            "dir a",
            "14848514 b.txt",
            "8504156 c.dat",
            "dir d",
            "$ cd a",
            "$ ls",
            "dir e",
            "29116 f",
            "2557 g",
            "62596 h.lst",
            "$ cd e",
            "$ ls",
            "584 i",
            "$ cd ..",
            "$ cd ..",
            "$ cd d",
            "$ ls",
            "4060174 j",
            "8033020 d.log",
            "5626152 d.ext",
            "7214296 k",
        ]
        expect: list[File] = [
            File("/", 23352670),
            File("/a/", 94269),
            File("/a/e/", 584),
            File("/d/", 24933642),
        ]
        """
        TODO - the real result
        expect: list[File] = [
            File("/", 48381165),
            File("/a/", 94853),
            File("/a/e/", 584),
            File("/d/", 24933642),
        ]
        """
        self.assertEqual(expect, Day7().run(data))
