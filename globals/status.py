from os import path

INITIALIZED: bool = path.exists('./.dtg/') and path.exists('./.dtg/models.dat') and path.exists(
    './.dtg/index.json')
