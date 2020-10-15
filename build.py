# MIT License
#
# Copyright (c) 2020 MyServer Developers
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import gzip
import hashlib
import json
import re
import shutil
import tarfile
from pathlib import Path

import yaml

# Clear build folder
build_path: Path = Path("build/templates")
shutil.rmtree(build_path, ignore_errors=True)
build_path.mkdir(parents=True, exist_ok=True)
content_path = build_path / "contents"
content_path.mkdir(parents=True, exist_ok=True)

templates = {}

# Find all template.yml files underneath the templates folder
for template_file_path in Path("templates").rglob("template.yml"):
    with open(template_file_path) as template_file:
        template = yaml.full_load(template_file)

        # Make sure template has a name
        if "name" not in template:
            print("Template missing name field: " + str(template_file_path))
            continue

        # Make sure its in the right format
        fullname: str = template.get("name")
        try:
            template_type, template_name, template_version = re.match(r"([^:]+):([^@]+)@(.+)", fullname).groups()
        except ValueError:
            print("Template name is incorrectly formatted: " + fullname)

        print("Found: " + fullname + " in " + str(template_file_path))

        # Compress folder to base64 encoded file
        temp_path = content_path / "~TMP.tgz"
        with tarfile.open(temp_path, "w:gz") as compressed:
            compressed.add(str(template_file_path.parent), arcname="")

        # Calculate sha256
        sha256_hash = hashlib.sha256()
        with temp_path.open("rb") as compressed:
            for byte_block in iter(lambda: compressed.read(4096), b""):
                sha256_hash.update(byte_block)

        # Rename file
        temp_path.rename(content_path / (sha256_hash.hexdigest() + ".tgz"))

        if template_type not in templates:
            templates[template_type] = {}

        if template_name not in templates.get(template_type):
            templates.get(template_type)[template_name] = {}

        templates.get(template_type).get(template_name)[template_version] = sha256_hash.hexdigest()

# Create contents.gz
contents_file = build_path / "contents.gz"
with gzip.open(contents_file, "w") as compressed:
    compressed.write(str(json.dumps({
        "version": 1.0,
        "contents": templates,
    })).encode())

# Calculate sha256 of file
sha256_hash = hashlib.sha256()
with contents_file.open("rb") as compressed:
    for byte_block in iter(lambda: compressed.read(4096), b""):
        sha256_hash.update(byte_block)

# Create release
release_file = build_path / "release"
with release_file.open("w") as output:
    json.dump({
        "version": 1.0,
        "contents_sha": sha256_hash.hexdigest()
    }, output)
