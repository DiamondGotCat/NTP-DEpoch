import socket
from ntp_depoch_common import now_dgc_epoch_ms, pack_packet, unpack_packet

SERVER = input("NTP-DEpoch Server IP/Domain: ")
PORT = 15432
BUF_SIZE = 28

while True:

  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  sock.settimeout(2)
  
  t1 = now_dgc_epoch_ms()
  req = pack_packet(1, 3, t1, 0, 0)
  sock.sendto(req, (SERVER, PORT))
  
  data, _ = sock.recvfrom(BUF_SIZE)
  t4 = now_dgc_epoch_ms()
  
  _, _, orig, t2, t3 = unpack_packet(data)
  
  offset = ((t2 - t1) + (t3 - t4)) / 2
  delay = (t4 - t1) - (t3 - t2)
  
  print(f"T₁={t1}, T₂={t2}, T₃={t3}, T₄={t4}")
  print(f"Offset: {offset:.3f} ms, Delay: {delay:.3f} ms")
  print(f"Corrected time (DGC Epoch): {now_dgc_epoch_ms() + offset:.0f} ms")
