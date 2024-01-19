console.log("hola");

const button = document.getElementById("crearProductoBtn");
const nombreProducto = document.getElementById("nombre");
const precioProducto = document.getElementById("precio");
const disponibleProducto = document.getElementById("disponible");

function crearProducto(e) {
  e.preventDefault();
  const body = {
    nombre: nombreProducto.value,
    precio: precioProducto.value,
    disponible: disponibleProducto.checked,
  };
  crearProductoRequest(body)
    .then((resultado) => {
      if (resultado === true) {
        alert("Producto creado exitosamente");
      } else {
        alert("Error al crear el producto");
      }
    })
    .catch((e) => {
      alert(`Error al crear el producto ${e.message}`);
    });
}

async function crearProductoRequest(body) {
  // stringfy convierte el objeto a un JSON
  const solicitud = await fetch("http://127.0.0.1:5000/producto", {
    method: "POST",
    body: JSON.stringify(body),
    headers: {
      "Content-Type": "application/json",
      // gracias a los header el backend sabra que informacion recibe, cuestiones de autenticacion, el origen de la peticion entre otros
    },
  });
  return solicitud.status === 201;
}
button.addEventListener("click", crearProducto);

async function pedirProductos() {
  const solicitud = await fetch("http://127.0.0.1:5000/productos");
  console.log(solicitud.status);
  // solo se puede utilizar el text o el json no se puede utilizar los 2 al mismo tiempo
  //   console.log(await solicitud.text());
  console.log(await solicitud.json()); //me sala informacion parseada npara que JS la pueda entender
}
pedirProductos();
