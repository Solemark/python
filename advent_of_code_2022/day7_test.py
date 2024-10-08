from pytest import fixture
from day7 import day7, File


@fixture
def data() -> tuple[list[str], list[File]]:
    return [
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
    ], [
        File("/", 23352670),
        File("/a/", 94269),
        File("/a/e/", 584),
        File("/d/", 24933642),
    ]


def test_day7(data: tuple[list[str], list[File]]) -> None:
    """
    TODO - the real result
    expect: list[File] = [
        File("/", 48381165),
        File("/a/", 94853),
        File("/a/e/", 584),
        File("/d/", 24933642),
    ]
    """
    inp, exp = data
    assert exp == day7(inp)
