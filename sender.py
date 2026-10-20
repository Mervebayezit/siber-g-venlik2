import socket

destination = "192.168.100.12"
port = 5000

data = b"A" * 4000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# IPv4 Path MTU Discovery'yi kapat;
# gerekli olduğunda IP fragmentation'a izin ver.
sock.setsockopt(
    socket.IPPROTO_IP,
    10,  # Linux IP_MTU_DISCOVER
    0    # IP_PMTUDISC_DONT
)

sent = sock.sendto(data, (destination, port))

print("Gonderilen uygulama verisi:", sent, "bayt")

sock.close()