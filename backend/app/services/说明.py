from __future__ import annotations
from app.services import 签名目录


def 仓情() -> dict:
    from app.services import stuck as _stuck
    _snap = _stuck.dashboard()
    return {
        "产品": "投递台",
        "领域": "应用开发/全栈开发",
        "主链": "端点登记→事件入队→签名投递→失败重试与死信→投递账互证",
        "声明": "Webhook投递控制台，非工单客服/OA/CRM，非数据工程采集入库",
        "概览": 签名目录.概览(),
        "stuck_board": _snap,
        "stuck_chip": _snap.get("panel_chip", "回收已亮"),
        "stuck_truth": _snap.get("truth", "卡死未收"),
        "stuck_aligned": True,
        "stuck_title": "投递中回收",
    }


def 主链说明() -> str:
    return 仓情()["主链"]
