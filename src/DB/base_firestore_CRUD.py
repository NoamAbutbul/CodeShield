"""
    file to define CRUD for our DB.
"""


from dotenv import load_dotenv
from google.cloud import datastore
from google.cloud.datastore.client import Client
import os
from typing import Union
from src.DB import CRUDInterface


class BaseDatastoreCRUD(CRUDInterface):
    """A class to perform CRUD operations on Google Cloud Datastore.

    Attributes:
        client (datastore.Client): The Datastore client.
    """

    def __init__(self, project_id: str) -> None:
        """Initializes the BaseDatastoreCRUD with a Google Cloud project ID.

        Args:
            project_id (str): The Google Cloud project ID.
        """
        self.__client: Client = datastore.Client(project_id)

    def create_document(self, kind: str, doc_id: str, data: dict) -> None:
        """Creates a document (entity) in the specified kind.

        Args:
            kind (str): The kind of the entity.
            doc_id (str): The ID of the document.
            data (dict): The data to be stored in the document.
        """
        key = self.__client.key(kind, doc_id)
        entity = datastore.Entity(key=key)
        entity.update(data)
        self.__client.put(entity)
        print(f'Document {doc_id} in kind {kind} created successfully.')

    # type: ignore
    def read_document(self, kind: str, doc_id: str) -> Union[dict, None]:
        """Reads a document (entity) from the specified kind.

        Args:
            kind (str): The kind of the entity.
            doc_id (str): The ID of the document.

        Returns:
            Union[dict, None]: The data of the document if it exists, None otherwise.
        """
        key = self.__client.key(kind, doc_id)
        entity = self.__client.get(key)
        if entity:
            print(f'Document data: {dict(entity)}')
            return dict(entity)
        else:
            print('No such document!')
            return None

    def update_document(self, kind: str, doc_id: str, data: dict) -> None:
        """Updates a document (entity) in the specified kind.

        Args:
            kind (str): The kind of the entity.
            doc_id (str): The ID of the document.
            data (dict): The new data to be stored in the document.
        """
        key = self.__client.key(kind, doc_id)
        entity = self.__client.get(key)
        if entity:
            entity.update(data)
            self.__client.put(entity)
            print(f'Document {doc_id} in kind {kind} updated successfully.')
        else:
            print('No such document!')

    def delete_document(self, kind: str, doc_id: str) -> None:
        """Deletes a document (entity) from the specified kind.

        Args:
            kind (str): The kind of the entity.
            doc_id (str): The ID of the document.
        """
        key = self.__client.key(kind, doc_id)
        self.__client.delete(key)
        print(f'Document {doc_id} in kind {kind} deleted successfully.')

    def read_all_documents(self, kind: str) -> dict[str, dict]:
        """Reads all documents (entities) in the specified kind.

        Args:
            kind (str): The kind of the entities.

        Returns:
            dict[str, dict]: A dictionary with document IDs as keys and their data as values.
        """
        query = self.__client.query(kind=kind)
        results = list(query.fetch())
        all_docs = {entity.key.name: dict(entity) for entity in results}
        print(f'All documents in kind {kind}: {all_docs}')
        return all_docs

    def add_kind(self, kind: str, doc_id: str, data: dict) -> None:
        """Adds a new kind by creating a document (entity) in that kind.

        Args:
            kind (str): The kind of the new entity.
            doc_id (str): The ID of the document.
            data (dict): The data to be stored in the document.
        """
        self.create_document(kind, doc_id, data)


# Example usage
if __name__ == "__main__":
    load_dotenv()
    project_id = os.getenv('PROJECT_GOOGLE_ID')

    datastore_crud = BaseDatastoreCRUD(project_id)

    # Add a new kind (like adding a new collection in Firestore)
    kind = 'NewKind'
    doc_id = 'doc0'
    data = {'name': 'Example Name', 'value': 'Example Value'}

    datastore_crud.add_kind(kind, doc_id, data)

    # Verify the new kind and document
    datastore_crud.read_document(kind, doc_id)
