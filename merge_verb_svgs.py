"""
Voegt inline SVG pictogrammen toe aan de werkwoorden in les 2-5 die nog geen SVG hebben.
Stijl: 110x110 viewBox, pastel achtergrondcirkel, flat icon in het midden.
"""
import json

# Map op basis-betekenis (zonder (m)/(f)) → SVG
SVG_VOOR_BETEKENIS = {
    # can — muscle / strong
    'can': '''<svg viewBox="0 0 110 110" xmlns="http://www.w3.org/2000/svg">
  <circle cx="55" cy="55" r="53" fill="#FFE7D1"/>
  <path d="M30 58 Q30 42 48 42 L62 42 Q80 42 80 58 L80 70 Q80 80 70 80 L40 80 Q30 80 30 70 Z" fill="#F5A86A" stroke="#C76A1C" stroke-width="2"/>
  <ellipse cx="55" cy="44" rx="18" ry="8" fill="#F5C4B3"/>
  <path d="M37 58 Q55 68 73 58" stroke="#C76A1C" stroke-width="2" fill="none"/>
  <circle cx="55" cy="62" r="4" fill="#C76A1C"/>
</svg>''',

    # to receive — package / box
    'to receive': '''<svg viewBox="0 0 110 110" xmlns="http://www.w3.org/2000/svg">
  <circle cx="55" cy="55" r="53" fill="#F3E9FA"/>
  <rect x="25" y="42" width="60" height="46" rx="3" fill="#C89BEA" stroke="#6A3D99" stroke-width="2"/>
  <rect x="25" y="42" width="60" height="10" fill="#A573D9" stroke="#6A3D99" stroke-width="2"/>
  <line x1="55" y1="42" x2="55" y2="88" stroke="#6A3D99" stroke-width="2"/>
  <path d="M40 42 Q40 28 55 32 Q70 28 70 42" fill="none" stroke="#EF476F" stroke-width="3" stroke-linecap="round"/>
</svg>''',

    # to come — footprints / arrow
    'to come': '''<svg viewBox="0 0 110 110" xmlns="http://www.w3.org/2000/svg">
  <circle cx="55" cy="55" r="53" fill="#E1F5EE"/>
  <ellipse cx="38" cy="46" rx="8" ry="12" fill="#1D9E75"/>
  <circle cx="34" cy="36" r="2" fill="#1D9E75"/>
  <circle cx="42" cy="36" r="2" fill="#1D9E75"/>
  <ellipse cx="62" cy="68" rx="8" ry="12" fill="#5DCAA5"/>
  <circle cx="58" cy="58" r="2" fill="#5DCAA5"/>
  <circle cx="66" cy="58" r="2" fill="#5DCAA5"/>
  <path d="M78 50 L90 58 L78 66 L78 60 L70 60 L70 56 L78 56 Z" fill="#1D9E75"/>
</svg>''',

    # love — heart
    'love': '''<svg viewBox="0 0 110 110" xmlns="http://www.w3.org/2000/svg">
  <circle cx="55" cy="55" r="53" fill="#FDE2E9"/>
  <path d="M55 85 C30 65 20 48 30 38 C40 28 52 32 55 45 C58 32 70 28 80 38 C90 48 80 65 55 85 Z" fill="#EF476F" stroke="#B22D52" stroke-width="2"/>
  <ellipse cx="45" cy="48" rx="4" ry="3" fill="#FDE2E9" opacity="0.7"/>
</svg>''',

    # know — brain / lightbulb
    'know': '''<svg viewBox="0 0 110 110" xmlns="http://www.w3.org/2000/svg">
  <circle cx="55" cy="55" r="53" fill="#FFF6D1"/>
  <path d="M40 70 Q28 60 34 44 Q38 30 55 30 Q72 30 76 44 Q82 60 70 70 L70 78 L40 78 Z" fill="#FFD93D" stroke="#C89E10" stroke-width="2"/>
  <rect x="42" y="78" width="26" height="5" rx="2" fill="#C89E10"/>
  <rect x="45" y="85" width="20" height="4" rx="2" fill="#8A6A0A"/>
  <path d="M48 50 Q55 45 62 50" stroke="#C89E10" stroke-width="2" fill="none"/>
  <line x1="55" y1="52" x2="55" y2="70" stroke="#C89E10" stroke-width="2"/>
</svg>''',

    # hear — ear
    'hear': '''<svg viewBox="0 0 110 110" xmlns="http://www.w3.org/2000/svg">
  <circle cx="55" cy="55" r="53" fill="#FFE4EC"/>
  <path d="M44 30 Q72 28 74 52 Q74 70 62 76 Q54 80 52 72 Q50 66 56 62 Q62 58 58 52 Q52 48 44 50 Q36 50 38 40 Q40 32 44 30 Z" fill="#F5C4B3" stroke="#C8967A" stroke-width="2"/>
  <path d="M52 44 Q62 44 64 52 Q64 60 58 62" stroke="#C8967A" stroke-width="2" fill="none"/>
  <path d="M20 50 Q26 50 28 56" stroke="#378ADD" stroke-width="3" fill="none" stroke-linecap="round"/>
  <path d="M14 44 Q22 44 26 52" stroke="#378ADD" stroke-width="3" fill="none" stroke-linecap="round" opacity="0.6"/>
</svg>''',

    # to arrange — clipboard / list
    'to arrange': '''<svg viewBox="0 0 110 110" xmlns="http://www.w3.org/2000/svg">
  <circle cx="55" cy="55" r="53" fill="#E6F1FB"/>
  <rect x="28" y="24" width="54" height="66" rx="4" fill="white" stroke="#378ADD" stroke-width="2"/>
  <rect x="42" y="20" width="26" height="10" rx="2" fill="#85B7EB" stroke="#378ADD" stroke-width="2"/>
  <line x1="36" y1="44" x2="74" y2="44" stroke="#378ADD" stroke-width="2" stroke-linecap="round"/>
  <line x1="36" y1="54" x2="68" y2="54" stroke="#85B7EB" stroke-width="2" stroke-linecap="round"/>
  <line x1="36" y1="64" x2="74" y2="64" stroke="#85B7EB" stroke-width="2" stroke-linecap="round"/>
  <line x1="36" y1="74" x2="64" y2="74" stroke="#85B7EB" stroke-width="2" stroke-linecap="round"/>
  <path d="M34 44 L38 48 L44 40" stroke="#1D9E75" stroke-width="2.5" fill="none" stroke-linecap="round"/>
</svg>''',

    # to ask — question mark speech bubble
    'to ask': '''<svg viewBox="0 0 110 110" xmlns="http://www.w3.org/2000/svg">
  <circle cx="55" cy="55" r="53" fill="#FFF2D4"/>
  <path d="M22 28 Q22 20 30 20 L80 20 Q88 20 88 28 L88 62 Q88 70 80 70 L50 70 L36 84 L38 70 L30 70 Q22 70 22 62 Z" fill="white" stroke="#EF9F27" stroke-width="2"/>
  <path d="M48 36 Q48 28 55 28 Q62 28 62 36 Q62 42 55 46 L55 52" stroke="#EF9F27" stroke-width="4" fill="none" stroke-linecap="round"/>
  <circle cx="55" cy="60" r="3" fill="#EF9F27"/>
</svg>''',

    # to think — thought bubble
    'to think': '''<svg viewBox="0 0 110 110" xmlns="http://www.w3.org/2000/svg">
  <circle cx="55" cy="55" r="53" fill="#EAF3DE"/>
  <ellipse cx="55" cy="42" rx="32" ry="20" fill="white" stroke="#5A8A2F" stroke-width="2"/>
  <circle cx="32" cy="68" r="6" fill="white" stroke="#5A8A2F" stroke-width="2"/>
  <circle cx="24" cy="82" r="4" fill="white" stroke="#5A8A2F" stroke-width="2"/>
  <circle cx="18" cy="92" r="3" fill="white" stroke="#5A8A2F" stroke-width="2"/>
  <circle cx="44" cy="42" r="3" fill="#5A8A2F"/>
  <circle cx="55" cy="42" r="3" fill="#5A8A2F"/>
  <circle cx="66" cy="42" r="3" fill="#5A8A2F"/>
</svg>''',

    # to eat — plate with fork
    'to eat': '''<svg viewBox="0 0 110 110" xmlns="http://www.w3.org/2000/svg">
  <circle cx="55" cy="55" r="53" fill="#FFE7D1"/>
  <circle cx="55" cy="62" r="28" fill="white" stroke="#C76A1C" stroke-width="2.5"/>
  <circle cx="55" cy="62" r="20" fill="#FFE7D1" stroke="#C76A1C" stroke-width="1.5"/>
  <circle cx="50" cy="58" r="5" fill="#EF476F"/>
  <circle cx="60" cy="60" r="4" fill="#6EBF5D"/>
  <circle cx="55" cy="67" r="4" fill="#EF9F27"/>
  <rect x="20" y="30" width="3" height="32" fill="#8B6A3F" rx="1"/>
  <rect x="17" y="26" width="2" height="12" fill="#8B6A3F"/>
  <rect x="21" y="26" width="2" height="12" fill="#8B6A3F"/>
  <rect x="25" y="26" width="2" height="12" fill="#8B6A3F"/>
  <rect x="88" y="30" width="3" height="32" fill="#8B6A3F" rx="1"/>
  <ellipse cx="89" cy="32" rx="5" ry="8" fill="#8B6A3F"/>
</svg>''',

    # to work — briefcase
    'to work': '''<svg viewBox="0 0 110 110" xmlns="http://www.w3.org/2000/svg">
  <circle cx="55" cy="55" r="53" fill="#E6F1FB"/>
  <rect x="18" y="42" width="74" height="52" rx="4" fill="#8B6A3F" stroke="#4D3A1F" stroke-width="2"/>
  <path d="M42 42 L42 30 Q42 26 46 26 L64 26 Q68 26 68 30 L68 42" fill="none" stroke="#4D3A1F" stroke-width="3"/>
  <rect x="18" y="58" width="74" height="6" fill="#4D3A1F"/>
  <rect x="50" y="56" width="10" height="10" rx="1" fill="#FFD93D" stroke="#4D3A1F" stroke-width="1.5"/>
</svg>''',

    # to search — magnifying glass
    'to search': '''<svg viewBox="0 0 110 110" xmlns="http://www.w3.org/2000/svg">
  <circle cx="55" cy="55" r="53" fill="#F3E9FA"/>
  <circle cx="46" cy="46" r="22" fill="white" stroke="#6A3D99" stroke-width="4"/>
  <circle cx="46" cy="46" r="16" fill="#E0CDF4" opacity="0.4"/>
  <line x1="62" y1="62" x2="86" y2="86" stroke="#6A3D99" stroke-width="7" stroke-linecap="round"/>
  <line x1="36" y1="36" x2="44" y2="40" stroke="white" stroke-width="3" stroke-linecap="round"/>
</svg>''',

    # to close — padlock
    'to close': '''<svg viewBox="0 0 110 110" xmlns="http://www.w3.org/2000/svg">
  <circle cx="55" cy="55" r="53" fill="#FDE2E9"/>
  <path d="M36 52 L36 40 Q36 24 55 24 Q74 24 74 40 L74 52" fill="none" stroke="#4D3A1F" stroke-width="5"/>
  <rect x="28" y="50" width="54" height="44" rx="5" fill="#FFD93D" stroke="#4D3A1F" stroke-width="2.5"/>
  <circle cx="55" cy="68" r="5" fill="#4D3A1F"/>
  <rect x="53" y="68" width="4" height="14" fill="#4D3A1F"/>
</svg>''',
}


NL_NAAR_EN = {
    'kunnen': 'can',
    'ontvangen/krijgen': 'to receive',
    'komen': 'to come',
    'houden van': 'love',
    'weten/kennen': 'know',
    'horen': 'hear',
    'ordenen/regelen': 'to arrange',
    'vragen': 'to ask',
    'denken': 'to think',
    'eten': 'to eat',
    'werken': 'to work',
    'zoeken': 'to search',
    'sluiten': 'to close',
}


def basis(woord):
    import re
    t = (woord.get('en') or woord.get('nl') or '').strip()
    # strip (m)/(f)/(v) én (mannelijk)/(vrouwelijk)/(infinitief)
    t = re.sub(r'\s*\((m|f|v|mannelijk|vrouwelijk|infinitief)\)\s*', '', t).strip().lower()
    # Map Dutch verb to English
    if t in NL_NAAR_EN:
        t = NL_NAAR_EN[t]
    return t


def main():
    with open('vocab_database.json', encoding='utf-8') as f:
        db = json.load(f)

    toegevoegd = 0
    for w in db['woorden']:
        if w.get('soort') != 'ww':
            continue
        if w.get('svg'):
            continue  # niet overschrijven
        k = basis(w)
        if k in SVG_VOOR_BETEKENIS:
            w['svg'] = SVG_VOOR_BETEKENIS[k]
            toegevoegd += 1
            print(f"  + {w.get('he_clean')} ({w.get('uitspraak')}) — {k}")

    print(f"Totaal toegevoegd: {toegevoegd}")

    with open('vocab_database.json', 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=2)
    print("Opgeslagen.")


if __name__ == '__main__':
    main()
