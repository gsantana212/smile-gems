#!/usr/bin/env python3
# toothgem/api.py — order intake stub for smile-gems preview.
# ponytail: GitHub Pages serves the demo statically; this stub exists so the
# production checkout at skillhub.shop/toothgem/ can drop in a known shape
# without re-discovering the order JSON contract. No payment wiring here —
# AGENTS.md is explicit: real Stripe belongs in the separate prod repo.

import json
import os
import sys
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

ALLOWED_KITS = {
    "starter": {"name": "The Starter", "price": 39},
    "pro":     {"name": "The Pro",     "price": 89},
    "vault":   {"name": "The Vault",   "price": 149},
}

# /mnt/storage is moxbox's external drive (Ada mesh "max box"). The VPS
# doesn't mount it; on moxbox persistence is enabled, everywhere else the
# stub logs to stdout only.
PERSIST_DIR = "/mnt/storage/ollama/orders/smile-gems"
PERSIST_ENABLED = os.path.isdir(os.path.dirname(PERSIST_DIR))


def persist(order: dict) -> str | None:
    """Append order to JSONL ledger on moxbox; returns path or None."""
    if not PERSIST_ENABLED:
        return None
    os.makedirs(PERSIST_DIR, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d")
    path = os.path.join(PERSIST_DIR, f"orders-{stamp}.jsonl")
    with open(path, "a") as f:
        f.write(json.dumps(order) + "\n")
    return path


class Handler(BaseHTTPRequestHandler):
    def _json(self, code: int, payload: dict) -> None:
        body = json.dumps(payload).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/health":
            return self._json(200, {"ok": True, "persist": PERSIST_ENABLED})
        if self.path == "/kits":
            return self._json(200, {"kits": ALLOWED_KITS})
        self._json(404, {"error": "not found"})

    def do_POST(self):
        if self.path != "/order":
            return self._json(404, {"error": "not found"})
        try:
            length = int(self.headers.get("Content-Length", "0"))
            raw = self.rfile.read(length) if length else b"{}"
            data = json.loads(raw or b"{}")
        except (ValueError, json.JSONDecodeError) as e:
            return self._json(400, {"error": f"bad json: {e}"})

        sku = data.get("sku", "")
        email = (data.get("email") or "").strip()
        name = (data.get("name") or "").strip()
        if sku not in ALLOWED_KITS:
            return self._json(400, {"error": f"unknown sku: {sku}"})
        if "@" not in email:
            return self._json(400, {"error": "valid email required"})

        order = {
            "ts": datetime.now(timezone.utc).isoformat(),
            "sku": sku,
            "kit": ALLOWED_KITS[sku]["name"],
            "price_usd": ALLOWED_KITS[sku]["price"],
            "name": name,
            "email": email,
            "notes": (data.get("notes") or "").strip(),
            "source": data.get("source", "smile-gems-preview"),
        }
        path = persist(order)
        if path:
            order["_persisted"] = path
        print(json.dumps(order), flush=True)
        return self._json(201, {"ok": True, "order": order, "persisted": path})


def demo() -> None:
    """Self-check: GET /health, GET /kits, POST /order."""
    import urllib.request
    base = "http://127.0.0.1:8765"
    with ThreadingHTTPServer(("127.0.0.1", 8765), Handler) as srv:
        # Probe with a thread request
        try:
            r = urllib.request.urlopen(base + "/health", timeout=2)
            assert r.status == 200 and json.loads(r.read())["ok"] is True
            r = urllib.request.urlopen(base + "/kits", timeout=2)
            assert json.loads(r.read())["kits"]["pro"]["price"] == 89
            req = urllib.request.Request(
                base + "/order", method="POST",
                data=json.dumps({"sku": "pro", "name": "Test", "email": "t@x.io"}).encode(),
                headers={"Content-Type": "application/json"},
            )
            r = urllib.request.urlopen(req, timeout=2)
            assert json.loads(r.read())["ok"] is True
            print("demo OK")
        finally:
            srv.shutdown()


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "demo":
        demo()
    else:
        port = int(os.environ.get("PORT", "8765"))
        with ThreadingHTTPServer(("0.0.0.0", port), Handler) as srv:
            print(f"toothgem api on :{port} (persist={PERSIST_ENABLED})")
            srv.serve_forever()
