productos = {}
proveedores = {}

contador_productos = 1
contador_proveedores = 1

usuarios_registrados = {("usuario1", "usuario1@gmail.com", "contraseña1")}

admin_registrados = {("1", "2", "3")}


def agregar_producto():
  global contador_productos

  print("----------------")
  print("Agregar producto")
  print("----------------")
  nombre = input("Nombre del producto: ")
  descripcion = input("Descripción del producto: ")
  precio = float(input("Precio del producto: "))
  cantidad = int(input("Cantidad en existencia: "))

  producto = {
    "id": contador_productos,
    "nombre": nombre,
    "descripcion": descripcion,
    "precio": precio,
    "cantidad": cantidad
  }

  productos[contador_productos] = producto
  contador_productos += 1

  print("¡Producto agregado exitosamente!")


def mostrar_proveedores():
  print("-------------------------------------------")
  print("Proveedores agregados por el administrador:")
  print("-------------------------------------------")
  for proveedor_id, proveedor in proveedores.items():
    print(f"ID: {proveedor['id']}")
    print(f"Nombre: {proveedor['nombre']}")
    print(f"Dirección: {proveedor['direccion']}")
    print(f"Teléfono: {proveedor['telefono']}")
    print(f"Producto: {proveedor['producto']}")
    print("----------------------")


def agregar_proveedor():
  global contador_proveedores

  print("-----------------")
  print("Agregar proveedor")
  print("-----------------")
  nombre = input("Nombre del proveedor: ")
  direccion = input("Dirección del proveedor: ")
  telefono = int(input("Teléfono del proveedor: "))
  producto = input("Nombre del producto : ")

  proveedor = {
    'id': contador_proveedores,
    'nombre': nombre,
    'direccion': direccion,
    'telefono': telefono,
    'Producto': producto
  }

  proveedores[contador_proveedores] = proveedor
  contador_proveedores += 1

  print("¡Proveedor agregado exitosamente!")


def modificar_proveedor():
  print("-------------------")
  print("Modificar proveedor")
  print("-------------------")
  id_proveedor = int(input("Ingresa el ID del proveedor a actualizar: "))
  proveedor = proveedores.get(id_proveedor)

  if proveedor:
    print(f"Actualizando proveedor con ID {id_proveedor}:")
    print("Deja en blanco si no deseas modificar un campo.")
    nombre = input(f"Nombre actual ({proveedor['nombre']}): ")
    direccion = input(f"Dirección actual ({proveedor['direccion']}): ")
    telefono = input(f"Teléfono actual ({proveedor['telefono']}): ")
    producto = input(f"Producto actual ({proveedor['telefono']}): ")
    if nombre:
      proveedor['nombre'] = nombre
    if direccion:
      proveedor['direccion'] = direccion
    if telefono:
      proveedor['telefono'] = int(telefono)
    if producto:
      proveedor['producto'] = (producto)
    print("¡Proveedor actualizado exitosamente!")
  else:
    print(f"No se encontró un proveedor con ID {id_proveedor}")


def eliminar_proveedor():
  print("------------------")
  print("Eliminar proveedor")
  print("------------------")
  id_proveedor = int(input("Ingresa el ID del proveedor a eliminar: "))
  proveedor = proveedores.get(id_proveedor)

  if proveedor:
    del proveedores[id_proveedor]
    print(f"Proveedor con ID {id_proveedor} eliminado exitosamente.")
  else:
    print(f"No se encontró un proveedor con ID {id_proveedor}")


def ver_productos():
  print("------------------")
  print("Productos en stock")
  print("------------------")

  for producto_id, producto in productos.items():
    print(f"ID: {producto['id']}")
    print(f"Nombre: {producto['nombre']}")
    print(f"Descripción: {producto['descripcion']}")
    print(f"Precio: {producto['precio']}")
    print(f"Cantidad en existencia: {producto['cantidad']}")
    print("----------------------")


def vista_cliente():
  print("----------------")
  print("Vista de Cliente")
  print("----------------")
  print("1. Ver productos")  #YA
  print("2. Buscar productos por nombre")  #NO
  print("3. Comprar producto")  #NO
  print("4. Cerrar sesión")  #YA

  opcion = input("Qué quieres hacer? (número): ")

  if opcion == "1":
    ver_productos()

  if opcion == "3":
    vista_cliente()

  if opcion == "2":
    nombre_producto = input("Ingresa el nombre del producto: ")
    clave_producto = buscar_producto_por_nombre(nombre_producto)
    if clave_producto:
      print("Información del producto encontrado:")
      print("ID: {}".format(clave_producto['id']))
      print("Nombre: {}".format(clave_producto['nombre']))
      print("Descripción: {}".format(clave_producto['descripcion']))
      print("Precio: ${}".format(clave_producto['precio']))
      print("Cantidad: {}".format(clave_producto['cantidad']))
    else:
      print("No se encontró ningún producto con el nombre '{}'.".format(
        nombre_producto))
      vista_cliente()

  if opcion == "4":
    vista_usuario()


def buscar_producto_por_nombre(nombre):
  for producto in productos.values():
    if producto['nombre'].lower() == nombre.lower():
      return producto
  return None


def vista_usuario():
  print("----------------")
  print("Vista de Usuario")
  print("----------------")
  print("1. Inicio de sesión como Admin")  #YA
  print("2. Crear cuenta de cliente")  #YA
  print("3. Inicio de sesión como Cliente")  #YA
  print("4. Ver productos")  #YA
  print("5. Buscar productos por nombre")  #NO

  opcion = input("Qué quieres hacer? (número): ")

  if opcion == "1":

    def inicio_admin():
      print("+-------------------------+")
      print("Inicio de sesión como admin")
      print("+-------------------------+")
      usuario_admin = str(input("Ingrese el nombre de usuario de admin: "))
      correo_admin = str(input("Ingrese el correo de admin: "))
      contraseña_admin = str(input("Ingrese la contraseña de admin: "))

      if (usuario_admin, correo_admin, contraseña_admin) in admin_registrados:

        def vista_admin():
          print("--------------")
          print("Vista de Admin")
          print("--------------")
          print("1. CRUD de productos")  #YA
          print("2. CRUD de proveedores")  #YA
          print("3. Cerrar sesión")  #YA

          opcion = input("Qué quieres hacer? (número): ")

          if opcion == "1":

            def crud_productos():
              print("-------------------")
              print("CRUD del inventario")
              print("-------------------")
              print("1. Agregar productos")  #YA
              print("2. Modificar un producto")  #YA
              print("3. Eliminar un producto")  #YA
              print("4. Ver productos")  #YA
              print("5. Cerrar CRUD")  #YA
              opcion = input("Qué quieres hacer? (número): ")

              if opcion == "1":
                agregar_producto()
                crud_productos()

              if opcion == "2":

                def modificar_producto():
                  print("---------------------")
                  print("Modificar un producto")
                  print("---------------------")
                  id_producto = int(
                    input("Ingresa el ID del producto a actualizar: "))
                  producto = productos.get(id_producto)

                  if producto:
                    print(f"Actualizando producto con ID {id_producto}:")
                    print("Deja en blanco si no deseas modificar un campo.")
                    nombre = input(f"Nombre actual ({producto['nombre']}): ")
                    descripcion = input(
                      f"Descripción actual ({producto['descripcion']}): ")
                    precio = input(f"Precio actual ({producto['precio']}): ")
                    cantidad = input(
                      f"Cantidad actual ({producto['cantidad']}): ")

                    if nombre:
                      producto['nombre'] = nombre

                    if descripcion:
                      producto['descripcion'] = descripcion

                    if precio:
                      producto['precio'] = float(precio)

                    if cantidad:
                      producto['cantidad'] = int(cantidad)

                    print("¡Producto actualizado exitosamente!")

                  else:
                    print(f"No se encontró un producto con ID {id_producto}")
                    crud_productos()

                modificar_producto()
                crud_productos()

              if opcion == "3":

                def eliminar_producto():
                  print("-----------------")
                  print("Eliminar producto")
                  print("-----------------")
                  id_producto = int(
                    input("Ingresa el ID del producto a eliminar: "))
                  producto = productos.get(id_producto)

                  if producto:
                    del productos[id_producto]
                    print(
                      f"Producto con ID {id_producto} eliminado exitosamente.")
                    crud_productos()

                  else:
                    print(f"No se encontró un producto con ID {id_producto}")
                    crud_productos()

                eliminar_producto()
                crud_productos()

              if opcion == "4":
                ver_productos()
                crud_productos()

              if opcion == "5":
                vista_admin()

            crud_productos()

          if opcion == "2":

            def crud_proveedores():
              print("-------------------")
              print("CRUD de los proveedores")
              print("-------------------")
              print("1. Agregar proveedor")  #YA
              print("2. Modificar proveedor")  #YA
              print("3. Eliminar proveedor")  #YA
              print("4. Mostrar proveedores")  #YA
              print("5. Cerrar CRUD")  #YA

              opcion = input("Qué quieres hacer? (número): ")

              if opcion == "1":
                agregar_proveedor()
                crud_proveedores()

              if opcion == "2":
                modificar_proveedor()
                crud_proveedores()

              if opcion == "3":
                eliminar_proveedor()
                crud_proveedores()

              if opcion == "4":
                mostrar_proveedores()
                crud_proveedores()

              if opcion == "5":
                vista_admin()

            crud_proveedores()

          if opcion == "3":
            vista_usuario()

        vista_admin()

    inicio_admin()

  if opcion == "2":

    def crear_cliente():
      print("-----------------------")
      print("Crear cuenta de cliente")
      print("-----------------------")

      print(
        "Para leer los términos y condiciones ingrese al siguiente link: https://docs.google.com/document/d/1Qa8v_BgM7MPCLaY508wct5bU6lnuIJItOQK2zCQZ2o0/edit?usp=sharing"
      )
      print()

      ingreso_usuario = input(
        "Ingrese el nombre usuario para la nueva cuenta: ")
      ingreso_correo = input("Ingrese el correo para la nueva cuenta: ")
      ingreso_contraseña = input(
        "Ingrese la contraseña para la nueva cuenta: ")
      ingreso_confirmar_contraseña = input(
        "Ingrese nuevamente la contraseña para confirmarla: ")

      if ingreso_contraseña == ingreso_confirmar_contraseña:
        terminos_condiciones = str(
          input("Acepta los terminos y condiciones de la empresa Si o No: "))

        if terminos_condiciones == "Si":
          usuarios_registrados.add(
            (ingreso_usuario, ingreso_correo, ingreso_contraseña))
          print("Se ha creado la cuenta exitosamente")
          vista_cliente()

        if terminos_condiciones == "No":
          print(
            "Lo sentimos, pero debe aceptar los términos y condiciones para crear una cuenta de cliente"
          )
          vista_usuario
      if ingreso_contraseña != ingreso_confirmar_contraseña:
        print(
          "Las contraseñas no coinciden, vuelva a hacer el registro o inicio de sesión"
        )
        crear_cliente()

    crear_cliente()
    vista_usuario()

  if opcion == "3":

    def inicio_cliente():
      print("-----------------------------")
      print("Inicio de sesión como Cliente")
      print("-----------------------------")

      usuario_cliente = input("Ingrese el usuario: ")
      correo_cliente = input("Ingrese el correo: ")
      contraseña_cliente = input("Ingrese la contraseña: ")
      if (usuario_cliente, correo_cliente,
          contraseña_cliente) in usuarios_registrados:
        print("¡Inicio de sesión exitoso!")
        vista_cliente()
      else:
        print("Los datos ingresados no coinciden con ninguna cuenta")
        vista_usuario()

    inicio_cliente()

  if opcion == "4":
    ver_productos()
    vista_usuario()

  if opcion == "5":
    nombre_producto = input("Ingresa el nombre del producto: ")
    clave_producto = buscar_producto_por_nombre(nombre_producto)
    if clave_producto:
      print("Información del producto encontrado:")
      print("ID: {}".format(clave_producto['id']))
      print("Nombre: {}".format(clave_producto['nombre']))
      print("Descripción: {}".format(clave_producto['descripcion']))
      print("Precio: ${}".format(clave_producto['precio']))
      print("Cantidad: {}".format(clave_producto['cantidad']))
    else:
      print("No se encontró ningún producto con el nombre '{}'.".format(
        nombre_producto))
      vista_usuario()


vista_usuario()