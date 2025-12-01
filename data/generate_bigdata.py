import pandas as pd
import numpy as np
from datetime import datetime, timedelta

print("🔧 Generiere 5 Millionen E-Commerce Transaktionen...")
print("⏳ Das dauert ca. 2-3 Minuten...")

np.random.seed(42)

# Anzahl der Zeilen
n = 5_000_000

# Datumsspanne: 2 Jahre
start_date = datetime(2022, 1, 1)

dates = [start_date + timedelta(days=np.random.randint(0, 730)) for _ in range(n)]

#Generiere Daten
data = {
    'transaction_id': range(1, n + 1),
    'customer_id': np.random.randint(1000, 50000, n),
    'product_category': np.random.choice(['Electronics', 'Fashion', 'Home', 'Sports', 'Books'], n),
    'product_price': np.round(np.random.uniform(5, 500, n), 2),
    'quantity': np.random.randint(1, 10, n),
    'date': dates,
    'payment_method': np.random.choice(['Credit Card', 'PayPal', 'Bank Transfer', 'Cash'], n),
    'country': np.random.choice(['Germany', 'Austria', 'Switzerland', 'Netherlands', 'Belgium'], n)
}

# Total berechnen
df = pd.DataFrame(data)
df['total'] = df['product_price'] * df['quantity']
# Speichern als CSVprint("💾 Speichere CSV...")
df.to_csv('ecommerce_5m.csv', index=False)
print(f"✅ Fertig! Dataset erstellt:")
print(f"   - Zeilen: {len(df):,}")
print(f"   - Spalten: {len(df.columns)}")
print(f"   - Dateigröße: ~500 MB")
print(f"   - Datei: ecommerce_5m.csv")