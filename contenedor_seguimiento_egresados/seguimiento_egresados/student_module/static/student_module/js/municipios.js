$(document).ready(function() {
    var selectEstado = document.getElementById("estado");
    let prefix = '/sse'
    var selectMunicipio = document.getElementById("municipio");
    // Cuando se selecciona un estado, cargar los municipios correspondientes
    selectEstado.addEventListener("change", function() {
        var estadoId = this.value;
        if (estadoId) {
        let url = `${prefix}/municipios/${estadoId}/`;

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
