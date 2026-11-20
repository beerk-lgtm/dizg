"""Kayıtları oyuna hazırlar.
Kullanım:
  python3 ses_hazirla.py KLASOR        -> KLASOR içindeki her dosya (m4a, ogg, opus, wav, mp3, aac...)
                                          adındaki ilk sayıya göre assets/ses/NN.mp3 olur. Örn: "07.m4a", "Kayıt 07.m4a"
  python3 ses_hazirla.py --bol DOSYA BASLANGIC
                                       -> Tek uzun kayıt: repliklerin arasında 2 sn sessizlik varsa
                                          parçalara böler ve BASLANGIC numarasından itibaren adlandırır.
Baştaki/sondaki sessizlik kırpılır, ses seviyesi eşitlenir, mono 64 kbps mp3 yapılır."""
import pathlib, re, subprocess, sys
kok = pathlib.Path(__file__).parent
hedef = kok / "assets" / "ses"; hedef.mkdir(parents=True, exist_ok=True)
FILTRE = ("silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.05,"
          "areverse,silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.1,areverse,"
          "loudnorm=I=-16:TP=-1.5:LRA=11")
def donustur(kaynak, no, bas=None, son=None):
    cmd = ["ffmpeg", "-y", "-loglevel", "error"]
    if bas is not None: cmd += ["-ss", f"{bas:.3f}", "-to", f"{son:.3f}"]
    cmd += ["-i", str(kaynak), "-af", FILTRE, "-ac", "1", "-ar", "44100", "-b:a", "64k", str(hedef / f"{no:02d}.mp3")]
    subprocess.run(cmd, check=True); print(f"  {kaynak.name} -> {no:02d}.mp3")
if len(sys.argv) >= 2 and sys.argv[1] == "--bol":
    dosya, no = pathlib.Path(sys.argv[2]), int(sys.argv[3])
    cikti = subprocess.run(["ffmpeg", "-i", str(dosya), "-af", "silencedetect=noise=-40dB:d=1.6", "-f", "null", "-"],
                           capture_output=True, text=True).stderr
    bas_l = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", cikti)]
    son_l = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", cikti)]
    sure = float(re.search(r"Duration: (\d+):(\d+):([\d.]+)", cikti).groups()[2]) + \
        60 * float(re.search(r"Duration: (\d+):(\d+):", cikti).group(2)) + 3600 * float(re.search(r"Duration: (\d+):", cikti).group(1))
    sinirlar = [0.0]
    for b, e in zip(bas_l, son_l): sinirlar += [b, e]
    sinirlar.append(sure)
    parcalar = [(sinirlar[i], sinirlar[i + 1]) for i in range(0, len(sinirlar) - 1, 2) if sinirlar[i + 1] - sinirlar[i] > 0.3]
    for (b, e) in parcalar: donustur(dosya, no, b, e); no += 1
    print(f"{len(parcalar)} parça çıkarıldı")
else:
    for f in sorted(pathlib.Path(sys.argv[1]).iterdir()):
        m = re.search(r"(\d+)", f.stem)
        if f.is_file() and m: donustur(f, int(m.group(1)))
