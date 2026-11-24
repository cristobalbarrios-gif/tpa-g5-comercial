# Guía del grupo 5 · Asignación de carteras

Su proyecto: asignar los 16 clientes nuevos de `datos/clientes_nuevos.csv` entre los ejecutivos, con reglas que el equipo acuerda y que Claude aplica. Hay casos difíciles a propósito.

**Hoy cada persona hará los tres roles, uno por fase.** En una fase todos tienen el mismo rol y trabajan a la vez, sin esperar a nadie. Quien dicta avisa «cambio de fase».

| Minutos | Fase |
|---|---|
| 0 a 6 | Tu espacio |
| 6 a 14 | Calentamiento: poda el CLAUDE.md |
| 14 a 27 | **Fase 1: autores** |
| 27 a 37 | **Fase 2: revisores** |
| 37 a 53 | **Fase 3: dueños** |
| 53 a 55 | Cierre |

## Tu espacio (6 minutos)
1. **Una persona del grupo** pulsa **Use this template → Create a new repository**, ponle el nombre de tu grupo y déjalo **público**. En Settings → Collaborators agrega a las demás. Esa persona es la dueña del repositorio.
2. **Todas** abren el repositorio en `claude.ai/code` y piden: *«Lee este proyecto y dime en cinco líneas qué problema resuelve, qué archivos hay y qué reglas debo respetar.»*

## Calentamiento: poda el CLAUDE.md (8 minutos)
Cada persona, por su lado, pide: *«Dime qué de este archivo puedes deducir del código y las carpetas, y propón la versión más resumida posible, con solo lo que una sesión nueva, sin memoria, necesita saber. No modifiques el archivo.»*
Comparen en el grupo: ¿qué reglas conservó cada versión? Las que nadie puede deducir (quién aprueba, la capacidad, los datos permitidos, la rama y el pull request) tienen que estar.

## Fase 1 · Autores (13 minutos)
Las reglas 1 y 5 chocan: la zona y la especialidad no pueden ir primero las dos. **Cada persona elige una opción distinta**, la resuelve en su propia rama y abre su propio pull request:
- **Opción 1, zona primero:** la especialidad solo desempata.
- **Opción 2, especialidad primero:** la zona solo desempata.
- **Opción 3, capacidad primero:** el cliente va al ejecutivo con más espacio libre, y la zona y la especialidad desempatan.
- **Opción 4, la tuya:** define la prioridad que te parezca mejor y explícala.

En grupos de dos usen las opciones 1 y 2; de tres, la 1, 2 y 3; de cuatro, todas.

Pide: *«Crea una rama, cambia las reglas 1 y 5 de reglas.md para que [tu opción], asigna los clientes de datos/clientes_nuevos.csv en asignacion_propuesta.csv con las columnas cliente_nuevo_id, ejecutivo_id y regla_aplicada, corre verificar.py, haz commit con un mensaje que diga qué cambió y por qué, y abre un pull request.»*

Si terminas antes, mira qué clientes quedaron pendientes y por qué.

## Fase 2 · Revisores (10 minutos)
Cada persona revisa el pull request de **otra**, en círculo: la primera revisa a la segunda, la segunda a la tercera, la última a la primera. En grupos de dos, se intercambian. Si el pull request que te toca no llegó, revisa `ejemplo-para-revisar/`.

Pide: *«Lee este pull request y dime si cambia solo lo que se pidió, si hay información que no debería estar y si se entiende sin quien lo escribió. Corre verificar.py y dime qué problemas hay, incluso los que el verificador no detecta. Deja tu revisión como comentario del pull request, con un veredicto: aprobar, pedir cambios o no aprobar.»*

Revisa también con `REVIEW.md`. Pasar el verificador no basta.

## Fase 3 · Dueños (16 minutos, todos juntos)
Ahora el grupo decide como dueño del repositorio.
1. **Aceptar (4 minutos).** Lean las tres o cuatro revisiones. Acepten primero el pull request mejor evaluado, con el botón **Merge** de GitHub: aceptar lo hace una persona.
2. **Conflicto (7 minutos).** Los demás pull requests chocan ahora con `main`. Abran el siguiente en `claude.ai/code` y pidan: *«Explícame qué cambió cada rama y propón cómo unirlas. No apliques nada hasta que yo elija.»* Decidan como grupo y digan: *«Elijo la opción … y completa el merge con su commit. Corre verificar.py.»* Resuelvan dos como máximo. Lo que quede se anota como decisión pendiente para el jefe comercial.
3. **Traspaso (5 minutos).** Pidan: *«Escribe traspaso.md con las cinco preguntas, a partir de lo que hicimos hoy.»* Léanlo y corríjanlo. Pruébenlo abriendo una sesión **nueva**: *«Lee CLAUDE.md y traspaso.md y dime cuál es el siguiente paso y qué no debo tocar.»*

Si sobra tiempo: pidan *«Completa proyecto.md con el problema y para quién es. Para «cómo se mide», propón una métrica que se pueda calcular con datos/, calcula su valor de hoy y propón una meta. Pregúntame lo que falte.»*

## Cierre (2 minutos)
Peguen en el chat el enlace de su repositorio y una frase: qué decisión le llevarían al jefe comercial.
