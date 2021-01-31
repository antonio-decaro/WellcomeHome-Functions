import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

kv_uri = f"https://wellcomehome-kv.vault.azure.net/"


credential = DefaultAzureCredential()
client = SecretClient(vault_url=kv_uri, credential=credential)


class DefaultConfig:
    # Cognitive Service infos
    COGNITIVE_SERVICES_ENDPOINT = "https://wellcomehome-cs.cognitiveservices.azure.com/"
    COGNITIVE_SERVICES_KEY = client.get_secret('wellcomehome-cs-key').value

    PERSON_GROUP_ID = "015ba04c-7902-40ae-be53-3a0d5c591874"

    # Cosmos DB infos
    COSMOSDB_ENDPOINT = "https://wellcomehome-cosmosdb.documents.azure.com:443/"
    COSMOSDB_KEY = client.get_secret('wellcomehome-db-key').value
    DATABASE_NAME = "WellcomeHomeDB"
    PEOPLE_CONTAINER = "People"
    USERS_CONTAINER = "Users"

    # Blob Storage Info
    STORAGE_CONNECTION = os.environ.get('AZURE_STORAGE_CONNECTION', '')

    # Bot infos
    BOT_NOTIFY_CHANNEL = os.environ['BOT_NOTIFY_CHANNEL']
    BOT_TRUST_TOKEN = client.get_secret('Trust-Token-ProactiveMessages').value


__all__ = ['DefaultConfig']
