import binascii, struct, socket, datetime, time

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    for angle in range(360):
        sock.sendto(angle.to_bytes(2, 'big')+b'\x01', ("127.0.0.1", 5000))
        print(angle)
        time.sleep(0.0006)