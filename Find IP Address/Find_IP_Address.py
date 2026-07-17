# Import the socket module for network operations
import socket as s

# Retrieve the current machine's hostname
my_hostname = s.gethostname()
# Print the hostname
print("Your Hostname is: " + my_hostname)

# Resolve the local IP address from the hostname
my_ip = s.gethostbyname(my_hostname)
# Print the local IP address
print("Your IP Address is: " + my_ip)

# Define the target hostname to resolve
host = "github.com"
# Resolve the target hostname to an IP address
ip = s.gethostbyname(host)

# Print the resolved IP address
print("The IP Address of " + host + " is: " + ip)