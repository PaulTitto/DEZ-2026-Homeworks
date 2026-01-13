import pyarrow.parquet as pq
import csv




if __name__ == "__main__":
    # Membaca table
    table = pq.read_table('green_tripdata_2025-11.parquet')

    # Mengonversi ke CSV menggunakan modul csv bawaan atau pyarrow.csv
    import pyarrow.csv as pv

    pv.write_csv(table, "green_tripdata_2025-11.csv")