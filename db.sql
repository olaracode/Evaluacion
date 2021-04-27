SELECT productos.id, productos.nombre, info_productos.info_tipo
FROM productos
INNER JOIN info_productos
ON info_productos.id_product=productos.id
WHERE fecha_creacion >= SYSDATE() - 2
AND NOT info_tipo = "Color"