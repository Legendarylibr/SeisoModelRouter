"""Known third-party vendor trees bundled with the router service."""

from __future__ import annotations

from seiso.vendor.bootstrap import VendorBootstrap, make_vendor_bootstrap

ADAPTIVE_QUANT: VendorBootstrap = make_vendor_bootstrap(
    "adaptive-rl-quant",
    "adaptive_quant",
    missing_hint="Expected third_party/adaptive-rl-quant/src/adaptive_quant",
)

