"""index.html + assets/ -> mecit-abi.html (tek dosya, WhatsApp ile paylaşılabilir).
assets/ses/NN.mp3 dosyaları varsa onları da içine gömer."""
import base64, json, pathlib, re
kok = pathlib.Path(__file__).parent
html = (kok / "index.html").read_text(encoding="utf-8")
def b64(yol, tip):
    return f"data:{tip};base64," + base64.b64encode(yol.read_bytes()).decode()
html = re.sub(r"assets/[\w\-/]+\.png", lambda m: b64(kok / m.group(0), "image/png"), html)
html = re.sub(r"assets/[\w\-/]+\.webp", lambda m: b64(kok / m.group(0), "image/webp"), html)
sesler = {f.stem: b64(f, "audio/mpeg") for f in sorted((kok / "assets" / "ses").glob("*.mp3"))}
html = html.replace("const SES_GOMULU=null;", "const SES_GOMULU=" + json.dumps(sesler) + ";", 1)
(kok / "mecit-abi.html").write_text(html, encoding="utf-8")
print(f"mecit-abi.html {len(html)//1024} KB, {len(sesler)} ses gömüldü")
