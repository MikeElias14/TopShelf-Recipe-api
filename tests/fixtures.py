import os
import tempfile
import pytest


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


