# Tec1
Esta versión es una adaptación del prototipo, la cual cuenta con una base de datos en Sqlite y además se utiliza Python para desarrollarla.

Si manejas Python te darás cuenta que este .py es capaz de crear su propia base de datos con Sqlite en caso de ser necesario y el nombre de la bd
es "datos.db" si quieres puedes cambiarlo, esto lo hice para poder asegurarme que en caso de que se borre la base de datos el programa pueda seguir
funcionando correctamente y no le falte ninguna columna.

En caso de que te salga un error de que falta una columna recomiendo que borres el archivo de la base de datos y vuelvas a ejecutar el programa, eso
debería solucionar el problema, en caso de que quieras solucionarlo recuerda que puedes modificar "datos.db" borras la tabla y la vuelves a crear
respetando los parametros del .py.




A una cosa que se me olvidaba los tipo de datos son casi todos TEXT excepto el id que se creó como PRIMARY KEY y además es AUTOINCREMENT,
también como este .py lo manejaba yo, no tuve mucho cuidado al nombrar las variables/atributos/nombredetablas por eso existe la columna correo pero al final no van correos ahí, pero ese tipo de cosas si te molestan las puedes llegar a editar, 
