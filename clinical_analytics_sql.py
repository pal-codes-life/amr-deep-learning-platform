import sqlite3
import pandas as pd

print("Connecting to Clinical Database...")
conn = sqlite3.connect('clinical_amr_records.db')

# Load the engineered data
data = pd.read_csv('amr_clinical_data.csv')
data.to_sql('GenomicRecords', conn, if_exists='replace', index=False)

# SQL Query: Track resistance rates by pathogen strain
query_resistance = """
SELECT 
    pathogen_strain,
    COUNT(sample_id) as total_samples,
    SUM(resistance_status) as resistant_cases,
    ROUND((CAST(SUM(resistance_status) AS FLOAT) / COUNT(sample_id)) * 100, 2) as resistance_rate_pct
FROM GenomicRecords
GROUP BY pathogen_strain
ORDER BY resistance_rate_pct DESC;
"""

print("\n--- Geographic & Strain Resistance Trends ---")
results = pd.read_sql_query(query_resistance, conn)
print(results.to_string(index=False))

conn.close()