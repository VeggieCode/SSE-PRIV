$(document).ready(function() {
    // Obtener una referencia a los elementos del DOM
    var selectEstado = document.getElementById("estado");
    console.log(selectEstado);
    var selectMunicipio = document.getElementById("municipio");
    // Cuando se selecciona un estado, cargar los municipios correspondientes
    selectEstado.addEventListener("change", function() {
        var estadoId = this.value;
        if (estadoId) {
        var url = "/municipios/" + estadoId + "/";
        $(selectEstado).selectpicker('refresh');

        fetch(url)
        .then(response => response.json())
        .then(municipios => {
            selectMunicipio.innerHTML = "<option value=''>Selecciona un municipio</option>";
            municipios.forEach(municipio => {
            var option = document.createElement("option");
            option.value = municipio.id;
            option.text = municipio.nombre;
            selectMunicipio.add(option);
            });
            $(selectMunicipio).selectpicker('refresh');

        });
    } else {
        // Si no se selecciona ningún estado, vaciar los municipios
        selectMunicipio.innerHTML = "<option value=''>Selecciona un municipio</option>";
        $(selectEstado).selectpicker('refresh');
        $(selectMunicipio).selectpicker('refresh');

    }
    });
});
