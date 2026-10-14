# tunnel.py - Multi-Device Access & Persistent Auto-Reconnecting Public Tunnel
import sys
import time
import typing
import pinggy

# Ensure UTF-8 output on Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

class PersistentTunnelHandler(pinggy.BaseTunnelHandler):
    def tunnel_established(self, url: typing.List[str]):
        print("\n" + "=" * 65)
        print("  RESEARCHMATE AI - PUBLIC LINK GENERATED (OPEN ON ANY DEVICE):")
        for u in url:
            print(f"  --> {u}")
        print("  Local Wi-Fi Network Access: http://192.168.1.5:8000")
        print("  Localhost:                 http://localhost:8000")
        print("=" * 65 + "\n")
        sys.stdout.flush()
        try:
            with open("tunnel_url.txt", "w", encoding="utf-8") as f:
                f.write("\n".join(url))
        except Exception:
            pass

    def disconnected(self):
        print("[Tunnel] Disconnected from relay server. Reconnecting in 3s...")
        sys.stdout.flush()

def main():
    print("=" * 65)
    print("  RESEARCHMATE AI - PERSISTENT MULTI-DEVICE LAUNCHER")
    print("  Local Machine:  http://localhost:8000")
    print("  Wi-Fi Network:  http://192.168.1.5:8000 (Open on any phone/tablet/laptop)")
    print("  Connecting live public internet tunnel with auto-reconnect...")
    print("=" * 65)
    sys.stdout.flush()

    while True:
        try:
            pinggy.start_tunnel(
                forwardto=8000,
                type="http",
                autoreconnect=True,
                eventclass=PersistentTunnelHandler
            )
        except Exception as e:
            print(f"[Tunnel] Pinggy reconnect notice ({e}), restarting in 3s...")
            sys.stdout.flush()
            time.sleep(3)

if __name__ == "__main__":
    main()
