"""
Main entry point for the ShadowGuard CLI.

This module currently contains minimal functionality to demonstrate how
ShadowGuard could be instrumented with analytics and extended in the
future.  It reports basic events to Amplitude (if configured) and
prints a placeholder message.  You can expand the `check_packages`
function to verify package integrity against your local mirror.
"""

from __future__ import annotations

import os
import sys
from typing import Optional

try:
    # The official Amplitude Analytics library for Python.  Install with:
    #   pip install amplitude-analytics
    from amplitude import Amplitude, BaseEvent  # type: ignore
except ImportError:
    Amplitude = None  # type: ignore  # type: ignore[assignment]
    BaseEvent = None  # type: ignore


def send_event(event_type: str, user_id: str = "anonymous") -> None:
    """Send an analytics event to Amplitude if the API key is set.

    Args:
        event_type: The name of the event (e.g., "app_started").
        user_id: Identifier for the user triggering the event.  Defaults to
            ``"anonymous"``.  Customize this with a real user identifier if
            available.
    """
    api_key = os.getenv("AMPLITUDE_API_KEY")
    if not api_key:
        return
    if Amplitude is None or BaseEvent is None:
        # The amplitude-analytics library is not installed.  Skip sending.
        return
    amp = Amplitude(api_key)
    event = BaseEvent(event_type=event_type, user_id=user_id)
    try:
        amp.track(event)
    except Exception:
        # Ignore errors from analytics to avoid impacting primary functionality.
        pass


def check_packages() -> None:
    """Placeholder for package integrity checking logic.

    In a future release this function will iterate over installed packages,
    compute cryptographic hashes, and compare them against a local mirror.
    """
    print("Checking packages (placeholder)...")


def main(argv: Optional[list[str]] = None) -> int:
    """Entry point for the ShadowGuard CLI.

    Args:
        argv: Optional list of command line arguments.  Defaults to
            ``sys.argv[1:]``.

    Returns:
        Exit code (0 for success).
    """
    send_event("app_started")
    args = argv if argv is not None else sys.argv[1:]
    # For now we support a single subcommand "check"
    if not args or args[0] in {"check", "scan"}:
        check_packages()
    else:
        print(f"Unknown command: {args[0]}", file=sys.stderr)
        print("Usage: shadowguard check", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
