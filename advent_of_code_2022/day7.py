from dataclasses import dataclass


@dataclass
class File:
    path: str
    size: int


def day7(data: list[str]) -> list[File]:
    sort: list[File] = []
    totals: list[File] = []
    path: str = ""
    total: int = 0
    for item in data:
        cmnd_comp = item.split()
        if cmnd_comp[0] == "$":
            if cmnd_comp[1] == "cd":
                if cmnd_comp[2] == "..":
                    chars: list[str] = path.replace("/", " ").split()
                    path = path.removesuffix(f"{chars[-1]}/")
                elif cmnd_comp[2] == "/":
                    path += "/"
                else:
                    path += f"{cmnd_comp[2]}/"
        else:
            if cmnd_comp[0] != "dir":
                sort.append(File(path, int(cmnd_comp[0])))
    # TODO - sort.sort() dont assume data is correctly sorted to be counted
    # TODO - can this section down below be done in the sort?
    path = "/"
    for i in range(sort.__len__()):
        if i == sort.__len__() - 1:
            total += sort[i].size
            totals.append(File(path, total))
            break
        if path == sort[i].path:
            print(path)
            total += sort[i].size
        else:
            print(path)
            totals.append(File(path, total))
            total = sort[i].size
            path = sort[i].path
    # TODO - calculate the size of dir's and sub dir's
    return totals
