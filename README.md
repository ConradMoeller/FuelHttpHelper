# FuelHttpHelper
Automatically uploads files to a Trilith FuelHttpServer

# Assumptions
- Trilith FuelHttpServer is running with basic authentication enabled through a `services`-Subdomain
- At least one FuelHttpReader is running behind the FuelHttpServer
- By default, four FuelHttpReaders are expected to be running with these channel Ids:
  - `lastgang-csv`
  - `lastgang-mscons`
  - `lastgang-xml`
  - `stammdaten-csv`

# Usage
1. Run `python3 FuelHttpHelper.py` and follow the instructions.
2. A `FuelHttpHelper.ini` will be created in the same directory as the script.
3. You must fill in the following parameters:
   - `domain`: The domain of your Trilith Synergy instance (excluding the `https://` or `services.` part)
   - `user`: The username supplied to you by Business Intelligence GmbH
   - `password`: The password supplied to you by Business Intelligence GmbH

_Optionally you can set these additional values:_

- `interval`: If you want to upload files automatically set this to your desired interval in minutes (0 means disabled)
- `delete`: If you want to delete files after they have been uploaded set this to `True` (this is the default behavior),
            `False` to disable, though you rarely want to send the same file twice.
- `channels`: Pipe `|` seprarated list of folders to scan for files to upload.

# Distribution

Pushes to `main` will trigger a release through GitHub Actions, including a Windows Executable bundled by `pyinstaller`
