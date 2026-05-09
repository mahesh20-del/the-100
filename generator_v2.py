"""
DATA GHOST: PROJECT #07 - INDUSTRIAL SYNTHETIC DATA ENGINE
Version: 2.1.0
Domain: Data Engineering / Industrial Simulation
Description: High-fidelity sales generator for the textile industry, mapping 
             specific regional geography (Odisha, Gujarat, etc.) to 
             material-specific transaction logic.
Goal: Produce atomic-level datasets for PostgreSQL ingestion and 
      Business Intelligence (BI) analysis.
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class TextileDataEngine:
    def __init__(self):
        self.version = "2.1.0"
        self.client_pool = [f'Textile_House_{i}' for i in range(100, 500)]
        self.materials = ['Cotton', 'Silk', 'Linen', 'Polyester', 'Synthetic']
        self.geo_map = {
            'Odisha': ['Cuttack', 'Bhubaneswar', 'Sambalpur'],
            'Gujarat': ['Ahmedabad', 'Surat', 'Rajkot'],
            'Maharashtra': ['Mumbai', 'Pune', 'Nagpur'],
            'West Bengal': ['Kolkata', 'Howrah', 'Hooghly']
        }

    def _get_region(self, state):
        mapping = {
            'Odisha': 'East',
            'West Bengal': 'East',
            'Gujarat': 'West',
            'Maharashtra': 'West'
        }
        return mapping.get(state, 'Domestic')

    def generate(self, rows=1000):
        data = []
        for _ in range(rows):
            state = np.random.choice(list(self.geo_map.keys()))
            record = {
                'customer_name': np.random.choice(self.client_pool),
                'material_type': np.random.choice(self.materials),
                'sales_date': (datetime(2025, 1, 1) + timedelta(days=np.random.randint(0, 365))).strftime('%Y-%m-%d'),
                'meters_sold': round(np.random.uniform(5.0, 1000.0), 2),
                'district': np.random.choice(self.geo_map[state]),
                'state': state,
                'region': self._get_region(state),
                'version': self.version
            }
            data.append(record)
        
        df = pd.DataFrame(data)
        df.to_csv('textile_v2.csv', index=False)
        print(f"🚀 Machine Restored: {rows} rows generated using Engine v{self.version}")

if __name__ == "__main__":
    engine = TextileDataEngine()
    engine.generate()
