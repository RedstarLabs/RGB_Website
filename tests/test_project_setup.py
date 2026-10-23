"""Smoke tests for the Phase 0 project setup."""


def test_package_can_be_imported() -> None:
    import rgb_website

    assert rgb_website is not None
