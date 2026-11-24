# Guía del grupo 5 · Asignación de carteras

Su proyecto: asignar los 16 clientes nuevos de `datos/clientes_nuevos.csv` entre los ejecutivos, con reglas que el equipo acuerda y que Claude aplica. Hay casos difíciles a propósito.

## 1. Tu espacio (10 minutos)
1. Pulsa **Use this template → Create a new repository**, ponle el nombre de tu grupo y déjalo **público**. Agrega a tu grupo en Settings → Collaborators.
2. Abre el repositorio en `claude.ai/code`. Reparte los roles: **autor A**, **autor B** y **revisor**. En grupos de dos, el revisor es quien no escribe el segundo cambio.
3. Pide: *«Lee este proyecto y dime en cinco líneas qué problema resuelve, qué archivos hay y qué reglas debo respetar.»*

## 2. El CLAUDE.md mínimo y el proyecto (10 minutos)
1. Pide: *«Dime qué de este archivo puedes deducir del código y las carpetas, y propón la versión más resumida posible, con solo lo que una sesión nueva, sin memoria, necesita saber.»*
2. Compara con el original: ¿quedaron las reglas del proceso, los datos permitidos y quién aprueba? Eso nadie lo puede deducir.
3. Pide: *«Completa proyecto.md con el problema, para quién es y cómo se mide, a partir de reglas.md y datos/. Pregúntame lo que falte.»*

## 3. Dos interpretaciones, un conflicto (25 minutos)
Las reglas 1 y 5 chocan: la zona y la especialidad no pueden ir primero las dos. Cada autor la resuelve distinto, en su rama.
- **Autor A:** *«Crea una rama, cambia la regla 5 de reglas.md para que la especialidad pase antes que la zona, asigna los clientes de datos/clientes_nuevos.csv en asignacion_propuesta.csv con las columnas cliente_nuevo_id, ejecutivo_id y regla_aplicada, corre verificar.py, haz commit con un mensaje que diga qué cambió y por qué, y abre un pull request.»*
- **Autor B:** *«Crea una rama, cambia la regla 1 de reglas.md para que la zona pase antes que la especialidad y la especialidad solo desempate, asigna los clientes de datos/clientes_nuevos.csv en asignacion_propuesta.csv con las columnas cliente_nuevo_id, ejecutivo_id y regla_aplicada, corre verificar.py, haz commit con un mensaje que diga qué cambió y por qué, y abre un pull request.»*

1. **El revisor** revisa el pull request del autor A con `REVIEW.md`. Pide a Claude: *«Lee este pull request y dime si cambia solo lo que se pidió, si hay información que no debería estar y si se entiende sin quien lo escribió. Corre verificar.py y dime qué problemas hay.»* El dueño acepta el pull request solo si el revisor lo aprueba.
2. **El pull request del autor B queda en conflicto**, en las reglas y en el archivo de asignación. Pide: *«Explícame qué cambió cada rama y propón cómo unirlas. No apliques nada hasta que yo elija.»* Decidan como grupo. Después: *«Elijo la opción … y completa el merge con su commit. Corre verificar.py.»*
3. Miren qué clientes quedaron pendientes o con problemas, y qué regla habría que aclarar. Eso es lo que le llevarían al jefe comercial.

## 4. Deja el traspaso (8 minutos)
1. Pide: *«Escribe traspaso.md con las cinco preguntas, a partir de lo que hicimos hoy.»* Léelo y corrígelo.
2. Pruébalo: abre una sesión **nueva** y pide *«Lee CLAUDE.md y traspaso.md y dime cuál es el siguiente paso y qué no debo tocar.»*
3. Pega en el chat el enlace de tu pull request.
