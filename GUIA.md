# Guía del grupo 5 · Asignación de carteras

Su proyecto: repartir las carteras de clientes entre los ejecutivos de ventas, con reglas que el equipo acuerda y que Claude aplica.

## 1. Tu espacio (10 minutos)
1. Pulsa **Use this template → Create a new repository**, ponle el nombre de tu grupo y déjalo **público**. Agrega a tu grupo en Settings → Collaborators.
2. Abre el repositorio en `claude.ai/code`. Reparte los roles: **autor A**, **autor B** y **revisor** (en grupos de tres; en grupos de dos, el revisor es quien no escribe el segundo cambio).
3. Pide a Claude: *«Lee este proyecto y dime en cinco líneas qué problema resuelve, qué archivos hay y qué reglas debo respetar.»*

## 2. El CLAUDE.md mínimo y el proyecto (10 minutos)
1. Pide: *«Dime qué de este archivo puedes deducir del código y las carpetas, y propón la versión más resumida posible, con solo lo que una sesión nueva, sin memoria, necesita saber.»*
2. Compara con el original: ¿quedaron las reglas del proceso, los datos permitidos y quién aprueba? Eso nadie lo puede deducir.
3. Pide: *«Completa proyecto.md con el problema, para quién es y cómo se mide, a partir de reglas.md y datos/. Pregúntame lo que falte.»*

## 3. Dos cambios, una línea, un conflicto (25 minutos)
Los dos autores cambian la **regla 3**, cada uno en su rama y por su lado.
- **Autor A:** *«Crea una rama, cambia la regla 3 de reglas.md para que ningún ejecutivo tenga más de 18 clientes, sin importar su capacidad, haz commit con un mensaje que diga qué cambió y por qué, y abre un pull request.»*
- **Autor B:** *«Crea una rama, cambia la regla 3 de reglas.md para que ningún ejecutivo tenga más de 16 clientes, aunque su capacidad sea mayor, haz commit con un mensaje que diga qué cambió y por qué, y abre un pull request.»*
1. El revisor revisa el pull request del autor A con `REVIEW.md` (*«Lee este pull request y dime si cambia solo lo que se pidió, si hay datos que no deben estar y si se entiende sin quien lo escribió.»*) y el dueño lo acepta.
2. El pull request del autor B queda en conflicto. Pide: *«Explícame qué cambió cada rama en la línea en conflicto y propón cómo unirlas. No apliques nada hasta que yo elija.»* Decidan como grupo y digan: *«Elijo la opción … y completa el merge con su commit.»*
3. Con la regla final, pregunta: *«Con datos/carteras_clientes.csv y datos/carteras_ejecutivos.csv, ¿cuántos ejecutivos superan hoy el tope y cuántos clientes habría que mover?»*

## 4. Deja el traspaso (8 minutos)
1. Pide: *«Escribe traspaso.md con las cinco preguntas, a partir de lo que hicimos hoy.»* Léelo y corrígelo.
2. Pruébalo: abre una sesión **nueva** y pide *«Lee CLAUDE.md y traspaso.md y dime cuál es el siguiente paso y qué no debo tocar.»*
3. Pega en el chat el enlace de tu pull request.
