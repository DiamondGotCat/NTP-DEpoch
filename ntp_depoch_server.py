import socket
from ntp_depoch_common import now_dgc_epoch_ms, pack_packet, unpack_packet

PORT = 12345
BUF_SIZE = 28

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", PORT))
print(f"NTP-DEpoch server listening on UDP/{PORT}")

while True:
    data, addr = sock.recvfrom(BUF_SIZE)
    version, mode, orig, _, _ = unpack_packet(data)
    if version != 1 or mode != 3:
        continue

    t2 = now_dgc_epoch_ms()
    t3 = now_dgc_epoch_ms()
    resp = pack_packet(1, 4, orig, t2, t3)
    sock.sendto(resp, addr)
