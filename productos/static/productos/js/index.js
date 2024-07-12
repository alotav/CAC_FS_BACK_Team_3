console.log("Se leyo el js");

document.addEventListener('DOMContentLoaded', function() {
    const imagenes = document.querySelectorAll('.novedad'); // Selecciona todas las imágenes de novedades
    let currentIndex = 0; // Índice de la imagen actual

    function mostrarImagen(index) {
        // Oculta todas las imágenes
        imagenes.forEach(imagen => imagen.style.display = 'none');
        // Muestra la imagen actual
        imagenes[index].style.display = 'block';
    }

    function mostrarImagenAnterior() {
        currentIndex = (currentIndex - 1 + imagenes.length) % imagenes.length;
        mostrarImagen(currentIndex);
    }

    function mostrarImagenSiguiente() {
        currentIndex = (currentIndex + 1) % imagenes.length;
        mostrarImagen(currentIndex);
    }

    // Mostrar la primera imagen al cargar la página
    mostrarImagen(currentIndex);

    // Agregar listeners a los botones de navegación
    document.getElementById('anterior').addEventListener('click', mostrarImagenAnterior);
    document.getElementById('siguiente').addEventListener('click', mostrarImagenSiguiente);
});