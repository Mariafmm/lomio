function GuardarCita(){
    swal({
      title: "Estas seguro?",
      text: "Se modificaran los datos de la cita",
      icon: "warning",
      buttons: true,
      dangerMode: true,
    }).then((willDelete) => {
      if (willDelete) {
        swal("OK! Su cita ha sido modificada con exito", {
          icon: "success",
        }).then(function() {
        window.location.href = "/Ventas/Calendario/";
     });
      } else {
        swal("OK! Ningun dato de su cita se ha modificado");
      }
    });

        }

function CancelarCita(){
    swal({
        title: "Tenga cuidado!",
        text: "Esta opcion no se puede desaser!",
        icon: "warning",
        buttons: true,
      }).then((willDelete) => {
        if (willDelete) {
          swal("OK! Se ha cancelado su cita", {
            icon: "success",
          }).then(function() {
          window.location.href = "/Ventas/Calendario/";
       });
        } else {
          swal("OK! No se cancelo la cita ");
        }
      });
}

function ConfirmarNoGuardarCita(){
  swal({
    title: "Estas seguro?",
    text: "No se guardaran los cambios que haya hecho",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  }).then((willDelete) => {
    if (willDelete) {
      swal("OK! Se redigira al listado de las citas", {
        icon: "error",
      }).then(function() {
      window.location.href = "/Ventas/ListadoCitas/";
   });
    } else {
      swal("OK! Puede seguir haciendo lo que estaba haciendo");
    }
  });
}

function GuardarCita(){
  swal({
    title: "Hecho",
    text: "Cita guardada",
    icon: "success",
  }).then(function() {
    window.location.href = "/Ventas/ListadoCitas/";
 });
}

function ConfirmarCita(){
  swal({
    title: "Hecho",
    text: "Cita Confirmada",
    icon: "success",
  });
}

function CancelarCita2(){
  swal({
      title: "Tenga cuidado!",
      text: "Esta opcion no se puede desaser!",
      icon: "warning",
      buttons: true,
    }).then((willDelete) => {
      if (willDelete) {
        swal("OK! Se ha cancelado su cita", {
          icon: "success",
        }).then(function() {
        window.location.href = "/Ventas/ListadoCitas/";
     });
      } else {
        swal("OK! No se cancelo la cita ");
      }
    });
}

// catalogo

function abrir_modal_detalleServicio(url){
  $("#VerMasServivios").load(url, function (){  
    $(this).appendTo("body").modal("show");
  });
}


