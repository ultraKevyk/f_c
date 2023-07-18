import re

def upravit_retezec(text):
    pattern = r'<option value="([^"]+)" class="([^"]+)">([^<]+)</option>'
    replacement = r'<a class="\2" value="\1">\3</a>'
    upraveny_text = re.sub(pattern, replacement, text)
    return upraveny_text

list = ['<option value="amur" class="dropdown-item">Amur</option>',
    '<option value="bolen" class="dropdown-item">Bolen</option>',
    '<option value="candát" class="dropdown-item">Candát</option>',
    '<option value="cejn" class="dropdown-item">Cejn</option>',
    '<option value="hlavatka" class="dropdown-item">Hlavatka</option>',
    '<option value="jelec jesen" class="dropdown-item">Jelec jesen</option>',
    '<option value="tloust" class="dropdown-item">Jelec tloušť</option>',
    '<option value="kapr" class="dropdown-item">Kapr</option>',
    '<option value="karas" class="dropdown-item">Karas</option>',
    '<option value="lipan" class="dropdown-item">Lipan</option>',
    '<option value="lín" class="dropdown-item">Lín</option>',
    '<option value="maréna peleď" class="dropdown-item">Maréna peleď</option>',
    '<option value="mník" class="dropdown-item">Mník</option>',
    '<option value="okoun" class="dropdown-item">Okoun</option>',
    '<option value="ostroretka" class="dropdown-item">Ostroretka</option>',
    '<option value="parma" class="dropdown-item">Parma</option>',
    '<option value="podoustev" class="dropdown-item">Podoustev</option>',
    '<option value="pstruh duhový" class="dropdown-item">Pstruh duhový</option>',
    '<option value="pstruh obecný" class="dropdown-item">Pstruh obecný</option>',
    '<option value="siven" class="dropdown-item">Siven</option>',
    '<option value="štika" class="dropdown-item">Štika</option>',
    '<option value="sumec" class="dropdown-item">Sumec</option>',
    '<option value="tolstolobik" class="dropdown-item">Tolstolobik</option>',
    '<option value="úhoř" class="dropdown-item">Úhoř</option>']

for line in list:
    print(upravit_retezec(line))


