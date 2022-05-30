/* Este método busca todo que contenga la clase .btn-delete
y implementamos la confirmación sobre la acción de borrar
un contacto (registro). */

const btnDelete = document.querySelectorAll('.btn-delete')

/* Comprovar se btnDelete existe para evitar errores */
if(btnDelete) {
    const btnArray = Array.from(btnDelete); /* transforma en array para recorrerlo */
    btnArray.forEach((btn) => { /* por cada boton que se recorra */
        btn.addEventListener('click', (e) => { /* se agraga un evento de escucha, que será click */
            if(!confirm('¿Desea realmente borrar esta tarea?')) { /* Se una ventana de confirm aparece */
                e.preventDefault(); /* Se no se confirma, se cancela */
            }
        });
    });
}
