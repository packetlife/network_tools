import requests

try:
    # Prompt user for an IP address
    ip = input("Enter an IP address (leave blank to use your own): ").strip()

    # If no IP is provided, get user's public IP
    if not ip:
        ip_response = requests.get("https://api.ipify.org?format=json", timeout=10)
        ip_response.raise_for_status()
        ip = ip_response.json()["ip"]

    # Get geolocation info
    geo_response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
    geo_response.raise_for_status()
    geo_data = geo_response.json()

    # Display results
    print(
        f"""
        IP address  : {geo_data.get("query", "N/A")}
        City        : {geo_data.get("city", "N/A")}
        Area        : {geo_data.get("regionName", "N/A")}
        Postal code : {geo_data.get("zip", "N/A")}
        Country     : {geo_data.get("country", "N/A")}
        """
    )

except requests.exceptions.RequestException as e:
    print(f"Network error: {e}")
except ValueError as e:
    print(f"JSON decoding error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")

