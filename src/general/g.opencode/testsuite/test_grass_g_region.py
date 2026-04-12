"""
Test suite for grass_g_region tool using pytest.

This module tests the grass_g_region.py script functionality.
"""

import pytest
import sys
import os
import importlib.util
from unittest.mock import patch, MagicMock

# Load the grass_g_region module directly
tool_path = os.path.join(os.path.dirname(__file__), "..", ".opencode", "tool")
sys.path.insert(0, tool_path)

spec = importlib.util.spec_from_file_location(
    "grass_g_region", os.path.join(tool_path, "grass_g_region.py")
)
if spec is not None:
    grass_g_region = importlib.util.module_from_spec(spec)
    sys.modules["grass_g_region"] = grass_g_region
    spec.loader.exec_module(grass_g_region)
    importlib.reload(grass_g_region)


class TestGrassGRegion:
    """Test class for grass_g_region functionality."""

    def test_main_with_insufficient_args(self):
        """Test that main exits with error when insufficient arguments provided."""
        with patch("builtins.print") as mock_print:
            # Set up sys.argv with insufficient args
            original_argv = sys.argv.copy()
            sys.argv = ["grass_g_region.py"]  # Only 1 arg, should fail

            try:
                with pytest.raises(SystemExit) as exc_info:
                    grass_g_region.main()
                assert exc_info.value.code == 1
                # Should print usage message
                assert mock_print.call_count >= 1
            finally:
                sys.argv = original_argv

    def test_main_with_valid_args_mock_grass(self):
        """Test main function with valid arguments and mocked GRASS."""
        with (
            patch("subprocess.run") as mock_subprocess,
            patch("platform.system", return_value="Linux"),
            patch("os.path.exists", return_value=True),
            patch("builtins.print") as mock_print,
        ):
            # Mock successful subprocess.run result
            mock_result = MagicMock()
            mock_result.returncode = 0
            mock_result.stdout = "north: 100\nsouth: 0\neast: 200\nwest: 0\n"
            mock_result.stderr = ""
            mock_subprocess.return_value = mock_result

            # Set up sys.argv with correct paths for this test environment
            original_argv = sys.argv.copy()
            sys.argv = [
                "grass_g_region.py",
                "/usr/lib/grass84",
                "/home/sampson/grassdata",
                "Sample_Python_Addon",
                "PERMANENT",
                "p",
                "raw_text",
            ]

            try:
                grass_g_region.main()
                # Verify subprocess was called correctly
                mock_subprocess.assert_called_once()
                args, kwargs = mock_subprocess.call_args
                cmd = args[0]
                assert cmd[0:3] == [
                    "grass",
                    "/home/sampson/grassdata/Sample_Python_Addon/PERMANENT",
                    "--exec",
                ]
                assert "g.region" in cmd
                assert "-p" in cmd
                # Check JSON output format
                mock_print.assert_called_once()
                import json

                output = json.loads(mock_print.call_args[0][0])
                assert output["mode"] == "query"
                assert "north: 100" in output["output"]
                assert "south: 0" in output["output"]
            finally:
                sys.argv = original_argv

    def test_main_with_invalid_location(self):
        """Test that main returns JSON error when location path does not exist."""

        def mock_exists(path):
            # Return True for GISBASE, False for invalid location
            return path == "/usr/lib/grass84" or not path.endswith("invalid_project")

        with (
            patch("os.path.exists", side_effect=mock_exists),
            patch("builtins.print") as mock_print,
        ):
            original_argv = sys.argv.copy()
            sys.argv = [
                "grass_g_region.py",
                "/usr/lib/grass84",
                "/home/sampson/grassdata",
                "invalid_project",
                "PERMANENT",
                "p",
                "raw_text",
            ]

            try:
                grass_g_region.main()
                # Should print JSON error message
                mock_print.assert_called_once()
                import json

                output = json.loads(mock_print.call_args[0][0])
                assert output["mode"] == "query"
                assert "GRASS location does not exist" in output["output"]
            finally:
                sys.argv = original_argv

    def test_main_with_invalid_mapset(self):
        """Test that main returns JSON error when mapset path does not exist."""

        def mock_exists(path):
            # Return True for GISBASE and location, False for invalid mapset
            return (
                path == "/usr/lib/grass84"
                or path == "/home/sampson/grassdata/Sample_Python_Addon"
                or (path.endswith("PERMANENT") and "invalid_mapset" not in path)
            )

        with (
            patch("os.path.exists", side_effect=mock_exists),
            patch("builtins.print") as mock_print,
        ):
            original_argv = sys.argv.copy()
            sys.argv = [
                "grass_g_region.py",
                "/usr/lib/grass84",
                "/home/sampson/grassdata",
                "Sample_Python_Addon",
                "invalid_mapset",
                "p",
                "raw_text",
            ]

            try:
                grass_g_region.main()
                # Should print JSON error message
                mock_print.assert_called_once()
                import json

                output = json.loads(mock_print.call_args[0][0])
                assert output["mode"] == "query"
                assert "Mapset does not exist" in output["output"]
            finally:
                sys.argv = original_argv

    def test_main_with_json_output(self):
        """Test main function with JSON output format."""
        with (
            patch("subprocess.run") as mock_subprocess,
            patch("os.path.exists", return_value=True),
            patch("builtins.print") as mock_print,
        ):
            # Mock successful subprocess.run result
            mock_result = MagicMock()
            mock_result.returncode = 0
            mock_result.stdout = "north: 100\nsouth: 0\n"
            mock_result.stderr = ""
            mock_subprocess.return_value = mock_result

            original_argv = sys.argv.copy()
            sys.argv = [
                "grass_g_region.py",
                "/usr/lib/grass84",
                "/home/sampson/grassdata",
                "Sample_Python_Addon",
                "PERMANENT",
                "p",
                "json",
            ]

            try:
                grass_g_region.main()
                # JSON output should be compact (no indentation)
                mock_print.assert_called_once()
                import json

                output = json.loads(mock_print.call_args[0][0])
                assert output["mode"] == "query"
                assert output["output"]["north"] == "100"
                assert output["output"]["south"] == "0"
            finally:
                sys.argv = original_argv

    def test_main_with_unknown_output_format(self):
        """Test main function with unknown output format."""
        with (
            patch("subprocess.run") as mock_subprocess,
            patch("os.path.exists", return_value=True),
            patch("builtins.print") as mock_print,
        ):
            # Mock successful subprocess.run result to reach format check
            mock_result = MagicMock()
            mock_result.returncode = 0
            mock_result.stdout = "mock output"
            mock_result.stderr = ""
            mock_subprocess.return_value = mock_result

            original_argv = sys.argv.copy()
            sys.argv = [
                "grass_g_region.py",
                "/usr/lib/grass84",
                "/home/sampson/grassdata",
                "Sample_Python_Addon",
                "PERMANENT",
                "p",
                "unknown",
            ]

            try:
                grass_g_region.main()
                # Should return JSON error for unknown format
                mock_print.assert_called_once()
                import json

                output = json.loads(mock_print.call_args[0][0])
                assert output["mode"] == "query"
                assert "Unknown output format" in output["output"]
            finally:
                sys.argv = original_argv

    def test_main_with_3d_flags(self):
        """Test main function with 3D print flags (-p3)."""
        with (
            patch("subprocess.run") as mock_subprocess,
            patch("os.path.exists", return_value=True),
            patch("builtins.print") as mock_print,
        ):
            # Mock 3D output
            mock_result = MagicMock()
            mock_result.returncode = 0
            mock_result.stdout = "projection: 0 (x,y)\nzone: 0\nnorth: 1\nsouth: 0\nwest: 0\neast: 1\ntop: 1.00000000\nbottom: 0.00000000\nnsres: 1\nnsres3: 1\newres: 1\newres3: 1\ntbres: 1\nrows: 1\nrows3: 1\ncols: 1\ncols3: 1\ndepths: 1\ncells: 1\ncells3: 1\n"
            mock_result.stderr = ""
            mock_subprocess.return_value = mock_result

            original_argv = sys.argv.copy()
            sys.argv = [
                "grass_g_region.py",
                "/usr/lib/grass84",
                "/home/sampson/grassdata",
                "Sample_Python_Addon",
                "PERMANENT",
                "p3",
                "raw_text",
            ]

            try:
                grass_g_region.main()
                # Verify subprocess was called with -p and -3
                mock_subprocess.assert_called_once()
                args, kwargs = mock_subprocess.call_args
                cmd = args[0]
                assert "-p" in cmd
                assert "-3" in cmd
                # Check JSON output
                mock_print.assert_called_once()
                import json

                output = json.loads(mock_print.call_args[0][0])
                assert output["mode"] == "query"
                assert "projection: 0 (x,y)" in output["output"]
                assert "top: 1.00000000" in output["output"]
            finally:
                sys.argv = original_argv

    def test_main_with_shell_style_flags(self):
        """Test main function with shell style flags (-g)."""
        with (
            patch("subprocess.run") as mock_subprocess,
            patch("os.path.exists", return_value=True),
            patch("builtins.print") as mock_print,
        ):
            # Mock shell style output
            mock_result = MagicMock()
            mock_result.returncode = 0
            mock_result.stdout = (
                "n=1\ns=0\nw=0\ne=1\nnsres=1\newres=1\nrows=1\ncols=1\n"
            )
            mock_result.stderr = ""
            mock_subprocess.return_value = mock_result

            original_argv = sys.argv.copy()
            sys.argv = [
                "grass_g_region.py",
                "/usr/lib/grass84",
                "/home/sampson/grassdata",
                "Sample_Python_Addon",
                "PERMANENT",
                "g",
                "raw_text",
            ]

            try:
                grass_g_region.main()
                # Verify subprocess was called with -g
                mock_subprocess.assert_called_once()
                args, kwargs = mock_subprocess.call_args
                cmd = args[0]
                assert "-g" in cmd
                # Check JSON output
                mock_print.assert_called_once()
                import json

                output = json.loads(mock_print.call_args[0][0])
                assert output["mode"] == "query"
                assert "n=1" in output["output"]
                assert "s=0" in output["output"]
            finally:
                sys.argv = original_argv

    def test_main_with_lat_long_flags(self):
        """Test main function with lat/long flags (-l)."""
        with (
            patch("subprocess.run") as mock_subprocess,
            patch("os.path.exists", return_value=True),
            patch("builtins.print") as mock_print,
        ):
            # Mock lat/long output
            mock_result = MagicMock()
            mock_result.returncode = 0
            mock_result.stdout = "long: -103.86789484 lat: 44.50165890 (north/west corner)\nlong: -103.62895703 lat: 44.49904013 (north/east corner)\nlong: -103.63190061 lat: 44.37303558 (south/east corner)\nlong: -103.87032572 lat: 44.37564292 (south/west corner)\nrows: 1\ncols: 1\n"
            mock_result.stderr = ""
            mock_subprocess.return_value = mock_result

            original_argv = sys.argv.copy()
            sys.argv = [
                "grass_g_region.py",
                "/usr/lib/grass84",
                "/home/sampson/grassdata",
                "Sample_Python_Addon",
                "PERMANENT",
                "l",
                "raw_text",
            ]

            try:
                grass_g_region.main()
                # Verify subprocess was called with -l
                mock_subprocess.assert_called_once()
                args, kwargs = mock_subprocess.call_args
                cmd = args[0]
                assert "-l" in cmd
                # Check JSON output
                mock_print.assert_called_once()
                import json

                output = json.loads(mock_print.call_args[0][0])
                assert output["mode"] == "query"
                assert "long: -103.86789484" in output["output"]
            finally:
                sys.argv = original_argv

    def test_main_with_extent_flags(self):
        """Test main function with extent flags (-e)."""
        with (
            patch("subprocess.run") as mock_subprocess,
            patch("os.path.exists", return_value=True),
            patch("builtins.print") as mock_print,
        ):
            # Mock extent output
            mock_result = MagicMock()
            mock_result.returncode = 0
            mock_result.stdout = "north: 1\nsouth: 0\neast: 1\nwest: 0\n"
            mock_result.stderr = ""
            mock_subprocess.return_value = mock_result

            original_argv = sys.argv.copy()
            sys.argv = [
                "grass_g_region.py",
                "/usr/lib/grass84",
                "/home/sampson/grassdata",
                "Sample_Python_Addon",
                "PERMANENT",
                "e",
                "raw_text",
            ]

            try:
                grass_g_region.main()
                # Verify subprocess was called with -e
                mock_subprocess.assert_called_once()
                args, kwargs = mock_subprocess.call_args
                cmd = args[0]
                assert "-e" in cmd
                # Check JSON output
                mock_print.assert_called_once()
                import json

                output = json.loads(mock_print.call_args[0][0])
                assert output["mode"] == "query"
                assert "north: 1" in output["output"]
            finally:
                sys.argv = original_argv

    def test_main_with_center_flags(self):
        """Test main function with center flags (-c)."""
        with (
            patch("subprocess.run") as mock_subprocess,
            patch("os.path.exists", return_value=True),
            patch("builtins.print") as mock_print,
        ):
            # Mock center output
            mock_result = MagicMock()
            mock_result.returncode = 0
            mock_result.stdout = "Center longitude: 103:44:59.170374W [-103.74977]\nCenter latitude: 44:26:14.439781N [44.43734]\n"
            mock_result.stderr = ""
            mock_subprocess.return_value = mock_result

            original_argv = sys.argv.copy()
            sys.argv = [
                "grass_g_region.py",
                "/usr/lib/grass84",
                "/home/sampson/grassdata",
                "Sample_Python_Addon",
                "PERMANENT",
                "c",
                "raw_text",
            ]

            try:
                grass_g_region.main()
                # Verify subprocess was called with -c
                mock_subprocess.assert_called_once()
                args, kwargs = mock_subprocess.call_args
                cmd = args[0]
                assert "-c" in cmd
                # Check JSON output
                mock_print.assert_called_once()
                import json

                output = json.loads(mock_print.call_args[0][0])
                assert output["mode"] == "query"
                assert "Center longitude" in output["output"]
            finally:
                sys.argv = original_argv

    def test_main_with_multiple_flags(self):
        """Test main function with multiple flags (e.g., 'pg' for -p -g)."""
        with (
            patch("subprocess.run") as mock_subprocess,
            patch("os.path.exists", return_value=True),
            patch("builtins.print") as mock_print,
        ):
            # Mock combined output
            mock_result = MagicMock()
            mock_result.returncode = 0
            mock_result.stdout = "projection: 0 (x,y)\nzone: 0\nnorth: 1\nsouth: 0\nwest: 0\neast: 1\ntop: 1.00000000\nbottom: 0.00000000\nnsres: 1\nnsres3: 1\newres: 1\newres3: 1\ntbres: 1\nrows: 1\nrows3: 1\ncols: 1\ncols3: 1\ndepths: 1\ncells: 1\ncells3: 1\nn=1\ns=0\nw=0\ne=1\nnsres=1\newres=1\nrows=1\ncols=1\n"
            mock_result.stderr = ""
            mock_subprocess.return_value = mock_result

            original_argv = sys.argv.copy()
            sys.argv = [
                "grass_g_region.py",
                "/usr/lib/grass84",
                "/home/sampson/grassdata",
                "Sample_Python_Addon",
                "PERMANENT",
                "pg",
                "raw_text",
            ]

            try:
                grass_g_region.main()
                # Verify subprocess was called with -p and -g
                mock_subprocess.assert_called_once()
                args, kwargs = mock_subprocess.call_args
                cmd = args[0]
                assert "-p" in cmd
                assert "-g" in cmd
                # Check JSON output
                mock_print.assert_called_once()
                import json

                output = json.loads(mock_print.call_args[0][0])
                assert output["mode"] == "query"
                assert "projection: 0 (x,y)" in output["output"]
                assert "n=1" in output["output"]
            finally:
                sys.argv = original_argv

    def test_create_location(self):
        """Test creating a new location with bounds."""
        with (
            patch("subprocess.run") as mock_subprocess,
            patch("os.path.exists", return_value=True),
            patch("builtins.print") as mock_print,
        ):
            # Mock g.proj success
            mock_result1 = MagicMock()
            mock_result1.returncode = 0
            mock_result1.stdout = ""
            mock_result1.stderr = ""
            # Mock g.region success
            mock_result2 = MagicMock()
            mock_result2.returncode = 0
            mock_result2.stdout = ""
            mock_result2.stderr = ""
            mock_subprocess.side_effect = [mock_result1, mock_result2]

            original_argv = sys.argv.copy()
            sys.argv = [
                "grass_g_region.py",
                "create",
                "/usr/lib/grass84",
                "/home/sampson/grassdata",
                "OttawaTest",
                "4326",
                "46",
                "44",
                "-74",
                "-76",
            ]

            try:
                grass_g_region.main()
                # Verify calls
                assert mock_subprocess.call_count == 2
                calls = mock_subprocess.call_args_list
                # First call: g.proj
                cmd1 = calls[0][0][0]
                assert "g.proj" in cmd1
                assert "-c" in cmd1
                assert "epsg=4326" in cmd1
                assert "location=OttawaTest" in cmd1
                # Second call: g.region in new location
                cmd2 = calls[1][0][0]
                assert "g.region" in cmd2
                assert "n=46.0" in cmd2
                assert "s=44.0" in cmd2
                assert "e=-74.0" in cmd2
                assert "w=-76.0" in cmd2
                # Check JSON output
                mock_print.assert_called_once()
                import json

                output = json.loads(mock_print.call_args[0][0])
                assert output["mode"] == "create"
                assert "Location 'OttawaTest' created" in output["output"]
                assert "EPSG 4326" in output["output"]
            finally:
                sys.argv = original_argv

    def test_set_region(self):
        """Test setting region bounds and resolution."""
        with (
            patch("subprocess.run") as mock_subprocess,
            patch("os.path.exists", return_value=True),
            patch("builtins.print") as mock_print,
        ):
            # Mock g.region success
            mock_result = MagicMock()
            mock_result.returncode = 0
            mock_result.stdout = ""
            mock_result.stderr = ""
            mock_subprocess.return_value = mock_result

            original_argv = sys.argv.copy()
            sys.argv = [
                "grass_g_region.py",
                "set",
                "/usr/lib/grass84",
                "/home/sampson/grassdata",
                "Sample_Python_Addon",
                "PERMANENT",
                "46",
                "44",
                "-74",
                "-76",
                "0.01",
            ]

            try:
                grass_g_region.main()
                # Verify call
                mock_subprocess.assert_called_once()
                args, kwargs = mock_subprocess.call_args
                cmd = args[0]
                assert "g.region" in cmd
                assert "n=46.0" in cmd
                assert "s=44.0" in cmd
                assert "e=-74.0" in cmd
                assert "w=-76.0" in cmd
                assert "res=0.01" in cmd
                # Check JSON output
                mock_print.assert_called_once()
                import json

                output = json.loads(mock_print.call_args[0][0])
                assert output["mode"] == "set"
                assert (
                    "Region set to n=46.0 s=44.0 e=-74.0 w=-76.0 res=0.01"
                    == output["output"]
                )
            finally:
                sys.argv = original_argv

    def test_create_ottawa_region(self):
        """Test creating Ottawa region with specific bounds."""
        with (
            patch("subprocess.run") as mock_subprocess,
            patch("os.path.exists", return_value=True),
            patch("builtins.print") as mock_print,
        ):
            # Mock g.proj success
            mock_result1 = MagicMock()
            mock_result1.returncode = 0
            mock_result1.stdout = ""
            mock_result1.stderr = ""
            # Mock g.region success
            mock_result2 = MagicMock()
            mock_result2.returncode = 0
            mock_result2.stdout = ""
            mock_result2.stderr = ""
            mock_subprocess.side_effect = [mock_result1, mock_result2]

            original_argv = sys.argv.copy()
            sys.argv = [
                "grass_g_region.py",
                "create",
                "/usr/lib/grass84",
                "/home/sampson/grassdata",
                "OttawaRegion",
                "4326",
                "46",
                "44",
                "-74",
                "-76",
            ]

            try:
                grass_g_region.main()
                # Check JSON output for Ottawa bounds
                mock_print.assert_called_once()
                import json

                output = json.loads(mock_print.call_args[0][0])
                assert output["mode"] == "create"
                assert "n=46.0 s=44.0 e=-74.0 w=-76.0" in output["output"]
            finally:
                sys.argv = original_argv


if __name__ == "__main__":
    pytest.main([__file__])
