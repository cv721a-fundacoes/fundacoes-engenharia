# Template de Modelagem — Projeto 2 (Fundações Profundas)

## Objetivo
Padronizar a modelagem mínima para permitir:
- rastreabilidade por estaca,
- comparação entre tipos,
- export para notebooks/relatórios,
- introdução conceitual de Digital Twin (integração de informações).

## Regras mínimas
1. Cada estaca deve ter `CV721A_ID` único (ex.: EST-001).
2. Preencher: `CV721A_Grupo`, `CV721A_Caso`.
3. Definir `CV721A_Estaca_Tipo` e dimensões principais.
4. Registrar a variável alvo escolhida no projeto (ex.: `CV721A_Estaca_CapUlt_kN`).
5. Blocos sobre estacas devem ter identificação e cota.

## Export (mínimo)
Gerar uma tabela (schedule) contendo:
- CV721A_ID
- CV721A_Grupo
- CV721A_Caso
- CV721A_Estaca_Tipo
- CV721A_Estaca_Diam_m
- CV721A_Estaca_Comp_m
- CV721A_Estaca_CapUlt_kN

Exportar em CSV para uso no notebook e no relatório.

> Digital Twin aqui é tratado como **integração de dados e modelo**, não como sistema completo.
