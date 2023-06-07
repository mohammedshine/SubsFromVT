iimport requests

def get_subdomains(api_key, domain):
    url = f'https://www.virustotal.com/vtapi/v2/domain/report'
    params = {'apikey': api_key, 'domain': domain}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        subdomains = data.get('subdomains', [])
        return subdomains
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []

api_key = '<INPUT YOUR VT API KEY HERE>'
domain = input("Enter the domain: ")
subdomains = get_subdomains(api_key, domain)
print(f"Subdomains for {domain}:")
for subdomain in subdomains:
    print(subdomain)

