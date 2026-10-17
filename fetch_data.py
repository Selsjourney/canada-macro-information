import requests

def fetch_boc(series_id, recent):
    url = f"https://www.bankofcanada.ca/valet/observations/{series_id}/json"
    response = requests.get(url, params={"recent": recent}, timeout=15)
    response.raise_for_status() 
    data = response.json()

    rows =[]
    for obs in data["observations"]: 
        date = obs["d"]
        raw = obs.get(series_id, {}).get("v")                           
        if raw is None:                                                  
            continue  
        value = float(raw)
        rows.append((date, value))

    return rows


fx = fetch_boc("FXUSDCAD", 3)
print("USD/CAD:", fx)

rate = fetch_boc("V39079", 3)
print("Overnight rate:", rate)

def fetch_statcan(vector_id, latest_n):
    url = "https://www150.statcan.gc.ca/t1/wds/rest/getDataFromVectorsAndLatestNPeriods"
    body = [{"vectorId": vector_id, "latestN": latest_n}]

    response = requests.post(url, json=body, timeout=15)
    response.raise_for_status()
    data = response.json()

    rows = []
    for point in data[0]["object"]["vectorDataPoint"]:
        date = point["refPer"]
        raw = point.get("value")
        if raw is None:
            continue
        value = float(raw)
        rows.append((date, value))

    return rows

cpi = fetch_statcan(41690973, 3)
print("CPI:", cpi)






  


