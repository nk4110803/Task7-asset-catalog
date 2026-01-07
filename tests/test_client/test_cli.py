import pytest
from unittest.mock import patch, MagicMock
from typer.testing import CliRunner
from client.cli import app

runner = CliRunner()
@patch("client.cli.Watcher.start") 
def test_cli_runs_without_error(mock_start, tmp_path):
    mock_start.return_value = None

    result = runner.invoke(app, [str(tmp_path)])

    assert result.exit_code == 0
    mock_start.assert_called_once()

@patch("client.cli.Watcher")
def test_run_creates_and_starts_watcher(mock_watcher_class, tmp_path):
    mock_watcher_instance = mock_watcher_class.return_value

    result = runner.invoke(app, [str(tmp_path)])
    mock_watcher_class.assert_called_once()
    mock_watcher_instance.start.assert_called_once()
    assert result.exit_code == 0