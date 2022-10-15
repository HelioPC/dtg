def ls_del_occ(ls: list, occ) -> list:
    return list(filter(occ.__ne__, ls))
