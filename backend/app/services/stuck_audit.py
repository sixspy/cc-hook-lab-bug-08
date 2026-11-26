"""投递中回收读轨审计。"""
from __future__ import annotations

from app.services import stuck as core
from app.services import stuck_cutover as cutover
from app.services import stuck_dualwrite as dual


def audit_summary() -> dict:
    return {
        "title": "投递中回收审计",
        "core": core.dashboard(),
        "cutover": cutover.board(),
        "dualwrite": dual.dual_board(),
        "half": core.half_fix_display(),
    }
