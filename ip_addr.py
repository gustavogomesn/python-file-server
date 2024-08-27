import socket

class IpAddr():
   
    def get_domain_name(self, ip_address):
        try:
            hostname = socket.gethostbyaddr(ip_address)[0]
            return hostname
        except socket.herror:
            return "No domain name found"
