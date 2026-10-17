from fetch_data import fetch_boc, fetch_statcan
from db import init_db, save_observations

BOC_SERIES = ["FXUSDCAD", "V39079", "BD.CDN.2YR.DQ.YLD", "BD.CDN.10YR.DQ.YLD"]
CPI_VECTOR = 41690973


def run():
    init_db()

    for series_id in BOC_SERIES:
        rows = fetch_boc(series_id, 365)
        count = save_observations(series_id, rows)
        print(f"{series_id}: saved {count} rows")

    cpi_rows = fetch_statcan(CPI_VECTOR, 36)
    count = save_observations("CPI", cpi_rows)
    print(f"CPI: saved {count} rows")


if __name__ == "__main__":
    run()