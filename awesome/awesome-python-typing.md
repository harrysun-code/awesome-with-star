# Typing

[![GitHub stars](https://img.shields.io/github/stars/typeddjango/awesome-python-typing?style=flat)](https://github.com/typeddjango/awesome-python-typing/stargazers)

# Awesome Python Typing [![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)

Collection of awesome Python types, stubs, plugins, and tools to work with them.

## Contents

- [Static type checkers](#static-type-checkers)
- [Dynamic type checkers](#dynamic-type-checkers)
- [Stub packages](#stub-packages)
- [Additional types](#additional-types)
- [Backports and improvements](#backports-and-improvements)
- [Tools](#tools)
- [Integrations](#integrations)
- [Articles](#articles)
- [Related](#related)

[Full list of typed projects on PyPi](https://pypi.org/search/?q=&o=&c=Typing+%3A%3A+Typed) is here.

## Static type checkers

- [basedmypy](https://github.com/KotlinIsland/basedmypy) [![GitHub stars](https://img.shields.io/github/stars/KotlinIsland/basedmypy?style=flat)](https://github.com/KotlinIsland/basedmypy/stargazers) - Based static typing with baseline functionality.
- [basedpyright](https://github.com/detachhead/basedpyright) [![GitHub stars](https://img.shields.io/github/stars/detachhead/basedpyright?style=flat)](https://github.com/detachhead/basedpyright/stargazers) - Pyright fork with improvements to VSCode support and various other fixes.
- [mypy](https://github.com/python/mypy) [![GitHub stars](https://img.shields.io/github/stars/python/mypy?style=flat)](https://github.com/python/mypy/stargazers) - Optional static typing (PEP 484).
- [pyanalyze](https://github.com/quora/pyanalyze) [![GitHub stars](https://img.shields.io/github/stars/quora/pyanalyze?style=flat)](https://github.com/quora/pyanalyze/stargazers) - Extensible static analyzer and type checker.
- [PyCharm](https://www.jetbrains.com/pycharm/) - IDE for Professional Developers.
- [pylyzer](https://github.com/mtshiba/pylyzer/) [![GitHub stars](https://img.shields.io/github/stars/mtshiba/pylyzer/?style=flat)](https://github.com/mtshiba/pylyzer//stargazers) - A fast static code analyzer & language server for Python, written in Rust.
- [pyrefly](https://github.com/facebook/pyrefly) [![GitHub stars](https://img.shields.io/github/stars/facebook/pyrefly?style=flat)](https://github.com/facebook/pyrefly/stargazers) - A fast type checker and language server for Python.
- [pyright](https://github.com/Microsoft/pyright) [![GitHub stars](https://img.shields.io/github/stars/Microsoft/pyright?style=flat)](https://github.com/Microsoft/pyright/stargazers) - Fast type checker meant for large Python source bases. It can run in a “watch” mode and performs fast incremental updates when files are modified.
- [pycroscope](https://github.com/JelleZijlstra/pycroscope) [![GitHub stars](https://img.shields.io/github/stars/JelleZijlstra/pycroscope?style=flat)](https://github.com/JelleZijlstra/pycroscope/stargazers) - A semi-static type checker for Python code. It imports the modules it type checks, enabling `pycroscope` to understand many dynamic constructs that other type checkers will reject. This makes it possible to extend `pycroscope` with plugins that interact directly with your code.
- [pytype](https://github.com/google/pytype) [![GitHub stars](https://img.shields.io/github/stars/google/pytype?style=flat)](https://github.com/google/pytype/stargazers) - Tool to check and infer types - without requiring type annotations.
- [ty](https://github.com/astral-sh/ty) [![GitHub stars](https://img.shields.io/github/stars/astral-sh/ty?style=flat)](https://github.com/astral-sh/ty/stargazers) - An extremely fast Python type checker, written in Rust, from the creators of Ruff and uv.
- [zuban](https://github.com/zubanls/zuban) [![GitHub stars](https://img.shields.io/github/stars/zubanls/zuban?style=flat)](https://github.com/zubanls/zuban/stargazers) - A Mypy-compatible Python type checker and Language Server built in Rust.

## Dynamic type checkers

- [beartype](https://github.com/beartype/beartype) [![GitHub stars](https://img.shields.io/github/stars/beartype/beartype?style=flat)](https://github.com/beartype/beartype/stargazers) - Unbearably fast `O(1)` runtime type-checking in pure Python.
- [pydantic](https://github.com/samuelcolvin/pydantic) [![GitHub stars](https://img.shields.io/github/stars/samuelcolvin/pydantic?style=flat)](https://github.com/samuelcolvin/pydantic/stargazers) - Data parsing using Python type hinting. Supports dataclasses.
- [pytypes](https://github.com/Stewori/pytypes) [![GitHub stars](https://img.shields.io/github/stars/Stewori/pytypes?style=flat)](https://github.com/Stewori/pytypes/stargazers) - Provides a rich set of utilities for runtime typechecking.
- [strongtyping](https://github.com/FelixTheC/strongtyping) [![GitHub stars](https://img.shields.io/github/stars/FelixTheC/strongtyping?style=flat)](https://github.com/FelixTheC/strongtyping/stargazers) - Decorator which checks whether the function is called with the correct type of parameters.
- [typedpy](https://github.com/loyada/typedpy) [![GitHub stars](https://img.shields.io/github/stars/loyada/typedpy?style=flat)](https://github.com/loyada/typedpy/stargazers) - Type-safe, strict Python. Works well with standard Python.
- [typeguard](https://github.com/agronholm/typeguard) [![GitHub stars](https://img.shields.io/github/stars/agronholm/typeguard?style=flat)](https://github.com/agronholm/typeguard/stargazers) - Another one runtime type checker.
- [typical](https://github.com/seandstewart/typical/) [![GitHub stars](https://img.shields.io/github/stars/seandstewart/typical/?style=flat)](https://github.com/seandstewart/typical//stargazers) - Data parsing and automatic type-coercion using type hinting. Supports dataclasses, standard classes, function signatures, and more.
- [trycast](https://github.com/davidfstr/trycast) [![GitHub stars](https://img.shields.io/github/stars/davidfstr/trycast?style=flat)](https://github.com/davidfstr/trycast/stargazers) - Parse JSON-like values whose shape is defined by typed dictionaries (TypedDicts) and other standard Python type hints.

## Stub packages

- [asgiref](https://github.com/django/asgiref) [![GitHub stars](https://img.shields.io/github/stars/django/asgiref?style=flat)](https://github.com/django/asgiref/stargazers) - ASGI specification, provides [asgiref.typing](https://github.com/django/asgiref/blob/main/asgiref/typing.py) [![GitHub stars](https://img.shields.io/github/stars/django/asgiref/blob/main/asgiref/typing.py?style=flat)](https://github.com/django/asgiref/blob/main/asgiref/typing.py/stargazers) module with type annotations for ASGI servers.
- [boto3-stubs](https://vemel.github.io/boto3_stubs_docs/) - Stubs for [boto3](https://github.com/boto/boto3) [![GitHub stars](https://img.shields.io/github/stars/boto/boto3?style=flat)](https://github.com/boto/boto3/stargazers).
- [botostubs](https://github.com/jeshan/botostubs) [![GitHub stars](https://img.shields.io/github/stars/jeshan/botostubs?style=flat)](https://github.com/jeshan/botostubs/stargazers) - Gives you code assistance for any boto3 API in any IDE.
- [celery-types](https://github.com/sbdchd/celery-types) [![GitHub stars](https://img.shields.io/github/stars/sbdchd/celery-types?style=flat)](https://github.com/sbdchd/celery-types/stargazers) - Type stubs for [Celery](https://github.com/celery/celery) [![GitHub stars](https://img.shields.io/github/stars/celery/celery?style=flat)](https://github.com/celery/celery/stargazers) and its related packages [django-celery-results](https://github.com/celery/django-celery-results) [![GitHub stars](https://img.shields.io/github/stars/celery/django-celery-results?style=flat)](https://github.com/celery/django-celery-results/stargazers), [ampq](https://github.com/celery/py-amqp) [![GitHub stars](https://img.shields.io/github/stars/celery/py-amqp?style=flat)](https://github.com/celery/py-amqp/stargazers), [kombu](https://github.com/celery/kombu) [![GitHub stars](https://img.shields.io/github/stars/celery/kombu?style=flat)](https://github.com/celery/kombu/stargazers), [billiard](https://github.com/celery/billiard) [![GitHub stars](https://img.shields.io/github/stars/celery/billiard?style=flat)](https://github.com/celery/billiard/stargazers), [vine](https://github.com/celery/vine) [![GitHub stars](https://img.shields.io/github/stars/celery/vine?style=flat)](https://github.com/celery/vine/stargazers) and [ephem](https://github.com/brandon-rhodes/pyephem) [![GitHub stars](https://img.shields.io/github/stars/brandon-rhodes/pyephem?style=flat)](https://github.com/brandon-rhodes/pyephem/stargazers).
- [django-stubs](https://github.com/typeddjango/django-stubs) [![GitHub stars](https://img.shields.io/github/stars/typeddjango/django-stubs?style=flat)](https://github.com/typeddjango/django-stubs/stargazers) - Stubs for [Django](https://github.com/django/django) [![GitHub stars](https://img.shields.io/github/stars/django/django?style=flat)](https://github.com/django/django/stargazers).
- [djangorestframework-stubs](https://github.com/typeddjango/djangorestframework-stubs) [![GitHub stars](https://img.shields.io/github/stars/typeddjango/djangorestframework-stubs?style=flat)](https://github.com/typeddjango/djangorestframework-stubs/stargazers) - Stubs for [DRF](https://github.com/encode/django-rest-framework) [![GitHub stars](https://img.shields.io/github/stars/encode/django-rest-framework?style=flat)](https://github.com/encode/django-rest-framework/stargazers).
- [grpc-stubs](https://github.com/shabbyrobe/grpc-stubs) [![GitHub stars](https://img.shields.io/github/stars/shabbyrobe/grpc-stubs?style=flat)](https://github.com/shabbyrobe/grpc-stubs/stargazers) - Stubs for [grpc](https://github.com/grpc/grpc) [![GitHub stars](https://img.shields.io/github/stars/grpc/grpc?style=flat)](https://github.com/grpc/grpc/stargazers).
- [lxml-stubs](https://github.com/lxml/lxml-stubs) [![GitHub stars](https://img.shields.io/github/stars/lxml/lxml-stubs?style=flat)](https://github.com/lxml/lxml-stubs/stargazers) - Stubs for [lxml](https://lxml.de).
- [PyQt5-stubs](https://github.com/stlehmann/PyQt5-stubs) [![GitHub stars](https://img.shields.io/github/stars/stlehmann/PyQt5-stubs?style=flat)](https://github.com/stlehmann/PyQt5-stubs/stargazers) - Stubs for [PyQt5](https://www.riverbankcomputing.com/software/pyqt/intro).
- [python-phonenumbers-stubs](https://github.com/AA-Turner/python-phonenumbers-stubs) [![GitHub stars](https://img.shields.io/github/stars/AA-Turner/python-phonenumbers-stubs?style=flat)](https://github.com/AA-Turner/python-phonenumbers-stubs/stargazers) - Stubs for [phonenumbers](https://github.com/daviddrysdale/python-phonenumbers) [![GitHub stars](https://img.shields.io/github/stars/daviddrysdale/python-phonenumbers?style=flat)](https://github.com/daviddrysdale/python-phonenumbers/stargazers).
- [pythonista-stubs](https://github.com/hbmartin/pythonista-stubs) [![GitHub stars](https://img.shields.io/github/stars/hbmartin/pythonista-stubs?style=flat)](https://github.com/hbmartin/pythonista-stubs/stargazers) - Stubs for [Pythonista](http://omz-software.com/pythonista/docs/ios/).
- [scipy-stubs](https://github.com/jorenham/scipy-stubs) [![GitHub stars](https://img.shields.io/github/stars/jorenham/scipy-stubs?style=flat)](https://github.com/jorenham/scipy-stubs/stargazers) - Stubs for [SciPy](https://github.com/scipy/scipy) [![GitHub stars](https://img.shields.io/github/stars/scipy/scipy?style=flat)](https://github.com/scipy/scipy/stargazers).
- [sqlalchemy-stubs](https://github.com/dropbox/sqlalchemy-stubs) [![GitHub stars](https://img.shields.io/github/stars/dropbox/sqlalchemy-stubs?style=flat)](https://github.com/dropbox/sqlalchemy-stubs/stargazers) - Stubs for [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) [![GitHub stars](https://img.shields.io/github/stars/sqlalchemy/sqlalchemy?style=flat)](https://github.com/sqlalchemy/sqlalchemy/stargazers).
- [sqlalchemy2-stubs](https://docs.sqlalchemy.org/en/14/orm/extensions/mypy.html) - Official stubs and mypy plugin for [SQLAlchemy](https://www.sqlalchemy.org).
- [torchtyping](https://github.com/patrick-kidger/torchtyping) [![GitHub stars](https://img.shields.io/github/stars/patrick-kidger/torchtyping?style=flat)](https://github.com/patrick-kidger/torchtyping/stargazers) - Enhanced type annotations for [PyTorch](https://pytorch.org/).
- [types-aiobotocore](https://vemel.github.io/types_aiobotocore_docs/) - Stubs for [aiobotocore](https://github.com/aio-libs/aiobotocore) [![GitHub stars](https://img.shields.io/github/stars/aio-libs/aiobotocore?style=flat)](https://github.com/aio-libs/aiobotocore/stargazers).
- [typeshed](https://github.com/python/typeshed) [![GitHub stars](https://img.shields.io/github/stars/python/typeshed?style=flat)](https://github.com/python/typeshed/stargazers) - Collection of library stubs, with static types.

## Additional types

- [meiga](https://github.com/alice-biometrics/meiga) [![GitHub stars](https://img.shields.io/github/stars/alice-biometrics/meiga?style=flat)](https://github.com/alice-biometrics/meiga/stargazers) - Simple, typed and monad-based Result type.
- [option](https://github.com/MaT1g3R/option) [![GitHub stars](https://img.shields.io/github/stars/MaT1g3R/option?style=flat)](https://github.com/MaT1g3R/option/stargazers) - Rust like Option and Result types.
- [optype](https://github.com/jorenham/optype) [![GitHub stars](https://img.shields.io/github/stars/jorenham/optype?style=flat)](https://github.com/jorenham/optype/stargazers) - Opinionated `collections.abc` and `operators` alternative: Flexible single-method protocols and typed operators with predictable names.
- [phantom-types](https://github.com/antonagestam/phantom-types) [![GitHub stars](https://img.shields.io/github/stars/antonagestam/phantom-types?style=flat)](https://github.com/antonagestam/phantom-types/stargazers) - Phantom types.
- [returns](https://github.com/dry-python/returns) [![GitHub stars](https://img.shields.io/github/stars/dry-python/returns?style=flat)](https://github.com/dry-python/returns/stargazers) - Make your functions return something meaningful, typed, and safe.
- [safetywrap](https://github.com/mplanchard/safetywrap) [![GitHub stars](https://img.shields.io/github/stars/mplanchard/safetywrap?style=flat)](https://github.com/mplanchard/safetywrap/stargazers) - Fully typesafe, Rust-like Result and Option types.
- [typet](https://github.com/contains-io/typet) [![GitHub stars](https://img.shields.io/github/stars/contains-io/typet?style=flat)](https://github.com/contains-io/typet/stargazers) - Length-bounded types, dynamic object validation.
- [useful-types](https://github.com/hauntsaninja/useful_types) [![GitHub stars](https://img.shields.io/github/stars/hauntsaninja/useful_types?style=flat)](https://github.com/hauntsaninja/useful_types/stargazers) - Collection of useful protocols and type aliases.

## Backports and improvements

- [future-typing](https://github.com/PrettyWood/future-typing) [![GitHub stars](https://img.shields.io/github/stars/PrettyWood/future-typing?style=flat)](https://github.com/PrettyWood/future-typing/stargazers) - Backport for type hinting generics in standard collections and union types as `X | Y`.
- [typing-extensions](https://github.com/python/typing_extensions) [![GitHub stars](https://img.shields.io/github/stars/python/typing_extensions?style=flat)](https://github.com/python/typing_extensions/stargazers) - Backported and experimental type hints.
- [typing-utils](https://github.com/bojiang/typing_utils) [![GitHub stars](https://img.shields.io/github/stars/bojiang/typing_utils?style=flat)](https://github.com/bojiang/typing_utils/stargazers) - Backport 3.8+ runtime typing utils(for eg: get_origin) & add issubtype & more.

## Tools

### Linters

- [flake8-annotations-complexity](https://github.com/best-doctor/flake8-annotations-complexity) [![GitHub stars](https://img.shields.io/github/stars/best-doctor/flake8-annotations-complexity?style=flat)](https://github.com/best-doctor/flake8-annotations-complexity/stargazers) - Plugin for flake8 to validate annotations complexity.
- [flake8-annotations](https://github.com/sco1/flake8-annotations) [![GitHub stars](https://img.shields.io/github/stars/sco1/flake8-annotations?style=flat)](https://github.com/sco1/flake8-annotations/stargazers) - Plugin for flake8 to check for presence of type annotations in function definitions.
- [flake8-pyi](https://github.com/ambv/flake8-pyi) [![GitHub stars](https://img.shields.io/github/stars/ambv/flake8-pyi?style=flat)](https://github.com/ambv/flake8-pyi/stargazers) - Plugin for Flake8 that provides specializations for type hinting stub files.
- [flake8-type-checking](https://github.com/snok/flake8-type-checking) [![GitHub stars](https://img.shields.io/github/stars/snok/flake8-type-checking?style=flat)](https://github.com/snok/flake8-type-checking/stargazers) - Plugin to help you guard any type-annotation-only import correctly.
- [flake8-typing-imports](https://github.com/asottile/flake8-typing-imports) [![GitHub stars](https://img.shields.io/github/stars/asottile/flake8-typing-imports?style=flat)](https://github.com/asottile/flake8-typing-imports/stargazers) - Plugin which checks that typing imports are properly guarded.
- [flake8-typing-only-imports](https://github.com/sondrelg/flake8-typing-only-imports) [![GitHub stars](https://img.shields.io/github/stars/sondrelg/flake8-typing-only-imports?style=flat)](https://github.com/sondrelg/flake8-typing-only-imports/stargazers) - flake8 plugin that helps identify which imports to put into type-checking blocks, and how to adjust your type annotations once imports are moved.
- [flake8-type-ignore](https://gitlab.com/jonafato/flake8-type-ignore/) - flake8 plugin to disallow type: ignore comments in your typed Python code.
- [wemake-python-styleguide](https://github.com/wemake-services/wemake-python-styleguide) [![GitHub stars](https://img.shields.io/github/stars/wemake-services/wemake-python-styleguide?style=flat)](https://github.com/wemake-services/wemake-python-styleguide/stargazers) - The strictest and most opinionated Python linter ever.
- [Ruff](https://github.com/astral-sh/ruff/) [![GitHub stars](https://img.shields.io/github/stars/astral-sh/ruff/?style=flat)](https://github.com/astral-sh/ruff//stargazers) - Extremely fast linter which supports lint rules from many other lint tools, such as flake8.

### Testing

- [mypy-test](https://github.com/orsinium-labs/mypy-test) [![GitHub stars](https://img.shields.io/github/stars/orsinium-labs/mypy-test?style=flat)](https://github.com/orsinium-labs/mypy-test/stargazers) - Test mypy plugins, stubs, custom types.
- [pytest-mypy-plugins](https://github.com/typeddjango/pytest-mypy-plugins) [![GitHub stars](https://img.shields.io/github/stars/typeddjango/pytest-mypy-plugins?style=flat)](https://github.com/typeddjango/pytest-mypy-plugins/stargazers) - Pytest plugin for testing mypy types, stubs, and plugins.
- [pytest-mypy-testing](https://github.com/davidfritzsche/pytest-mypy-testing) [![GitHub stars](https://img.shields.io/github/stars/davidfritzsche/pytest-mypy-testing?style=flat)](https://github.com/davidfritzsche/pytest-mypy-testing/stargazers) - Pytest plugin to test mypy static type analysis.
- [pytest-mypy](https://github.com/dbader/pytest-mypy) [![GitHub stars](https://img.shields.io/github/stars/dbader/pytest-mypy?style=flat)](https://github.com/dbader/pytest-mypy/stargazers) - Mypy static type checker plugin for Pytest.

### Working with types

- [com2ann](https://github.com/ilevkivskyi/com2ann) [![GitHub stars](https://img.shields.io/github/stars/ilevkivskyi/com2ann?style=flat)](https://github.com/ilevkivskyi/com2ann/stargazers) - Tool for translation of type comments to type annotations.
- [merge-pyi](https://github.com/google/pytype/tree/master/pytype/tools/merge_pyi) [![GitHub stars](https://img.shields.io/github/stars/google/pytype/tree/master/pytype/tools/merge_pyi?style=flat)](https://github.com/google/pytype/tree/master/pytype/tools/merge_pyi/stargazers) - Part of pytype toolchain, applies stub files onto source code.
- [mypy-baseline](https://github.com/orsinium-labs/mypy-baseline) [![GitHub stars](https://img.shields.io/github/stars/orsinium-labs/mypy-baseline?style=flat)](https://github.com/orsinium-labs/mypy-baseline/stargazers) - Integrate mypy with existing codebase. A CLI tool that filters out existing type errors and reports only new ones.
- [mypy-protobuf](https://github.com/dropbox/mypy-protobuf) [![GitHub stars](https://img.shields.io/github/stars/dropbox/mypy-protobuf?style=flat)](https://github.com/dropbox/mypy-protobuf/stargazers) - Tool to generate mypy stubs from protobufs.
- [mypy-silent](https://github.com/whtsky/mypy-silent/) [![GitHub stars](https://img.shields.io/github/stars/whtsky/mypy-silent/?style=flat)](https://github.com/whtsky/mypy-silent//stargazers) - Silence mypy by adding or removing code comments.
- [mypyc](https://github.com/python/mypy/tree/master/mypyc) [![GitHub stars](https://img.shields.io/github/stars/python/mypy/tree/master/mypyc?style=flat)](https://github.com/python/mypy/tree/master/mypyc/stargazers) - Compiles mypy-annotated, statically typed Python modules into CPython C extensions.
- [retype](https://github.com/ambv/retype) [![GitHub stars](https://img.shields.io/github/stars/ambv/retype?style=flat)](https://github.com/ambv/retype/stargazers) - Another tool to apply stubs to code.
- [typeforce](https://github.com/orsinium-labs/typeforce) [![GitHub stars](https://img.shields.io/github/stars/orsinium-labs/typeforce?style=flat)](https://github.com/orsinium-labs/typeforce/stargazers) - CLI tool that enriches your Python environment with type annotations, empowering mypy.
- [typesplainer](https://github.com/wasi-master/typesplainer) [![GitHub stars](https://img.shields.io/github/stars/wasi-master/typesplainer?style=flat)](https://github.com/wasi-master/typesplainer/stargazers) - A Python type explainer.
- [typing-inspect](https://github.com/ilevkivskyi/typing_inspect) [![GitHub stars](https://img.shields.io/github/stars/ilevkivskyi/typing_inspect?style=flat)](https://github.com/ilevkivskyi/typing_inspect/stargazers) - The typing_inspect module defines experimental API for runtime inspection of types defined in the `typing` module.
- [typing-json](https://pypi.org/project/typing-json/) - Lib for working with typed objects and JSON.

### Helper tools to add annotations to existing code

- [autotyping](https://github.com/JelleZijlstra/autotyping) [![GitHub stars](https://img.shields.io/github/stars/JelleZijlstra/autotyping?style=flat)](https://github.com/JelleZijlstra/autotyping/stargazers) - Automatically add simple return type annotations for functions (bool, None, Optional).
- [infer-types](https://github.com/orsinium-labs/infer-types) [![GitHub stars](https://img.shields.io/github/stars/orsinium-labs/infer-types?style=flat)](https://github.com/orsinium-labs/infer-types/stargazers) - CLI tool to automatically infer and add type annotations into Python code.
- [jsonschema-gentypes](https://github.com/camptocamp/jsonschema-gentypes) [![GitHub stars](https://img.shields.io/github/stars/camptocamp/jsonschema-gentypes?style=flat)](https://github.com/camptocamp/jsonschema-gentypes/stargazers) - Generate Python types based on TypedDict from a JSON Schema.
- [monkeytype](https://github.com/instagram/MonkeyType) [![GitHub stars](https://img.shields.io/github/stars/instagram/MonkeyType?style=flat)](https://github.com/instagram/MonkeyType/stargazers) - Collects runtime types of function arguments and return values, and can automatically generate stub files or even add draft type annotations directly to your code based on the types collected at runtime.
- [no_implicit_optional](https://github.com/hauntsaninja/no_implicit_optional) [![GitHub stars](https://img.shields.io/github/stars/hauntsaninja/no_implicit_optional?style=flat)](https://github.com/hauntsaninja/no_implicit_optional/stargazers) - A codemod to make your implicit optional type hints [PEP 484](https://peps.python.org/pep-0484/#union-types) compliant.
- [pyannotate](https://github.com/dropbox/pyannotate) [![GitHub stars](https://img.shields.io/github/stars/dropbox/pyannotate?style=flat)](https://github.com/dropbox/pyannotate/stargazers) - Insert annotations into your source code based on call arguments and return types observed at runtime.
- [PyTypes](https://github.com/pvs-hd-tea/PyTypes) [![GitHub stars](https://img.shields.io/github/stars/pvs-hd-tea/PyTypes?style=flat)](https://github.com/pvs-hd-tea/PyTypes/stargazers) - Infer Types by Python Tracing.
- [pytest-annotate](https://github.com/kensho-technologies/pytest-annotate) [![GitHub stars](https://img.shields.io/github/stars/kensho-technologies/pytest-annotate?style=flat)](https://github.com/kensho-technologies/pytest-annotate/stargazers) - Pyannotate plugin for pytest.
- [pytest-monkeytype](https://github.com/mariusvniekerk/pytest-monkeytype) [![GitHub stars](https://img.shields.io/github/stars/mariusvniekerk/pytest-monkeytype?style=flat)](https://github.com/mariusvniekerk/pytest-monkeytype/stargazers) - MonkeyType plugin for pytest.
- [pytype annotate-ast](https://github.com/google/pytype/tree/master/pytype/tools/annotate_ast) [![GitHub stars](https://img.shields.io/github/stars/google/pytype/tree/master/pytype/tools/annotate_ast?style=flat)](https://github.com/google/pytype/tree/master/pytype/tools/annotate_ast/stargazers) - A work-in-progress tool to annotate the nodes of an AST with their Python types.
- [RightTyper](https://github.com/RightTyper/RightTyper) [![GitHub stars](https://img.shields.io/github/stars/RightTyper/RightTyper?style=flat)](https://github.com/RightTyper/RightTyper/stargazers) - A tool that generates types for your function arguments and return values. RightTyper lets your code run at nearly full speed with almost no memory overhead.
- [auto-optional](https://github.com/Luttik/auto-optional) [![GitHub stars](https://img.shields.io/github/stars/Luttik/auto-optional?style=flat)](https://github.com/Luttik/auto-optional/stargazers) - Makes typed arguments Optional when the default argument is `None`.

### Mypy plugins

- [kubernetes-typed](https://github.com/gordonbondon/kubernetes-typed) [![GitHub stars](https://img.shields.io/github/stars/gordonbondon/kubernetes-typed?style=flat)](https://github.com/gordonbondon/kubernetes-typed/stargazers) - Plugin for Kubernetes [CRD](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/) type checking.
- [loguru-mypy](https://github.com/kornicameister/loguru-mypy) [![GitHub stars](https://img.shields.io/github/stars/kornicameister/loguru-mypy?style=flat)](https://github.com/kornicameister/loguru-mypy/stargazers) - Plugin for [loguru](https://github.com/Delgan/loguru) [![GitHub stars](https://img.shields.io/github/stars/Delgan/loguru?style=flat)](https://github.com/Delgan/loguru/stargazers) support.
- [mypy-zope](https://github.com/Shoobx/mypy-zope) [![GitHub stars](https://img.shields.io/github/stars/Shoobx/mypy-zope?style=flat)](https://github.com/Shoobx/mypy-zope/stargazers) - Plugin for [zope.interface](https://zopeinterface.readthedocs.io/en/latest/) support.
- [mypy/plugins](https://github.com/python/mypy/tree/master/mypy/plugins) [![GitHub stars](https://img.shields.io/github/stars/python/mypy/tree/master/mypy/plugins?style=flat)](https://github.com/python/mypy/tree/master/mypy/plugins/stargazers) - Plugins already integrated into mypy.
- [NumPy](https://numpy.org/devdocs/reference/typing.html) - Plugin for [NumPy](https://numpy.org) support.
- [pynamodb-mypy](https://github.com/pynamodb/pynamodb-mypy) [![GitHub stars](https://img.shields.io/github/stars/pynamodb/pynamodb-mypy?style=flat)](https://github.com/pynamodb/pynamodb-mypy/stargazers) - Plugin for [PynamoDB](https://github.com/pynamodb/PynamoDB) [![GitHub stars](https://img.shields.io/github/stars/pynamodb/PynamoDB?style=flat)](https://github.com/pynamodb/PynamoDB/stargazers) support.
- [pydantic](https://docs.pydantic.dev/latest/integrations/mypy/) - Plugin for additional [Pydantic](https://docs.pydantic.dev/latest/) support.

## Integrations

- [emacs-flycheck-mypy](https://github.com/lbolla/emacs-flycheck-mypy) [![GitHub stars](https://img.shields.io/github/stars/lbolla/emacs-flycheck-mypy?style=flat)](https://github.com/lbolla/emacs-flycheck-mypy/stargazers) - Mypy integration for Emacs.
- [mypy-playground](https://github.com/ymyzk/mypy-playground) [![GitHub stars](https://img.shields.io/github/stars/ymyzk/mypy-playground?style=flat)](https://github.com/ymyzk/mypy-playground/stargazers) - Online playground for mypy.
- [mypy-pycharm-plugin](https://github.com/dropbox/mypy-PyCharm-plugin) [![GitHub stars](https://img.shields.io/github/stars/dropbox/mypy-PyCharm-plugin?style=flat)](https://github.com/dropbox/mypy-PyCharm-plugin/stargazers) - Mypy integration for PyCharm.
- [pylance](https://github.com/microsoft/pylance-release) [![GitHub stars](https://img.shields.io/github/stars/microsoft/pylance-release?style=flat)](https://github.com/microsoft/pylance-release/stargazers) - PyRight integration for VSCode.
- [vim-mypy](https://github.com/Integralist/vim-mypy) [![GitHub stars](https://img.shields.io/github/stars/Integralist/vim-mypy?style=flat)](https://github.com/Integralist/vim-mypy/stargazers) - Mypy integration for Vim.
- [nbQA](https://github.com/nbQA-dev/nbQA) [![GitHub stars](https://img.shields.io/github/stars/nbQA-dev/nbQA?style=flat)](https://github.com/nbQA-dev/nbQA/stargazers) - Run type checkers (e.g. Mypy) on Jupyter Notebooks.

## Articles

### PEPs

- [PEP-3107](https://www.python.org/dev/peps/pep-3107) - Function Annotations.
- [PEP-482](https://www.python.org/dev/peps/pep-0482/) - Literature Overview for Type Hints.
- [PEP-483](https://www.python.org/dev/peps/pep-0483/) - The Theory of Type Hints.
- [PEP-484](https://www.python.org/dev/peps/pep-0484/) - Type Hints.
- [PEP-526](https://www.python.org/dev/peps/pep-0526/) - Syntax for Variable Annotations.
- [PEP-544](https://www.python.org/dev/peps/pep-0544/) - Protocols: Structural subtyping (static duck typing).
- [PEP-557](https://www.python.org/dev/peps/pep-0557/) - Data Classes.
- [PEP-560](https://www.python.org/dev/peps/pep-0560/) - Core support for typing module and generic types.
- [PEP-561](https://www.python.org/dev/peps/pep-0561/) - Distributing and Packaging Type Information.
- [PEP-563](https://www.python.org/dev/peps/pep-0563/) - Postponed Evaluation of Annotations.
- [PEP-585](https://www.python.org/dev/peps/pep-0585/) - Type Hinting Generics In Standard Collections.
- [PEP-586](https://www.python.org/dev/peps/pep-0586/) - Literal Types.
- [PEP-589](https://www.python.org/dev/peps/pep-0589/) - TypedDict: Type Hints for Dictionaries with a Fixed Set of Keys.
- [PEP-591](https://www.python.org/dev/peps/pep-0591/) - Adding a final qualifier to typing.
- [PEP-593](https://www.python.org/dev/peps/pep-0593/) - Flexible function and variable annotations.
- [PEP-604](https://www.python.org/dev/peps/pep-0604/) - Complementary syntax for Union[].
- [PEP-612](https://www.python.org/dev/peps/pep-0612/) - Parameter Specification Variables.
- [PEP-613](https://www.python.org/dev/peps/pep-0613/) - Explicit Type Aliases.

### Third-party articles

- [1-minute guide to real constants in Python](https://sobolevn.me/2018/07/real-python-contants) - Full tutorial about `Final` constants and inheritance.
- [Simple dependent types in Python](https://sobolevn.me/2019/01/simple-dependent-types-in-python) - Full tutorial about `Literal` types.
- [Testing mypy stubs, plugins, and types](https://sobolevn.me/2019/08/testing-mypy-types) - Full tutorial about testing mypy types.
- [Our journey to type checking 4 million lines of Python](https://dropbox.tech/application/our-journey-to-type-checking-4-million-lines-of-python) - Dropbox has been one of the first companies to adopt Python static type checking at this scale.
- [PyTest MonkeyType Introduction](https://dev.to/ldrscke/type-annotate-an-existing-python-django-codebase-with-monkeytype-254i) - Type Annotate an existing Python Django Codebase with MonkeyType.
- [The state of type hints in Python](https://bernat.tech/posts/the-state-of-type-hints-in-python/) - As of May 2018.
- [Type hints cheat sheet](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html) - Cheat sheet on writing type annotations by MyPy team.
- [Typechecking Django and DRF](https://sobolevn.me/2019/08/typechecking-django-and-drf) - Full tutorial about type-checking Django.
- [Type Check Your Django Application](https://kracekumar.com/post/type_check_your_django_app/) - An article based on two recent talks on adding type checks to Django.
- [typing](https://docs.python.org/3/library/typing.html) - Official Python documentation for `typing` module.
- [Python-typing-koans](https://github.com/kracekumar/python-typing-koans/) [![GitHub stars](https://img.shields.io/github/stars/kracekumar/python-typing-koans/?style=flat)](https://github.com/kracekumar/python-typing-koans//stargazers) - A set of examples to learn optional static typing in Python.
- [Python Type Checking (Guide)](https://realpython.com/python-type-checking/) - In this guide, you will get a look into Python type checking.
- [Adding type hints to urllib3](https://sethmlarson.dev/blog/2021-10-18/tests-arent-enough-case-study-after-adding-types-to-urllib3) - Tests are not enough: Case study adding type hints to urllib3.
- [Adam Johnsons Blog](https://adamj.eu/tech/tag/mypy/) - Adam Johnson blogs about typing practices.
- [ParamSpec Guide](https://sobolevn.me/2021/12/paramspec-guide) - Newly released feature in `PEP612` allows you do a lot of advanced typing things with functions and their signatures.
- [Static Typing Python Decorators](https://rednafi.github.io/reflections/static-typing-python-decorators.html) - Accurately static typing decorators in Python is an icky business. The wrapper function obfuscates type information required to statically determine the types of the parameters and the return values of the wrapped function.
- [How do mypy, Pyright, and ty compare?](https://pydevtools.com/handbook/explanation/how-do-mypy-pyright-and-ty-compare/) - A detailed comparison of the three major Python static type checkers covering features, performance, and trade-offs.
- [ty: A Complete Guide](https://pydevtools.com/handbook/explanation/ty-complete-guide/) - Comprehensive guide to ty, the fast Python type checker from Astral.

## Related

- [awesome-python](https://github.com/vinta/awesome-python) [![GitHub stars](https://img.shields.io/github/stars/vinta/awesome-python?style=flat)](https://github.com/vinta/awesome-python/stargazers) - Curated list of awesome Python frameworks, libraries, software and resources.
- [Python Developer Tooling Handbook](https://pydevtools.com/) - Comprehensive handbook covering Python type checkers, linters, and development tools with reference pages for [mypy](https://pydevtools.com/handbook/reference/mypy/), [Pyright](https://pydevtools.com/handbook/reference/pyright/), and [ty](https://pydevtools.com/handbook/reference/ty/).
- [python-typecheckers](https://github.com/ethanhs/python-typecheckers) [![GitHub stars](https://img.shields.io/github/stars/ethanhs/python-typecheckers?style=flat)](https://github.com/ethanhs/python-typecheckers/stargazers) - List of Python type checkers: static and runtime.
