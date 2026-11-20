"""index.html + assets/*.png -> mecit-abi.html (tek dosya, WhatsApp ile paylaşılabilir)."""
import base64, pathlib, re
kok = pathlib.Path(__file__).parent
html = (kok / "index.html").read_text(encoding="utf-8")
def gom(m):
    yol = kok / m.group(1)
    return "data:image/png;base64," + base64.b64encode(yol.read_bytes()).decode()
html = re.sub(r"(assets/[\w\-]+\.png)", lambda m: gom(m), html)
(kok / "mecit-abi.html").write_text(html, encoding="utf-8")
print("mecit-abi.html", len(html) // 1024, "KB")
