# Tarea 3 Laboratorio de Seminario de Sistemas 1

Api REST realizada en Python utilizando el framework Flask. Para el reconocimiento de imágenes con ayuda de la herramienta Rekognition de AWS.

## Endpoints

### /tarea3-201906570
Retorna un estado 200 si la operación es correcta y un estado 400 si ha ocurrido un error.

POST
JSON esperado.
```json
{
    "img": string de imagen en base64
}
```

JSON de respuesta.
```json
{
    "data": arreglo etiquetas de Rekognition
}
```
