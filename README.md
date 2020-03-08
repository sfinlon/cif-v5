# Getting Started

## Docker
```bash
$ export CSIRTG_TOKEN=1234  # sign up at csirtg.io
$ export MAXMIND_USERID=1234  # sign up at maxmind.com
$ export MAXMIND_LIC=1234

$ git clone https://github.com/csirtgadgets/cif-v5.git
$ mkdir data  # shared data directory for containers
$ cp cif-v5/docker-compose.yml ./
$ docker-compose pull
$ docker-compose up -d

$ docker-compose logs -f
```

## Testing
```bash
$ pip install 'cifsdk>=5.0b1,<6.0'

$ export CIF_REMOTE='http://localhost:5000'
$ cif -nq example.com 
```

# What's Changed?

* Less. Stuff. 
* Abstracted a lot of the technical pieces into separate libraries (eg: csirtg-geo, csirtg-peers, etc)
* Codebase has been significantly simplified
* **NO TOKENS**, YOU ARE RESPONSIBLE FOR PROTECTING YOUR NODES!!!
* Pipelines and better Plugin support for "external enrichment"
* Docker Compose is the first class citizen, feel free to customize from there
* Docker containers are now split up, not running as supervisord anymore
* cif-httpd is significantly simpler to interact with, improved REST doc (openapi)
* New threat intel rules
* Python 3.7+ support

# Building Locally
```bash
$ git clone https://github.com/csirtgadgets/cif-v5.git
$ cd cif-v5/
$ make docker
$ make docker-tag
$ docker-compose up -d
$ docker-compose logs -f
```

## Architecture

```
                                                              cif-enricher
                                                               ^        +
                                                               |        |
                                                               +        v
csirtg-fm +--> cifsdk  +--------->  cif-httpd +------------> cif-router +-----> cif-store +-----> sqlite
                                                               +
                                           ^                   |        ^
                                           |                   |        |
                                           |                   v        +
                                           |                   cif-hunter
                                           +

                                        cifsdk
```

# Getting Involved
There are many ways to get involved with the project. If you have a new and exciting feature, or even a simple bugfix, simply [fork the repo](https://help.github.com/articles/fork-a-repo), create some simple test cases, [generate a pull-request](https://help.github.com/articles/using-pull-requests) and give yourself credit!

If you've never worked on a GitHub project, [this is a good piece](https://guides.github.com/activities/contributing-to-open-source) for getting started.

* [How To Contribute](contributing.md)  
* [Project Page](http://csirtgadgets.com/collective-intelligence-framework/)

# COPYRIGHT AND LICENSE

Copyright (C) 2020 [the CSIRT Gadgets](http://csirtgadgets.com)

Free use of this software is granted under the terms of the [Mozilla Public License (MPLv2)](https://www.mozilla.org/en-US/MPL/2.0/).
