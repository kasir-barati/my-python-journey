import socket

port = 80
host = "data.pr4e.org"
socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# A transport layer virtual circuit established between two application programs for the purpose of communication.
socket1.connect((host, port))

# What is a command? HTTP is a generic, stateless, object-oriented protocol which can be used for many tasks, such as name servers and distributed object management systems, through extension of its request methods (commands).

# The Request-Line begins with a method token, followed by the Request-URI and the protocol version, and ending with CRLF.
command = f"GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n"

# Request Header Fields
# The reason for the Host header is to allow the server to disambiguate which website is being accessed, if multiple websites are being served up on the same IP address.
# But here since we are using HTTP 1.0 instead of HTTP 1.1 the following header is not required, so it may work if the server you're connecting to only has a single website on it, but if it's hosting multiple websites, you'll probably still get a 400 error. As such we just added it. Although with this server it works either way.
command = command + f"Host: {host}"

# Carriage Return Line Feed
command = command + "\r\n\r\n"
# The Request-URI is transmitted as an encoded string, where some characters may be escaped using the "% HEX HEX" encoding defined by RFC 1738 [4]. The origin server must decode the Request-URI in order to properly interpret the request.
# Here the encode method returns a bytes data type: https://docs.python.org/3/library/stdtypes.html#bytes
encoded_command = command.encode(encoding="utf-8")

socket1.send(encoded_command)

while True:
    # A feature of HTTP is the typing of data representation, allowing systems to be built independently of the data being transferred.
    data = socket1.recv(512)
    # We need to decode the bytes we received over the socket connection so that the strings internally are properly represented.
    decoded_data = data.decode()
    if (len(data) < 1):
        break
    print(decoded_data)

socket1.close()
