import requests

def fetch_boc(series_id, recent):
    url = f"https://www.bankofcanada.ca/valet/observations/{series_id}/json"
    response = requests.get(url, params={"recent": recent})
    data = response.json()

    rows =[]
    for obs in data["observations"]: 
        date = obs["d"]
        value = float(obs[series_id]["v"])
        rows.append((date, value))

    return rows


fx = fetch_boc("FXUSDCAD", 3)
print("USD/CAD:", fx)

rate = fetch_boc("V39079", 3)
print("Overnight rate:", rate)






  


