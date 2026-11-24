# Propuesta de ejemplo para revisar

Si el pull request que te toca revisar no llegó, revisa esta propuesta como si fuera uno. La escribió un autor que eligió **capacidad primero**: el cliente va al ejecutivo con más espacio libre, y la zona y la especialidad solo desempatan.

Qué dice el autor en su pull request:

> Cambié las reglas 1 y 5 para que la capacidad vaya primero. Asigné los 16 clientes en `asignacion_propuesta_ejemplo.csv` y corrí `verificar.py`. Para que se entienda el caso, dejé en el commit al contacto de N-009 (Pedro Soto, RUT 12.345.678-0) como ejemplo de cliente que pidió atención en Centro.

Para revisarla, pide a Claude: *«Lee ejemplo-para-revisar/README.md y corre `python3 verificar.py ejemplo-para-revisar/asignacion_propuesta_ejemplo.csv`. Dime si cambia solo lo que se pidió, si hay información que no debería estar y si se entiende sin quien lo escribió, y qué problemas hay incluso si el verificador no los detecta.»*
