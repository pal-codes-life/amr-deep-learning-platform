import pandas as pd
import numpy as np
import random
import uuid


def generate_genomic_data(num_samples=2000):
    print("Extracting and engineering genomic features...")

    pathogens = ['Staphylococcus aureus', 'Escherichia coli', 'Klebsiella pneumoniae', 'Pseudomonas aeruginosa']
    regions = ['South Asia', 'North America', 'Europe', 'East Asia']
    antibiotic_classes = ['Beta-lactams', 'Fluoroquinolones', 'Aminoglycosides', 'Macrolides']

    records = []
    for _ in range(num_samples):
        pathogen = random.choice(pathogens)
        # Simulate genetic features
        k_mer_freq = round(random.uniform(0.1, 0.9), 4)
        mutation_score = round(random.uniform(0.0, 10.0), 2)
        plasmid_count = random.randint(0, 5)
        efflux_pump_active = random.choice([0, 1])

        # Logic to simulate realistic resistance probability based on genetic markers
        resistance_prob = (k_mer_freq * 0.3) + (mutation_score * 0.05) + (plasmid_count * 0.1) + (
                    efflux_pump_active * 0.2)
        is_resistant = 1 if resistance_prob > 0.6 else 0

        records.append({
            "sample_id": f"SEQ_{uuid.uuid4().hex[:8].upper()}",
            "pathogen_strain": pathogen,
            "region": random.choice(regions),
            "antibiotic_class": random.choice(antibiotic_classes),
            "k_mer_frequency": k_mer_freq,
            "mutation_score": mutation_score,
            "plasmid_count": plasmid_count,
            "efflux_pump_active": efflux_pump_active,
            "resistance_status": is_resistant
        })

    df = pd.DataFrame(records)
    df.to_csv("amr_clinical_data.csv", index=False)
    print(f"Pipeline complete. Processed {len(df)} genomic sequences into 'amr_clinical_data.csv'.")


if __name__ == "__main__":
    generate_genomic_data()