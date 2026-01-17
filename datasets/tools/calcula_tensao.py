import pandas as pd
import numpy as np

INFILE = "datasets/projeto1_fundacoes_rasas/dataset_fundacoes_rasas.csv"
OUTFILE = "datasets/projeto1_fundacoes_rasas/dataset_fundacoes_rasas_com_tensao.csv"

df = pd.read_csv(INFILE)

# Tipos numéricos (robustez)
df["tipo_solo"] = pd.to_numeric(df["tipo_solo"], errors="coerce").astype("Int64")
df["N_SPT_medio"] = pd.to_numeric(df["N_SPT_medio"], errors="coerce")
df["nivel_fundacao_m"] = pd.to_numeric(df["nivel_fundacao_m"], errors="coerce")
df["carga_kN"] = pd.to_numeric(df["carga_kN"], errors="coerce")

# Sanidade mínima
if df[["tipo_solo", "N_SPT_medio", "nivel_fundacao_m"]].isna().any().any():
    raise ValueError("Há valores ausentes/inválidos em tipo_solo, N_SPT_medio ou nivel_fundacao_m.")

# Coeficiente por tipo de solo (didático)
coef_map = {1: 22, 2: 18, 3: 14}
coef_solo = df["tipo_solo"].map(coef_map)

if coef_solo.isna().any():
    raise ValueError("tipo_solo contém valores fora do domínio {1,2,3}.")

coef_solo = coef_solo.astype(float)

# Limita profundidade ao domínio do dataset (opcional, recomendado)
z = df["nivel_fundacao_m"].clip(0.6, 2.0)

# Fator de profundidade: (z-0.6)/(2.0-0.6) = (z-0.6)/1.4
fz = 1.0 + 0.12 * ((z - 0.6) / 1.4)

tensao = coef_solo * df["N_SPT_medio"] * fz

# Clamp e arredondamento
df["tensao_admissivel_kPa"] = np.clip(tensao, 80, 450).round(1)

# Ordem institucional das colunas
cols = [
    "id_caso",
    "tipo_solo",
    "N_SPT_medio",
    "nivel_fundacao_m",
    "carga_kN",
    "tensao_admissivel_kPa",
    "area_sapata_m2",
]

missing = [c for c in cols if c not in df.columns]
if missing:
    raise ValueError(f"Colunas ausentes no CSV de entrada: {missing}")

df = df[cols]

df.to_csv(OUTFILE, index=False, encoding="utf-8")
print(f"OK: arquivo gerado em {OUTFILE}")
