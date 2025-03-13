Digital Marketplace Jinja Macros
=========================

![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)
![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)
![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)
[![PyPI version](https://badge.fury.io/py/ccs-digitalmarketplace-frontend-jinja.svg)](https://badge.fury.io/py/ccs-digitalmarketplace-frontend-jinja)

This repository provides a complete set of [Jinja](https://jinja.palletsprojects.com/) macros that are kept up-to-date and 100% compliant with [CCS Digital Marketplace GOV.UK Frontend](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-govuk-frontend) Nunjucks macros. Porting is intentionally manual rather than automated to make updates simpler than maintaining an automated conversion routine. A comprehensive test suite ensures compliance against the latest, and every subsequent, CCS GOV.UK Frontend Frontend release.

This project was inspired by the [GOV.UK Frontend Jinja Macros](https://github.com/LandRegistry/govuk-frontend-jinja) project by [HM Land Registry](https://github.com/LandRegistry) and we thank them for their work which has helped with this project.

## Compatibility

The following table shows the version of Digital Marketplace Frontend Jinja that you should use for your targeted version of CCS Digital Marketplace GOV.UK Frontend:

| Digital Marketplace Frontend Jinja Version | Target CCS Digital Marketplace GOV.UK Frontend Version |
| ------------------------------------------ | ------------------------------------------------------ |
| [3.7.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-frontend-jinja/releases/tag/3.7.0) | [2.8.1](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-govuk-frontend/releases/tag/v2.8.1) |
| [3.6.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-frontend-jinja/releases/tag/3.6.0) | [2.7.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-govuk-frontend/releases/tag/v2.7.0) |
| [3.5.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-frontend-jinja/releases/tag/3.5.0) | [2.6.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-govuk-frontend/releases/tag/v2.6.0) |
| [3.4.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-frontend-jinja/releases/tag/3.4.0) | [2.4.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-govuk-frontend/releases/tag/v2.4.0) |
| [3.3.1](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-frontend-jinja/releases/tag/3.3.1) | [2.3.1](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-govuk-frontend/releases/tag/v2.3.1) |
| [3.3.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-frontend-jinja/releases/tag/3.3.0) | [2.3.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-govuk-frontend/releases/tag/v2.3.0) |
| [3.2.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-frontend-jinja/releases/tag/3.2.0) | [2.2.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-govuk-frontend/releases/tag/v2.2.0) |
| [3.1.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-frontend-jinja/releases/tag/3.1.0) | [2.1.1](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-govuk-frontend/releases/tag/v2.1.1) |
| [3.0.1](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-frontend-jinja/releases/tag/3.0.1) | [2.0.2](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-govuk-frontend/releases/tag/v2.0.2) |
| [2.10.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-frontend-jinja/releases/tag/2.10.0) | [1.3.1](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-govuk-frontend/releases/tag/v1.3.1) |
| [2.9.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-frontend-jinja/releases/tag/2.9.0) | [1.2.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-govuk-frontend/releases/tag/v1.2.0) |
| [2.8.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-frontend-jinja/releases/tag/2.8.0) | [1.1.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-govuk-frontend/releases/tag/v1.1.0) |
| [2.7.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-frontend-jinja/releases/tag/2.7.0) | [1.0.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-govuk-frontend/releases/tag/v1.0.0) |
| [2.6.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-frontend-jinja/releases/tag/2.6.0) | [6.4.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-govuk-frontend/releases/tag/6.4.0) |
| [2.5.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-frontend-jinja/releases/tag/2.5.0) | [6.3.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-govuk-frontend/releases/tag/6.3.0) |
| [2.2.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-frontend-jinja/releases/tag/2.2.0) | [6.2.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-govuk-frontend/releases/tag/6.2.0) |
| [2.1.1](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-frontend-jinja/releases/tag/2.1.1) | [6.1.1](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-govuk-frontend/releases/tag/6.1.1) |
| [2.1.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-frontend-jinja/releases/tag/2.1.0) | [6.1.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-govuk-frontend/releases/tag/6.1.0) |
| [2.0.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-frontend-jinja/releases/tag/2.0.0) | [6.0.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-govuk-frontend/releases/tag/6.0.0) |
| [1.4.1](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-frontend-jinja/releases/tag/1.4.1) | [5.5.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-govuk-frontend/releases/tag/5.5.0) |
| [1.4.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-frontend-jinja/releases/tag/1.4.0) | [5.5.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-govuk-frontend/releases/tag/5.5.0) |
| [1.3.3](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-frontend-jinja/releases/tag/1.3.3) | [5.4.3](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-govuk-frontend/releases/tag/5.4.3) |
| [1.3.2](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-frontend-jinja/releases/tag/1.3.2) | [5.4.2](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-govuk-frontend/releases/tag/5.4.2) |
| [1.3.1](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-frontend-jinja/releases/tag/1.3.1) | [5.4.1](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-govuk-frontend/releases/tag/5.4.1) |
| [1.3.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-frontend-jinja/releases/tag/1.3.0) | [5.4.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-govuk-frontend/releases/tag/5.4.0) |
| [1.2.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-frontend-jinja/releases/tag/1.2.0) | [5.2.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-govuk-frontend/releases/tag/5.2.0) |
| [1.1.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-frontend-jinja/releases/tag/1.1.0) | [5.2.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-govuk-frontend/releases/tag/5.2.0) |
| [1.0.2](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-frontend-jinja/releases/tag/1.0.2) | [5.1.2](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-govuk-frontend/releases/tag/5.1.2) |
| [1.0.1](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-frontend-jinja/releases/tag/1.0.1) | [5.1.1](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-govuk-frontend/releases/tag/5.1.1) |
| [1.0.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-frontend-jinja/releases/tag/1.0.0) | [5.1.0](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-govuk-frontend/releases/tag/5.1.0) |

Any other versions of CCS Digital Marketplace GOV.UK Frontend not shown above _may_ still be compatible, but have not been specifically tested and verified.

## How to use

After running `pip install ccs-digitalmarketplace-frontend-jinja`, ensure that you tell Jinja where to load the templates from using the `PackageLoader` as follows:

```python
from flask import Flask
from jinja2 import ChoiceLoader, PackageLoader, PrefixLoader

app = Flask(__name__)

app.jinja_loader = ChoiceLoader(
    [
        PackageLoader("app"),
        PrefixLoader(
          {
            "govuk_frontend_jinja": PackageLoader("govuk_frontend_jinja"),
            "digitalmarketplace_frontend_jinja": PackageLoader("digitalmarketplace_frontend_jinja"),
          }
        ),
    ]
)
```

### Calling a Macro in your template

To use a component in your project templates you must import and call the component macro and pass the relevant options, for example:

```html
{%- from 'digitalmarketplace_frontend_jinja/components/alert/macro.html' import digitalmarketplaceAlert -%}

{{ digitalmarketplaceAlert({
    "titleText": "Your application is complete",
    "text": "You still have 3 unsubmitted services",
    "type" : "success"
}) }}
```

The options available to each component macro can be found in the original [CCS Digital Marketplace GOV.UK Frontend](https://github.com/Crown-Commercial-Service/ccs-digitalmarketplace-govuk-frontend/tree/main/packages/digitalmarketplace-frontend/src/digitalmarketplace/components) documentation. Since this project is a like-for-like port, the only difference between the Nunjucks examples and their Jinja equivalents is having to quote key names, e.g. `'text'` instead of `text`.

## Versioning

Releases of this project follow [semantic versioning](http://semver.org/), ie
> Given a version number MAJOR.MINOR.PATCH, increment the:
>
> - MAJOR version when you make incompatible API changes,
> - MINOR version when you add functionality in a backwards-compatible manner, and
> - PATCH version when you make backwards-compatible bug fixes.

To make a new version:
- update the version in the `digitalmarketplace_frontend_jinja/__init__.py` file
- if you are making a major change, also update the change log;

When the pull request is merged a GitHub Action will tag the new version.

## Pre-commit hooks

This project has a [pre-commit hook][pre-commit hook] to do some general file checks and check the `pyproject.toml`.
Follow the [Quick start][pre-commit quick start] to see how to set this up in your local checkout of this project.

## Licence

Unless stated otherwise, the codebase is released under [the MIT License][mit].
This covers both the codebase and any sample code in the documentation.

The documentation is [&copy; Crown copyright][copyright] and available under the terms
of the [Open Government 3.0][ogl] licence.

[mit]: LICENCE
[copyright]: http://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/
[ogl]: http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/

[pre-commit hook]: https://pre-commit.com/
[pre-commit quick start]: https://pre-commit.com/#quick-start
