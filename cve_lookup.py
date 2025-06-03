import requests

def search_cve(query):
    url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={query}"
    response = requests.get(url)
    
    if response.status_code == 200:
        results = response.json()
        if results['totalResults'] > 0:
            for item in results['vulnerabilities']:
                cve_id = item['cve']['id']
                description = item['cve']['descriptions'][0]['value']
                print(f"CVE ID: {cve_id}")
                print(f"Description: {description}")
                print("-" * 40)
        else:
            print("No results found.")
    else:
        print("Error: Unable to fetch data")

if __name__ == "__main__":
    query = input("Enter CVE ID or search term (e.g., 'SQL injection'): ")
    search_cve(query)

