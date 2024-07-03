"""
    File to define CRUD interface for our DB.
"""


from abc import ABC, abstractmethod
from typing import Union


class CRUDInterface(ABC):
    """A general interface for CRUD operations."""

    @abstractmethod
    def create_document(self, kind: str, doc_id: str, data: dict) -> None:
        """Creates a document (entity) in the specified kind.

        Args:
            kind (str): The kind of the entity.
            doc_id (str): The ID of the document.
            data (dict): The data to be stored in the document.
        """
        raise NotImplementedError("create_document method is not implemented")

    @abstractmethod
    def read_document(self, kind: str, doc_id: str) -> Union[dict, None]:
        """Reads a document (entity) from the specified kind.

        Args:
            kind (str): The kind of the entity.
            doc_id (str): The ID of the document.

        Returns:
            Union[dict, None]: The data of the document if it exists, None otherwise.
        """
        raise NotImplementedError("read_document method is not implemented")

    @abstractmethod
    def update_document(self, kind: str, doc_id: str, data: dict) -> None:
        """Updates a document (entity) in the specified kind.

        Args:
            kind (str): The kind of the entity.
            doc_id (str): The ID of the document.
            data (dict): The new data to be stored in the document.
        """
        raise NotImplementedError("update_document method is not implemented")

    @abstractmethod
    def delete_document(self, kind: str, doc_id: str) -> None:
        """Deletes a document (entity) from the specified kind.

        Args:
            kind (str): The kind of the entity.
            doc_id (str): The ID of the document.
        """
        raise NotImplementedError("delete_document method is not implemented")

    @abstractmethod
    def read_all_documents(self, kind: str) -> dict[str, dict]:
        """Reads all documents (entities) in the specified kind.

        Args:
            kind (str): The kind of the entities.

        Returns:
            dict[str, dict]: A dictionary with document IDs as keys and their data as values.
        """
        raise NotImplementedError(
            "read_all_documents method is not implemented")

    @abstractmethod
    def add_kind(self, kind: str, doc_id: str, data: dict) -> None:
        """Adds a new kind by creating a document (entity) in that kind.

        Args:
            kind (str): The kind of the new entity.
            doc_id (str): The ID of the document.
            data (dict): The data to be stored in the document.
        """
        raise NotImplementedError("add_kind method is not implemented")
