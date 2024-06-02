# qtmvvmtoolkit

## Description

Build MVVM software pattern for PySide6

## How build

```pwsh
pyhton -m build
```

## How Deploy

```
 twine upload dist/* -u $CI_DEPLOY_USER -p $CI_DEPLOY_PASSWORD --repository-url https://gitlab.com/api/v4/projects/45425930/packages/pypi
```
