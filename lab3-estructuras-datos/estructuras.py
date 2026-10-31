"""Lista enlazada y tabla hash para consultar guias de envio."""


class Nodo:
    """Nodo de una lista enlazada que guarda una guia y su estado."""

    def __init__(self, guia: int, estado: str) -> None:
        """Crea un nodo sin siguiente.

        Args:
            guia: numero de guia del envio.
            estado: estado actual del envio.
        """
        self.guia = guia
        self.estado = estado
        self.siguiente: Nodo | None = None


class ListaEnlazada:
    """Lista simplemente enlazada de guias, con insercion al inicio."""

    def __init__(self) -> None:
        """Crea una lista vacia."""
        self.cabeza: Nodo | None = None
        self.tamano = 0

    def insertar(self, guia: int, estado: str) -> None:
        """Agrega una guia al inicio de la lista.

        Args:
            guia: numero de guia del envio.
            estado: estado actual del envio.
        """
        nodo = Nodo(guia, estado)
        nodo.siguiente = self.cabeza
        self.cabeza = nodo
        self.tamano = self.tamano + 1

    def buscar(self, guia: int) -> str | None:
        """Busca una guia recorriendo la lista.

        Args:
            guia: numero de guia a buscar.

        Returns:
            El estado del envio, o None si la guia no existe.
        """
        nodo = self.cabeza
        while nodo is not None and nodo.guia != guia:
            nodo = nodo.siguiente
        if nodo is None:
            return None
        return nodo.estado
