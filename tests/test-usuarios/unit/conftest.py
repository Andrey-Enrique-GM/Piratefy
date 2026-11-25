import pytest


class FakeCursor:
    """A fake cursor that simulates database operations for testing purposes"""
    def __init__(self, result=None, lastrowid=None, error=None):
        self.result = result
        self.lastrowid = lastrowid
        self.error = error
        self.executed_queries = []
        self.executed_params = []
        self.closed = False

    def execute(self, query, params=None):
        if self.error:
            raise self.error
        self.executed_queries.append(query)
        self.executed_params.append(params)

    def fetchone(self):
        return self.result

    def close(self):
        self.closed = True


class FakeConnection:
    """A fake connection that simulates database operations for testing purposes"""
    def __init__(self, cursor):
        self._cursor = cursor
        self.committed = False
        self.closed = False
        self.cursor_options = None

    def cursor(self, *args, **kwargs):
        self.cursor_options = args
        return self._cursor

    def commit(self):
        self.committed = True

    def close(self):
        self.closed = True


@pytest.fixture
def database_connection(monkeypatch):
    """Fixture that provides a fake database connection and cursor for testing purposes"""
    def _database_connection(result=None, lastrowid=None, error=None):
        cursor = FakeCursor(result, lastrowid, error)
        connection = FakeConnection(cursor)
        monkeypatch.setattr(
            "entities.usuario.get_db_connection", lambda: connection
        )
        return connection, cursor

    return _database_connection