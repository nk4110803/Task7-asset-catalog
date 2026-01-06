from unittest.mock import patch
import pytest
from typer.testing import CliRunner
from client.cli import app

runner=CliRunner()
def test_cli_runs_without_eror():
    result=runner.invoke(app, ["run","/tmp"])
    assert result.exit_code==0
    
@patch("client.watcher")
def test_run_creates_and_starts_watcher(mock_watcher):
    result=runner.invoke(app, ["run","/tmp"])
    mock_watcher.assert_called_once()
    mock_watcher.return_value.start.assert_called_once()
    assert result.exit_code == 0
