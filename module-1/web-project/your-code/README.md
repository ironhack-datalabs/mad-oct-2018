## API 

Utilicé la API de Coindesk la cual te permite descargarte el histórico de precios de Bitcoin. 

En el Jupyter Notebook se describen los pasos que seguí. Entre lo que más me costó fue hacer los whiles al comienzo para garantizar que el usuario escriba de forma correcta los parámetros, me imagino que debe haber una forma más sencilla de hacerlo y con menos líneas, probablemente definiendo un par de funciones. 

En muchos casos los datos no me venian como me hubiese gustado y por eso tengo q manipularlos bastante para poder limpiarlos y quedarme con lo que quiero. 

Es un poco largo el programa ya que para poder mostrar el precio promedio del año tengo que hacer un Request por año, esto es así, ya que si el usuario por ejemplo pone que quiere ver del 2017 nada mas de enero a marzo, la peticion no me descargaria los precios q van desde marzo a diciembre y el resultado no sería el correcto. 


## WORD

Decidí extraer las tasas de cambio del BCE, fue mucho más simple de lo que pensaba así que opté por traerme también el nombre y el precio de los productos que aparecen en la sección de Deals de Ebay. Finalmente me propuse calcular el precio de todos los productos con algunas de las monedas que importe del BCE. Al comienzo intenté hacerlo concatenado los dos dataframes y luego haciendo un merge pero no conseguí como por lo que opte por hacerlo trabajando con iteraciones, me costó bastante trabajo, mucho ensayo y error, pero al final salió bien. 

En líneas generales me gustó el proyecto, intenté hacerlo lo mejor que pude dado la escasa información que tenía, a lo mejor hubiese sido mejor otra API que tuviese más para jugar. 



