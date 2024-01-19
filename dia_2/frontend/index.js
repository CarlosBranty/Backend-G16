console.log("hola");

async function pedirProductos() {
  const solicitud = await fetch("http://127.0.0.1:5000/productos");
  console.log(solicitud.status);
  // solo se puede utilizar el text o el json no se puede utilizar los 2 al mismo tiempo
  //   console.log(await solicitud.text());
  console.log(await solicitud.json()); //me sala informacion parseada npara que JS la pueda entender
}
pedirProductos();
