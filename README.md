# Antimicrobial Resistance (AMR) Deep Learning Platform

## Overview
A life-sciences data platform designed to bridge computational biology and artificial intelligence. This pipeline extracts simulated genomic features from microbial DNA sequences, stores them in a clinical relational database for epidemiological tracking, and deploys a deep learning neural network to predict pathogen resistance to specific antibiotic classes.

## Architecture
* **Genomic Data Engineering (`genomic_data_pipeline.py`):** Simulates the extraction of genetic markers (k-mer frequencies, mutation scores, plasmid counts, efflux pump activity) into structured feature matrices.
* **Clinical BI Analytics (`clinical_analytics_sql.py`):** Utilizes SQLite to aggregate and track geographic trends and strain-specific mutation frequencies across simulated patient populations.
* **Deep Learning Classifier (`amr_dl_classifier.py`):** Implements a Multi-Layer Perceptron (MLP) neural network using Scikit-Learn to classify bacterial strains as susceptible or resistant, optimizing for high clinical accuracy.

## Tech Stack
* **Languages:** Python, SQL
* **Data & Analytics:** Pandas, NumPy, SQLite
* **AI/Machine Learning:** Scikit-Learn (MLPClassifier, StandardScaler)
* **Domain:** Bioinformatics, Pathogen Genomics, Predictive Epidemiology
