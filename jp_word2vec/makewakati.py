import MeCab

# tagger = MeCab.Tagger('-F\s%f[6] -U\s%m -E\\n')
tagger = MeCab.Tagger("-Owakati")

with open("kokoro.txt", "r", encoding="shift-jis") as f:
    text = f.readlines()
    for line in text:
        if "。" in line:
            result = tagger.parse(line)
            with open("kokoro_wakati.txt", "a", encoding="utf-8") as of:
                of.write(result[1:])
        else:
            pass

print("Finish")
