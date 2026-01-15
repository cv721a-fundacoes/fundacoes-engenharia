# -*- coding: utf-8 -*-
"""
Script pyRevit para cálculo do volume total de concreto (m³)
em fundações (categoria Structural Foundation), com foco em sapatas.

Disciplina: Fundações
Objetivo: Quantitativos BIM aplicados à engenharia estrutural
"""

from pyrevit import script
from Autodesk.Revit.DB import (
    FilteredElementCollector,
    BuiltInCategory,
    BuiltInParameter,
    UnitUtils,
    UnitTypeId
)

doc = __revit__.ActiveUIDocument.Document
output = script.get_output()

output.print_md("## Quantitativo de Concreto – Sapatas (m³)")
output.print_md(
    "Coleta elementos da categoria **Structural Foundation** e soma o parâmetro **Volume**."
)

# Coleta todos os elementos da categoria 'Structural Foundation'
foundations = (
    FilteredElementCollector(doc)
    .OfCategory(BuiltInCategory.OST_StructuralFoundation)
    .WhereElementIsNotElementType()
    .ToElements()
)

if not foundations:
    output.print_md("**Nenhuma fundação encontrada** no modelo (categoria Structural Foundation).")
    script.exit()

volume_total_m3 = 0.0
cont_com_volume = 0
cont_sem_volume = 0

for elem in foundations:
    vol_param = elem.get_Parameter(BuiltInParameter.HOST_VOLUME_COMPUTED)

    if vol_param and vol_param.HasValue:
        # Volume vem em unidades internas do Revit (ft³). Convertemos para m³.
        vol_ft3 = vol_param.AsDouble()
        vol_m3 = UnitUtils.ConvertFromInternalUnits(vol_ft3, UnitTypeId.CubicMeters)

        volume_total_m3 += vol_m3
        cont_com_volume += 1
    else:
        cont_sem_volume += 1

output.print_md("---")
output.print_md("**Elementos encontrados:** {}".format(len(foundations)))
output.print_md("**Com volume computado:** {}".format(cont_com_volume))
output.print_md("**Sem volume computado:** {}".format(cont_sem_volume))
output.print_md("### **Volume total de concreto:** {:.2f} m³".format(volume_total_m3))

if cont_sem_volume > 0:
    output.print_md(
        "> Observação: alguns elementos não possuem volume computado. "
        "Isso pode indicar família sem sólido válido, categoria incorreta, ou parâmetros indisponíveis."
    )
