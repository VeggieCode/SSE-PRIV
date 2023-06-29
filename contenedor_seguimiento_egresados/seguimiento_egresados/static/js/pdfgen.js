function generarPDF() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/generar-pdf/');
    xhr.setRequestHeader('Content-Type', 'application/pdf');
    xhr.onload = function() {
        if (xhr.status === 200) {
            var blob = new Blob([xhr.response], {type: 'application/pdf'});
            var url = URL.createObjectURL(blob);
            var link = document.createElement('a');
            link.href = url;
            link.download = 'constancia.pdf';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }
    };
    xhr.responseType = 'arraybuffer';
    xhr.send();
}