import os
import requests

#function to ping IP address and return the status
def ping_ip(ip):
    response = os.system(f"ping -c 1 {ip}")
    return "Active" if response == 0 else 'Not Active'

#function to store IP status in NetBox
def store_in_netbox(ip_status, netbox_url, netbox_token):
    headers = {
        'Authorization': f'Token {netbox_token}',
        'Content-Type': 'application/json'
    }

    for ip, status in ip_status.items():
        Description = 'Address for '+ip 
        data = {
            "address": ip,
            "Status": status,
            'description': Description 
        }
        response = requests.post(f"{netbox_url}/api/ipam/ip-addresses/", headers=headers, json=data)
        if response.status_code not in [200, 201]:
            print(f"Failed to store {ip}: {response.content}")

#main function
def main():
    ipam = {}
    hostname = "x.x.x." #replace with the first three octet of your IP address
    netbox_url = "http://netbox.url/"  # Replace with your NetBox URL
    netbox_token = "xyxyxyxyxyxyxyxyxy"  # Replace with your NetBox token
    
    for x in range(0, 256):
        ip = f"{hostname}{x}"
        ipam[ip] = ping_ip(ip)


    #store the IP status in NetBox
    store_in_netbox(ipam, netbox_url, netbox_token)

if __name__ == '__main__':
  main()
  
 
