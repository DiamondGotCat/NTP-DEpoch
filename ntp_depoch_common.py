import struct
from datetime import datetime, timezone

EPOCH_2000 = datetime(2000, 1, 1, tzinfo=timezone.utc)

def now_dgc_epoch_ms() -> int:
    delta = datetime.now(timezone.utc) - EPOCH_2000
    return int(delta.total_seconds() * 1000)

def pack_packet(version: int, mode: int, originate: int, receive: int, transmit: int) -> bytes:
    return struct.pack(">BBHQQQ", version, mode, 0, originate, receive, transmit)

def unpack_packet(data: bytes):
    version, mode, _, originate, receive, transmit = struct.unpack(">BBHQQQ", data)
    return version, mode, originate, receive, transmit
