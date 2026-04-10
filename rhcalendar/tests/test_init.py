from rhcalendar import networkdays


def test_init():
    assert networkdays


def test_version_fallback(monkeypatch):
    """ When _version.py is missing, __version__ falls back gracefully. """
    import importlib
    import sys
    import rhcalendar
    with monkeypatch.context() as m:
        m.setitem(sys.modules, "rhcalendar._version", None)
        importlib.reload(rhcalendar)
        assert rhcalendar.__version__ == "0.0.0+unknown"
    importlib.reload(rhcalendar)
