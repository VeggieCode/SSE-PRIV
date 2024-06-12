/** The variable municipiosEndpoint should be defined in script tag inside the template that is using this script. */
$(document).ready(function () {
    // Obtener una referencia a los elementos del DOM
    var selectEstado = document.getElementById("estado");
    var selectMunicipio = document.getElementById("municipio");
    // Cuando se selecciona un estado, cargar los municipios correspondientes
    selectEstado.addEventListener("change", function () {
        let estadoId = this.value;
        if (estadoId) {
            const url = municipiosEndpoint.replace('0', estadoId)
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

                });
        } else {
            // Si no se selecciona ningún estado, vaciar los municipios
            selectMunicipio.innerHTML = "<option value=''>Selecciona un municipio</option>";
        }
    });
});