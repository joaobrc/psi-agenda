import pytest
from fastapi.testclient import TestClient

from src.psi_agenda.app import app


@pytest.fixture
def cliente():
    with TestClient(app) as client:
        yield client
