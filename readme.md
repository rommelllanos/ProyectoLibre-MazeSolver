# Maze Solver - AI 1 Project

## Realizado por:
### Rommel Llanos: 15-10789
### Jesús Marcano: 12-10359

## Descripción
Este proyecto es una implementación de varios algoritmos de búsqueda (Búsqueda en Profundidad, Búsqueda en Amplitud, Búsqueda de Costo Uniforme y A*) para resolver laberintos. La entrada principal del proyecto es el archivo `MazeSolver.py`. Asegúrate de tener todos los paquetes necesarios instalados (numpy, matplotlib, etc).

## Cómo ejecutar el proyecto

Para correr el proyecto, sigue estos pasos:

1. Asegúrate de tener Python instalado en tu máquina.
3. Corre el archivo `MazeSolver.py` utilizando Python. Puedes hacer esto ejecutando `python MazeSolver.py` en tu terminal.

## Detalles de la Implementación

### Estructuras de Datos

Nuestra implementación hace uso de tres estructuras de datos principales:

- **Queue**: En esta implementación de una cola FIFO (Primero en Entrar, Primero en Salir), se utiliza en la búsqueda en amplitud (BFS). La clase Queue tiene operaciones básicas como `enqueue` (para agregar elementos al final de la cola) y `dequeue` (para eliminar elementos del frente de la cola).

- **Stack**: Esta implementación de una pila LIFO (Último en Entrar, Primero en Salir) es utilizada en la búsqueda en profundidad (DFS). La clase Stack también tiene operaciones de `push` (para agregar elementos al tope de la pila) y `pop` (para eliminar elementos desde el tope de la pila).

- **PriorityQueueImpl**: Esta es una implementación de una cola de prioridad, que se utiliza en la búsqueda de costo uniforme (UCS) y en la búsqueda A*. Los elementos se insertan en la cola de prioridad basados en su costo en UCS y en su costo más la heurística en A*.

### Laberinto y Azulejos (Tiles)

El laberinto se representa como una matriz en la que cada celda puede contener un obstáculo (representado por '-') o un terreno transitable (representado por 0, 1, 2, 3). Cada celda transitable es un "Tile". Los Tiles son implementados en dos clases, `TileWithoutHeuristic` y `TileWithHeuristic`. Ambas clases contienen el costo para moverse a ese Tile, pero `TileWithHeuristic` adicionalmente contiene un valor de heurística para la búsqueda A*.

## Desafíos

- **Elección de las estructuras de datos**: Elegir las estructuras de datos correctas fue un desafío inicial. Las estructuras de datos que escogimos debían adaptarse a las necesidades de los algoritmos de búsqueda. Asegurarse de que las estructuras de datos fueran eficientes también fue crucial para el rendimiento del programa.

- **Manejo de obstáculos y caminos**: Dado que cada celda puede contener un obstáculo o un terreno con un costo de tránsito diferente, tuvimos que diseñar una manera de manejar estos casos en cada algoritmo de búsqueda.

- **Generación aleatoria de laberintos**: Crear un laberinto aleatorio que siempre sea resoluble presentó su propio conjunto de desafíos. En este aspecto, se implementó una generación sencilla de laberintos, pero es importante notar que no siempre garantiza un camino resoluble.

## Hallazgos

- **Performance de los algoritmos de búsqueda**: A través de este proyecto, pudimos apreciar las diferencias en eficiencia entre los diversos algoritmos de búsqueda. Por ejemplo, la búsqueda en profundidad (DFS) puede encontrar rápidamente un camino, pero no necesariamente el más corto, mientras que la búsqueda A* siempre encuentra el camino más corto, pero puede tomar más tiempo.

- **Importancia de la heurística en A***: Este proyecto también destacó la importancia de elegir una buena heurística en la búsqueda A*. Una heurística mal elegida puede llevar a que A* se comporte peor que UCS, mientras que una heurística bien elegida puede mejorar significativamente la eficiencia del algoritmo.

- **Visualización de los resultados**: Una de las partes más satisfactorias del proyecto fue la visualización de los laberintos y las soluciones. Esto no sólo hizo el proyecto más interesante, sino que también nos ayudó a entender mejor cómo funcionan los algoritmos de búsqueda.

## Consideraciones

Al ejecutar este proyecto, ten en cuenta las siguientes consideraciones:

1. Asegúrate de tener todos los paquetes necesarios instalados. Puedes instalar las dependencias con el comando `pip install -r requirements.txt`.
2. El programa generará un laberinto de manera aleatoria. Ten en cuenta que no todos los laberintos generados serán resolubles. Si recibes un error de que no se pudo encontrar un camino, simplemente intenta ejecutar el programa de nuevo.
3. Para cambiar la heurística utilizada en la búsqueda A*, deberás modificar el código directamente. En esta implementación, la heurística es un valor aleatorio, lo que puede llevar a que la búsqueda A* no siempre encuentre el camino más corto. Experimenta con diferentes funciones de heurística para ver cómo afectan los resultados.
4. El tamaño del laberinto y los costos de las celdas transitables son generados aleatoriamente. Si necesitas un control más preciso sobre estos parámetros para tus experimentos, podrías modificar el código para permitir la entrada de estos parámetros por parte del usuario.

## Conclusiones

A través de este proyecto, pudimos apreciar la utilidad y eficiencia de varios algoritmos de búsqueda en la solución de problemas de laberinto. Los resultados nos mostraron la importancia de la elección de las estructuras de datos y las heurísticas en la eficacia de los algoritmos.

La implementación de la generación aleatoria de laberintos nos permitió poner a prueba nuestros algoritmos en una amplia variedad de casos. Aunque la generación de laberintos no garantiza siempre un laberinto resoluble, esto añadió un elemento de incertidumbre que hizo que el proyecto fuera más desafiante e interesante.

Además, este proyecto resaltó la importancia de la visualización en la comprensión de los algoritmos de búsqueda. La capacidad de visualizar el laberinto y la ruta encontrada por cada algoritmo nos ayudó a entender mejor cómo funcionan estos algoritmos y cómo se comparan entre sí.

En resumen, este proyecto nos proporcionó una valiosa oportunidad para aplicar y entender mejor los algoritmos de búsqueda que se estudian en el curso de AI 1. Aunque la implementación tuvo sus desafíos, la resolución de estos desafíos fue una experiencia de aprendizaje enriquecedora.

Esperamos que este proyecto te ayude a entender mejor estos algoritmos y te inspire a explorar más en el campo de la inteligencia artificial.
