from zlib import compress, decompress, Z_BEST_COMPRESSION


def pack(data: str) -> bytes:
    return compress(data.encode(), Z_BEST_COMPRESSION)


def unpack(data: bytes) -> str:
    return decompress(data).decode('utf-8')
