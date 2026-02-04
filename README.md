# ShadowGuard

ShadowGuard is a security‑focused Python tool designed to help developers
verify the integrity of their dependencies and maintain a private mirror of
trusted packages.  It provides a command‑line interface to scan installed
packages, compare checksums against a local mirror, and download clean
packages when corruption or tampering is detected.

## Features

- **Package integrity scanning** – compute SHA‑256 checksums for installed
  packages and compare them to known‑good hashes.
- **Mirror integration** – when a corrupted or missing package is detected,
  ShadowGuard can fetch replacements from a local mirror (see the companion
  `pip-backup` repository for instructions on creating one).
- **Extensibility** – the core tool is intentionally minimal.  You can
  extend `shadowguard/main.py` to add additional checks (for example, GPG
  signature verification) or to integrate with external vulnerability
  databases.
- **Paid feature placeholders** – hooks are included for future premium
  features such as real‑time monitoring, automated updates, and advanced
  analytics.  These features will be available under a paid subscription
  model to support ongoing development.

## Getting Started

Clone this repository and install it in editable mode:

```sh
pip install -e .
```

Run the CLI to scan your environment (currently a placeholder):

```sh
shadowguard check
```

At present this command prints a placeholder message.  Implementations of
package scanning and verification live in `shadowguard/main.py`.

### Analytics Integration

ShadowGuard can optionally send anonymous usage events to
[Amplitude](https://amplitude.com/) so you can understand how the tool is
used.  To enable analytics:

1. Create an account and a project on Amplitude to obtain an API key.
2. Install the Amplitude Analytics SDK:

   ```sh
   pip install amplitude-analytics
   ```

3. Set the `AMPLITUDE_API_KEY` environment variable before running
   ShadowGuard.  For example:

   ```sh
   export AMPLITUDE_API_KEY=your-amplitude-api-key
   shadowguard check
   ```

If the environment variable is unset or the SDK is not installed, the
analytics code is silently disabled.

## Project Structure

```
shadowguard/
├── pyproject.toml          Project metadata and build configuration
├── README.md               This file
└── shadowguard/
    ├── __init__.py         Package initialization
    └── main.py             CLI entry point and core logic
```

## Monetization

ShadowGuard is distributed under a dual‑license model.  The core functionality
(including package integrity checks and mirror integration) is open source and
free to use.  Advanced features such as continuous monitoring, detailed
analytics, and enterprise support will be offered under a paid subscription.

If you are interested in sponsoring development or licensing premium features,
please open an issue or contact the maintainer.
