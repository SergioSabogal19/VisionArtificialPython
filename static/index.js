function validarSelecciones() {
    var select1 = document.getElementById('select1').value;
    var select2 = document.getElementById('select2').value;
    var select3 = document.getElementById('select3').value;
    var select4 = document.getElementById('select4').value;

    // Verificar que los valores sean diferentes
    if (select1 == select2 || select1 == select3 || select1 == select4 ||
        select2 == select3 || select2 == select4 ||
        select3 == select4) {
        alert("Por favor, seleccione valores diferentes para cada almacenamiento.");
        return false; // Detener el envío del formulario
    }
    else{
        return true; // Continuar con el envío del formulario
    }

    
}