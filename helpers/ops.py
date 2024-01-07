from difflib import SequenceMatcher
from zlib import compress, decompressobj, Z_BEST_COMPRESSION, MAX_WBITS


def pack(data: str) -> bytes:
    return compress(data.encode('utf-8'), Z_BEST_COMPRESSION)


def unpack(data: bytes) -> str:
    return decompressobj().decompress(data).decode('utf-8')

def most_similar(target: str, names: list[str]) -> str:
    max_similarity = 0
    most_similar_name = ''

    for name in names:
        similarity = similar_names(target, name)
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_name = name

    return most_similar_name

def similar_names(name_1: str, name_2: str) -> float:
    return SequenceMatcher(None, name_1, name_2).ratio() * 100
