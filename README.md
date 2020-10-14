# MyServerTemplates

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
[![GitHub release](https://img.shields.io/github/release/Bundabrg/MyServerTemplates)](https://GitHub.com/Bundabrg/MyServerTemplates/releases/)
[![GitHub commits](https://img.shields.io/github/commits-since/Bundabrg/MyServerTemplates/latest)](https://GitHub.com/Bundabrg/MyServerTemplates/commit/)
[![Github all releases](https://img.shields.io/github/downloads/Bundabrg/MyServerTemplates/total.svg)](https://GitHub.com/Bundabrg/MyServerTemplates/releases/)
<!-- ![HitCount](http://hits.dwyl.com/bundabrg/MyServerTemplates.svg) -->

![Workflow](https://github.com/bundabrg/MyServerTemplates/workflows/build/badge.svg)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Bundabrg/MyServerTemplates/graphs/commit-activity)
[![GitHub contributors](https://img.shields.io/github/contributors/Bundabrg/MyServerTemplates)](https://GitHub.com/Bundabrg/MyServerTemplates/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/Bundabrg/MyServerTemplates)](https://GitHub.com/Bundabrg/MyServerTemplates/issues/)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/Bundabrg/MyServerTemplates.svg)](http://isitmaintained.com/project/Bundabrg/MyServerTemplates "Average time to resolve an issue")
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/Bundabrg/MyServerTemplates)](https://GitHub.com/Bundabrg/MyServerTemplates/pull/)
 

---

[**Documentation**](https://bundabrg.github.io/MyServer/)

[**Source Code**](https://github.com/bundabrg/MyServerTemplates/)

---

[MyServer](https://github.com/bundabrg/Myserver) is a server management tool that allows both administrators and
users to create and manage servers under Bungeecord. The definitions of these servers are provided by template files
which can be pulled from a hosted repository.

This is the official repository of MyServer though you can easily fork it and host your own copies. Templates must be
built into a repository format which the `build.py` script provides.

The following repositories are provided:
  * [https://bundabrg.github.io/MyServerTemplates/stable](https://bundabrg.github.io/MyServerTemplates/stable) - This will 
  always point to the latest stable release and should generally be safe to use
  * [https://bundabrg.github.io/MyServerTemplates/development](https://bundabrg.github.io/MyServerTemplates/development) - 
  This will always point to the current development templates for those who like to live on the edge
  * `https://bundabrg.github.io/MyServerTemplates/vX.Y.Z` - Each release of templates will have a version number. If you prefer to
  stick to a particular version then replace `X.Y.Z` with the release version

## Quick Start

* Edit your `config.yml` in the [MyServer](https://github.com/bundabrg/Myserver) folder in your plugins folder and add the
repository of your choice under repositories. You can add more than one if there are other published repositories.

Example
```
# Don't touch
version: 1

folder:
  # Template folder
  templates: templates

  # Cache folder
  cache: cache
  
  # Instances folder
  instances: instances

# Template Repositories
repositories:
  - https://bundabrg.github.io/MyServerTemplates/stable

# Server Config
bungeecord:
  ip-listen: 127.0.0.1

  # Start of Dynamic Ports
  port-start: 26000

  # How many ports to reserve
  port-amount: 1000

```
