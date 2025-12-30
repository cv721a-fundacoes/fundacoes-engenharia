# Template de Modelagem — Projeto 1 (Fundações Rasas)

## Objetivo
Padronizar a modelagem mínima para permitir:
- rastreabilidade (ID por elemento),
- extração de parâmetros,
- export para notebooks/relatórios.

## Regras mínimas
1. Cada sapata/bloco deve ter `CV721A_ID` único (ex.: RAS-001).
2. Preencher: `CV721A_Grupo`, `CV721A_Caso`, `CV721A_Carga_kN`.
3. Preencher parâmetros do projeto: tipo e dimensões principais.
4. Manter coerência geométrica (unidades, cotas, orientação).

## Export (mínimo)
Gerar uma tabela (schedule) contendo:
- CV721A_ID
- CV721A_Grupo
- CV721A_Caso
- CV721A_Carga_kN
- CV721A_Sapata_Tipo
- CV721A_Sapata_B_m
- CV721A_Sapata_L_m
- CV721A_Sapata_Area_m2
- CV721A_sigma_adm_kPa

Exportar em CSV para uso no notebook e no relatório.
