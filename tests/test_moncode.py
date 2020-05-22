from click.testing import CliRunner

import moncode

def test_main():
    runner = CliRunner()
    result = runner.invoke(moncode.main)
    assert result.exit_code == 0
