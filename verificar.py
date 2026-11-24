#!/usr/bin/env python3
"""Verifica que asignacion_propuesta.csv no rompa las reglas duras. Uso: python3 verificar.py
El archivo debe tener las columnas: cliente_nuevo_id, ejecutivo_id, regla_aplicada (o «pendiente» en ejecutivo_id)."""
import csv, sys
from datetime import date
HOY = date(2026, 11, 24)
ej = {r["ejecutivo_id"]: r for r in csv.DictReader(open("datos/carteras_ejecutivos.csv"))}
act = list(csv.DictReader(open("datos/carteras_clientes.csv")))
nue = {r["cliente_nuevo_id"]: r for r in csv.DictReader(open("datos/clientes_nuevos.csv"))}
carga = {}
for c in act: carga[c["ejecutivo_actual"]] = carga.get(c["ejecutivo_actual"], 0) + 1
def capacidad(e):
    r = ej[e]; cap = int(r["capacidad_clientes"])
    if r["estado"] == "licencia": return 0
    if r["estado"] == "ramp-up" and (HOY - date.fromisoformat(r["fecha_estado"])).days <= 90: return cap // 2
    return cap
errores, filas = [], list(csv.DictReader(open("asignacion_propuesta.csv")))
vistos = {f["cliente_nuevo_id"] for f in filas}
for n in nue:
    if n not in vistos: errores.append(f"{n}: no aparece en la propuesta")
nuevos_por_ej = {}
for f in filas:
    n, e = f["cliente_nuevo_id"], f["ejecutivo_id"].strip()
    if n not in nue: errores.append(f"{n}: no es un cliente nuevo"); continue
    if e.lower() == "pendiente": continue
    if e not in ej: errores.append(f"{n}: el ejecutivo {e} no existe"); continue
    nuevos_por_ej[e] = nuevos_por_ej.get(e, 0) + 1
    c = nue[n]
    if (c["potencial"] == "A" or int(c["facturacion_anual_estimada"]) > 150_000_000) and ej[e]["nivel"] != "senior":
        errores.append(f"{n}: regla 2, necesita un ejecutivo senior y {e} es {ej[e]['nivel']}")
    if ej[e]["estado"] == "licencia": errores.append(f"{n}: regla 3, {e} está de licencia")
    if not f.get("regla_aplicada", "").strip(): errores.append(f"{n}: regla 10, falta la regla aplicada")
for e, k in nuevos_por_ej.items():
    if carga.get(e, 0) + k > capacidad(e):
        errores.append(f"{e}: regla 3, queda con {carga.get(e,0)+k} clientes y su capacidad efectiva es {capacidad(e)}")
print(f"{len(filas)} filas revisadas, {len(errores)} problemas")
for x in errores: print(" -", x)
sys.exit(1 if errores else 0)
