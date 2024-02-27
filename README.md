# Documentación del Proyecto con SQLite y Python
Este proyecto está desarrollado en Python y utiliza SQLite para la gestión de una base de datos denominada datos.db. El diseño está pensado para garantizar robustez y flexibilidad, permitiendo la creación automática de la base de datos y sus estructuras necesarias si estas no existen previamente. Esto asegura una alta disponibilidad y reduce el riesgo de interrupciones por problemas relacionados con la base de datos.

Características Principales:

-  Creación Automática de la Base de Datos: El script está diseñado para verificar la existencia de la base de datos al inicio. Si datos.db no se encuentra, el programa procederá a crearla automáticamente junto con las tablas y columnas necesarias.
  
-  Manejo de Errores: En caso de encontrarse con un error relacionado con la ausencia de columnas, se recomienda eliminar el archivo datos.db y ejecutar nuevamente el programa. Esta acción regenerará la base de datos con la estructura correcta.
  
-  Flexibilidad en la Modificación de la Estructura: Si necesitas ajustar la estructura de la base de datos, como eliminar o añadir tablas y columnas, puedes hacerlo directamente modificando el script y respetando los parámetros definidos.

Estructura de la Base de Datos:

-  ID: Campo de identificación única para cada registro, configurado como PRIMARY KEY y AUTOINCREMENT.
  
-  Otros Campos: Predominantemente de tipo TEXT, con la excepción del campo ID. Se incluye una columna llamada correo, la cual, a pesar de su nombre, no se utiliza para almacenar direcciones de correo electrónico. Este aspecto puede ser modificado según las necesidades del proyecto.

Buenas Prácticas Implementadas:

-  Nomenclatura Clara: Aunque en la versión inicial no se prestó especial atención a la nomenclatura de variables, atributos y nombres de tablas, se reconoce la importancia de una nomenclatura clara y descriptiva para el mantenimiento y escalabilidad del proyecto.
  
-  Flexibilidad y Mantenibilidad: El diseño permite fácil adaptación y modificación de la estructura de la base de datos, lo que contribuye a un mantenimiento eficiente y facilita futuras actualizaciones o cambios en los requisitos del proyecto.

Recomendaciones:

-  Para garantizar la integridad y el correcto funcionamiento del sistema:

     + Ante errores específicos relacionados con la estructura de la base de datos, considera revisar la documentación y los mensajes de error para realizar los ajustes necesarios de manera informada.
     + Aprovecha las capacidades de SQLite y Python para implementar prácticas de manejo de excepciones y registros de errores, lo que permitirá una mejor diagnóstico y resolución de problemas.
     + Considera la implementación de pruebas automatizadas para validar la lógica de negocio y la interacción con la base de datos, asegurando así la calidad y fiabilidad del sistema.
