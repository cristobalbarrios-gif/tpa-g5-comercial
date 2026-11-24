# Guía del grupo 5 · Asignación de carteras

Su proyecto: asignar los 16 clientes nuevos de `datos/clientes_nuevos.csv` entre los ejecutivos, con reglas que el equipo acuerda y que Claude aplica. Hay casos difíciles a propósito.

## 1. Tu espacio (10 minutos)
1. Pulsa **Use this template → Create a new repository**, ponle el nombre de tu grupo y déjalo **público**. Agrega a tu grupo en Settings → Collaborators.
2. Abre el repositorio en `claude.ai/code`. Reparte los roles: **autor A**, **autor B** y **revisor**. En grupos de dos, el revisor es quien no escribe el segundo cambio.
3. Pide: *«Lee este proyecto y dime en cinco líneas qué problema resuelve, qué archivos hay y qué reglas debo respetar.»*

## 2. El CLAUDE.md mínimo y el proyecto (10 minutos)
1. Pide: *«Dime qué de este archivo puedes deducir del código y las carpetas, y propón la versión más resumida posible, con solo lo que una sesión nueva, sin memoria, necesita saber.»*
2. Compara con el original: ¿quedaron las reglas del proceso, los datos permitidos y quién aprueba? Eso nadie lo puede deducir.
3. Pide: *«Completa proyecto.md con el problema y para quién es. Para «cómo se mide», propón una métrica que se pueda calcular con datos/, calcula su valor de hoy y propón una meta. Pregúntame lo que falte.»*
4. Decidan como grupo: ¿esa métrica mide lo que importa? Una buena métrica se puede recalcular después con `verificar.py` y los datos. Anoten en `proyecto.md` la métrica, su valor de hoy y la meta.

## 3. Tres trabajos a la vez, y un conflicto (25 minutos)
Las reglas 1 y 5 chocan: la zona y la especialidad no pueden ir primero las dos. Cada autor la resuelve distinto, en su rama. **Mientras tanto, el revisor no espera: prepara con qué va a revisar.** El dueño es quien creó el repositorio.

**Minutos 0 a 10: los tres trabajan a la vez**
- **Autor A:** *«Crea una rama, cambia la regla 5 de reglas.md para que la especialidad pase antes que la zona, asigna los clientes de datos/clientes_nuevos.csv en asignacion_propuesta.csv con las columnas cliente_nuevo_id, ejecutivo_id y regla_aplicada, corre verificar.py, haz commit con un mensaje que diga qué cambió y por qué, y abre un pull request.»*
- **Autor B:** *«Crea una rama, cambia la regla 1 de reglas.md para que la zona pase antes que la especialidad y la especialidad solo desempate, asigna los clientes de datos/clientes_nuevos.csv en asignacion_propuesta.csv con las columnas cliente_nuevo_id, ejecutivo_id y regla_aplicada, corre verificar.py, haz commit con un mensaje que diga qué cambió y por qué, y abre un pull request.»*
- **Revisor:** el verificador no revisa todas las reglas. Pide: *«Lee reglas.md y verificar.py y dime qué reglas de reglas.md no revisa verificar.py. Después agrega a verificar.py la revisión de las reglas 8 y 9 y de las filas repetidas, pruébalo y abre un pull request.»* Lee lo que Claude encuentra: eso es lo que más cuesta ver.

**Minutos 10 a 17: la revisión**
- El revisor revisa el pull request del autor A con `REVIEW.md` y con su verificador mejorado. Pide: *«Lee este pull request y dime si cambia solo lo que se pidió, si hay información que no debería estar y si se entiende sin quien lo escribió. Corre verificar.py y dime qué problemas hay, incluso los que el verificador no detecta.»*
- El dueño acepta el pull request de A solo si el revisor lo aprueba, y después el del verificador.

**Minutos 17 a 25: el conflicto**
- **El pull request del autor B queda en conflicto**, en las reglas y en el archivo de asignación. Pide: *«Explícame qué cambió cada rama y propón cómo unirlas. No apliques nada hasta que yo elija.»* Decidan como grupo. Después: *«Elijo la opción … y completa el merge con su commit. Corre verificar.py.»*
- Cierren con una lista de decisiones que le llevarían al jefe comercial: qué clientes quedaron pendientes y qué regla hay que aclarar.

## 4. Deja el traspaso (8 minutos)
1. Pide: *«Escribe traspaso.md con las cinco preguntas, a partir de lo que hicimos hoy.»* Léelo y corrígelo.
2. Pruébalo: abre una sesión **nueva** y pide *«Lee CLAUDE.md y traspaso.md y dime cuál es el siguiente paso y qué no debo tocar.»*
3. Pega en el chat el enlace de tu pull request.
