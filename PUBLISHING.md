# Publishing (uv)

This guide keeps the release flow reproducible and aligned with uv-based tooling.

## One-time setup

- Configure GitHub Actions as a PyPI Trusted Publisher.
- For local publishing, create a PyPI token and store it as `UV_PUBLISH_TOKEN`.
- Ensure `pyproject.toml` has the right version before each release.

## Build

```bash
uv build
```

## Publish

```bash
uv publish
```

## Release checklist

- Update the version in `pyproject.toml`.
- Review `README.md` for up-to-date CLI examples.
- Build and publish using uv.
