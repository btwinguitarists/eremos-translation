#!/usr/bin/env python3
"""Build the public portable plugin reproducibly, without local configuration."""
from pathlib import Path
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'mcp' / 'plugin'
FILES = ('plugin.json', 'mcp.json', 'skills/quote-eremos/SKILL.md', 'assets/icon.png')


def build(destination: Path | None = None) -> Path:
    manifest = json.loads((SOURCE / 'plugin.json').read_text())
    config = json.loads((SOURCE / 'mcp.json').read_text())
    server = config['mcpServers']['eremos-bible']
    assert server['type'] == 'streamable-http'
    assert server['url'] == 'https://mcp.eremosapp.com/mcp'
    assert 'headers' not in server and 'extensions' not in server
    destination = destination or ROOT / 'mcp' / 'dist'
    destination.mkdir(parents=True, exist_ok=True)
    archive = destination / f"{manifest['name']}-{manifest['version']}.zip"
    checksums = []
    for openai in (False, True):
        target = archive.with_stem(archive.stem + '-openai') if openai else archive
        with zipfile.ZipFile(target, 'w', compression=zipfile.ZIP_DEFLATED) as output:
            for name in FILES:
                data = (SOURCE / name).read_bytes()
                if openai and name == 'mcp.json':
                    extended = json.loads(data)
                    extended['mcpServers']['eremos-bible']['extensions'] = {
                        'com.openai': {'auth': {'type': 'none'}}}
                    data = (json.dumps(extended, indent=2) + '\n').encode()
                info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                output.writestr(info, data)
        digest = hashlib.sha256(target.read_bytes()).hexdigest()
        checksums.append(f'{digest}  {target.name}\n')
    (destination / 'SHA256SUMS').write_text(''.join(checksums))
    return archive


if __name__ == '__main__':
    print(build())
