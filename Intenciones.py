# Esta clase sirve para definir la estructura de las preguntas y respuestas.
# ¡Hola! Estás hablando con Tomatobot, asistente virtual que te ayudará
# con tus dudas sobre TomatoGo!

class Intenciones:
    def __init__(self, nombre, opcion, ejemplo, respuesta):
        self.nombre = nombre
        self.opcion = opcion
        self.ejemplo = ejemplo
        self.respuesta = respuesta


intenciones = [
    Intenciones(
        "pedidos_japón",
        "1",
        [
            "Pedidos a Japón",
            "Encargo a Japon",
            "Orden a Japon",
            "como hago mi pedido a Japon",
            "cotizaciones Japon",
            "como se hacen los encargos a Japón",
            "quiero hacer pedido Mercari Japón"
            "quiero comprar en Mercari Japón",
            "como se hace un pedido a Mercari Japón",
        ],
        "Para pedir a Japón se necesita que el cliente elija \n"
        "el producto en la página de Mercari Japón y enviar \n"
        "el link al grupo de Mercari Japón, así se cotiza \n" 
        "el precio y el cliente confirma realizar el pedido"
    ),

    Intenciones(
        "pedidos_corea",
        "2",
        [
            "Pedidos a Corea",
            "Encargo a Corea",
            "Orden a Corea",
            "como hago mi pedido a Corea",
            "cotizaciones Corea",
            "como se hacen los encargos a Corea",
            "quiero hacer pedido Mercari Corea",
            "quiero comprar en Mercari Corea",
            "como se hace un pedido a Mercari Corea"
        ],
        "Para pedir a Corea se necesita que el cliente elija \n"
        "el producto en la página de Mercari Corea y enviar \n"
        "el link al grupo de Mercari Corea, así se cotiza \n" 
        "el precio y el cliente confirma realizar el pedido"

    ),

    Intenciones(
        "pagos_aduana_ems",
        "3",
        [
            "Pagos EMS",
            "Pagos Aduana",
            "Pagos Aduana y EMS",
            "como son los pagos de envio",
            "como hago el pago de aduana",
            "como hago el pago de ems",
            "como hago el pago de aduana y ems",
            "como son los pagos de ems y aduana"
        ],
        "Los pagos de aduana y EMS se realizan de la siguiente manera \n"
        "mediante la cuenta banco azteca, escribiendo como concepto \n"
        "tu nombre y ADUANA/EMS, después se realiza el formulario y \n"
        "se mandan las capturas en el grupo EMS y Aduana"
    ),

    Intenciones(
        "formulario_comprobante",
        "4",
        [
            "donde se encuentra el formulario",
            "como lleno el formulario",
            "formulario",
            "comprobante",
            "formulario y comprobante",
            "donde hago el formulario",
            "cual es el comprobante",
            "donde mando el comprobante",
            "datos para el comprobante",
            "informacion del comprobante"
        ],
        "Los links de cada formulario se encuentran en la \n"
        "descripción del grupo, el comprobante se tiene \n" 
        "que mandar a grupo de Pagos o Aduana y EMS, \n" 
        "con tu nombre y lo que pediste: "
    ),

    Intenciones(
        "envio_domicilio",
        "5",
        [
            "como es el envio a domicilio",
            "cuanto tarda en llegar mi pedido",
            "cuanto cuesta el envio a domicilio",
            "que paqueteria utilizas"
        ],
        "Se debe de cotizar el envió de domicilio \n"
        "solamente cuando se abra la fecha, la cual \n"
        "se estará indicando en el grupo general \n"
    ),

    Intenciones(
        "atencion_personalizada",
        "6",
        [
            "quiero que me atienda una persona",
            "atencion personalizada",
            "servicio al cliente",
            "necesito que una persona me atienda"
        ],
        "Te ayudare a contactar con una persona de atencion al cliente."
    ),

    Intenciones(
        "restricciones",
        "7",
        [
            "restricciones",
            "muestrame las restricciones",
            "quiero conocer las restricciones",
            "cuales son las restricciones"
        ],
        "Estas son las restricciones que debes consultar antes de realizar tu pedido: \n"
        "-No nos hacemos responsables por compras en otro grupo. \n"
        "-Pagos que no se hagan a las cuentas indicadas no serán tomados en cuenta \n"
        "-No se aceptan reventas, bajo ninguna circustancia. \n"
        "-Se vetara sin reembolso a quien robe referencias o venda mercancia como propia."
    )
]
