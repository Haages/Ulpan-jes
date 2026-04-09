
import json

# Laad de repo database (de echte met 240 woorden)
with open('vocab_database.json', encoding='utf-8') as f:
    db = json.load(f)

# SVG data — alleen les 1 woorden
svg_data = {
    ("אני", "ani"): """<svg viewBox="0 0 110 115" xmlns="http://www.w3.org/2000/svg">
  <circle cx="55" cy="57" r="53" fill="#E1F5EE"/>
  <circle cx="55" cy="28" r="13" fill="#F5C4B3"/>
  <path d="M42 24 C42 15 68 15 68 24 C68 17 42 17 42 24Z" fill="#5DCAA5"/>
  <circle cx="49" cy="26" r="2" fill="#444"/>
  <circle cx="61" cy="26" r="2" fill="#444"/>
  <path d="M48 34 Q55 38 62 34" stroke="#C8967A" stroke-width="2" fill="none" stroke-linecap="round"/>
  <rect x="41" y="42" width="28" height="26" rx="8" fill="#1D9E75"/>
  <rect x="41" y="65" width="12" height="24" rx="6" fill="#1D9E75"/>
  <rect x="57" y="65" width="12" height="24" rx="6" fill="#1D9E75"/>
  <rect x="28" y="42" width="13" height="22" rx="6" fill="#F5C4B3"/>
  <rect x="69" y="26" width="13" height="18" rx="6" fill="#F5C4B3"/>
  <ellipse cx="75" cy="21" rx="6" ry="7" fill="#F5C4B3"/>
  <line x1="71" y1="15" x2="70" y2="8" stroke="#F5C4B3" stroke-width="3" stroke-linecap="round"/>
  <line x1="75" y1="13" x2="75" y2="6" stroke="#F5C4B3" stroke-width="3" stroke-linecap="round"/>
  <line x1="79" y1="15" x2="80" y2="8" stroke="#F5C4B3" stroke-width="3" stroke-linecap="round"/>
</svg>""",
    ("אתה", "ata"): """<svg viewBox="0 0 110 110" xmlns="http://www.w3.org/2000/svg">
  <circle cx="55" cy="55" r="53" fill="#E6F1FB"/>
  <circle cx="24" cy="28" r="13" fill="#F5C4B3"/>
  <path d="M11 24 C11 15 37 15 37 24 C37 17 11 17 11 24Z" fill="#85B7EB"/>
  <circle cx="19" cy="26" r="2" fill="#444"/>
  <circle cx="29" cy="26" r="2" fill="#444"/>
  <path d="M18 33 Q24 37 30 33" stroke="#C8967A" stroke-width="1.5" fill="none" stroke-linecap="round"/>
  <rect x="14" y="41" width="20" height="24" rx="7" fill="#378ADD"/>
  <rect x="14" y="62" width="9" height="20" rx="4" fill="#185FA5"/>
  <rect x="25" y="62" width="9" height="20" rx="4" fill="#185FA5"/>
  <rect x="3" y="41" width="11" height="20" rx="5" fill="#F5C4B3"/>
  <rect x="34" y="44" width="20" height="9" rx="4" fill="#F5C4B3"/>
  <ellipse cx="57" cy="48" rx="6" ry="5" fill="#F5C4B3"/>
  <line x1="60" y1="46" x2="66" y2="44" stroke="#F5C4B3" stroke-width="3" stroke-linecap="round"/>
  <path d="M68 41 L74 46 L68 51 Z" fill="#378ADD"/>
  <circle cx="88" cy="28" r="11" fill="#F5C4B3"/>
  <path d="M77 24 C77 17 99 17 99 24 C99 19 77 19 77 24Z" fill="#9FE1CB"/>
  <circle cx="83" cy="26" r="2" fill="#444"/>
  <circle cx="93" cy="26" r="2" fill="#444"/>
  <path d="M82 33 Q88 37 94 33" stroke="#C8967A" stroke-width="1.5" fill="none" stroke-linecap="round"/>
  <rect x="78" y="39" width="20" height="24" rx="7" fill="#1D9E75"/>
  <rect x="78" y="60" width="9" height="20" rx="4" fill="#0F6E56"/>
  <rect x="89" y="60" width="9" height="20" rx="4" fill="#0F6E56"/>
  <rect x="98" y="39" width="11" height="20" rx="5" fill="#F5C4B3"/>
  <rect x="67" y="39" width="11" height="20" rx="5" fill="#F5C4B3"/>
</svg>""",
    ("את", "at"): """<svg viewBox="0 0 110 110" xmlns="http://www.w3.org/2000/svg">
  <circle cx="55" cy="55" r="53" fill="#FBEAF0"/>
  <circle cx="22" cy="28" r="11" fill="#F5C4B3"/>
  <path d="M11 24 C11 16 33 16 33 24 C33 18 11 18 11 24Z" fill="#D4537E"/>
  <circle cx="11" cy="31" r="3" fill="#FAC775" stroke="#EF9F27" stroke-width="1"/>
  <circle cx="33" cy="31" r="3" fill="#FAC775" stroke="#EF9F27" stroke-width="1"/>
  <circle cx="17" cy="26" r="2" fill="#444"/>
  <circle cx="27" cy="26" r="2" fill="#444"/>
  <path d="M16 33 Q22 37 28 33" stroke="#C8967A" stroke-width="1.5" fill="none" stroke-linecap="round"/>
  <path d="M13 39 L9 52 L1 86 L43 86 L35 52 L31 39 Z" fill="#D4537E"/>
  <line x1="9" y1="52" x2="33" y2="52" stroke="#F4C0D1" stroke-width="1.5"/>
  <path d="M15 39 L22 45 L29 39" fill="none" stroke="#F4C0D1" stroke-width="1.5"/>
  <rect x="1" y="39" width="8" height="14" rx="4" fill="#F5C4B3"/>
  <rect x="31" y="41" width="18" height="8" rx="4" fill="#F5C4B3"/>
  <ellipse cx="52" cy="45" rx="5" ry="4" fill="#F5C4B3"/>
  <line x1="54" y1="43" x2="60" y2="41" stroke="#F5C4B3" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M62 38 L67 42 L62 46 Z" fill="#D4537E"/>
  <circle cx="82" cy="28" r="11" fill="#F5C4B3"/>
  <path d="M71 24 C71 16 93 16 93 24 C93 18 71 18 71 24Z" fill="#ED93B1"/>
  <circle cx="71" cy="31" r="3" fill="#FAC775" stroke="#EF9F27" stroke-width="1"/>
  <circle cx="93" cy="31" r="3" fill="#FAC775" stroke="#EF9F27" stroke-width="1"/>
  <circle cx="77" cy="26" r="2" fill="#444"/>
  <circle cx="87" cy="26" r="2" fill="#444"/>
  <path d="M76 33 Q82 37 88 33" stroke="#C8967A" stroke-width="1.5" fill="none" stroke-linecap="round"/>
  <path d="M73 39 L69 52 L61 86 L103 86 L95 52 L91 39 Z" fill="#ED93B1"/>
  <line x1="69" y1="52" x2="91" y2="52" stroke="#F4C0D1" stroke-width="1.5"/>
  <path d="M75 39 L82 45 L89 39" fill="none" stroke="#F4C0D1" stroke-width="1.5"/>
  <rect x="60" y="39" width="8" height="14" rx="4" fill="#F5C4B3"/>
  <rect x="92" y="39" width="8" height="14" rx="4" fill="#F5C4B3"/>
</svg>""",
    ("רוצה", "rotze"): """<svg viewBox="0 0 110 110" xmlns="http://www.w3.org/2000/svg">
  <circle cx="55" cy="55" r="53" fill="#FCEBEB"/>
  <circle cx="32" cy="58" r="13" fill="#F5C4B3"/>
  <path d="M19 54 C19 46 45 46 45 54 C45 48 19 48 19 54Z" fill="#85B7EB"/>
  <circle cx="27" cy="56" r="2" fill="#444"/>
  <circle cx="37" cy="56" r="2" fill="#444"/>
  <path d="M26 63 Q32 67 38 63" stroke="#C8967A" stroke-width="2" fill="none" stroke-linecap="round"/>
  <rect x="22" y="71" width="18" height="22" rx="6" fill="#378ADD"/>
  <rect x="22" y="90" width="8" height="16" rx="4" fill="#185FA5"/>
  <rect x="32" y="90" width="8" height="16" rx="4" fill="#185FA5"/>
  <rect x="10" y="71" width="12" height="18" rx="5" fill="#F5C4B3"/>
  <rect x="40" y="71" width="12" height="18" rx="5" fill="#F5C4B3"/>
  <circle cx="50" cy="48" r="3" fill="white" stroke="#5DCAA5" stroke-width="1.5"/>
  <circle cx="60" cy="38" r="5" fill="white" stroke="#5DCAA5" stroke-width="1.5"/>
  <ellipse cx="82" cy="23" rx="23" ry="16" fill="white" stroke="#5DCAA5" stroke-width="2"/>
  <circle cx="82" cy="19" r="6" fill="#F09595"/>
  <circle cx="79" cy="17" r="2" fill="white" opacity="0.5"/>
  <polygon points="78,24 82,33 86,24" fill="#FAC775"/>
  <line x1="79" y1="26" x2="85" y2="26" stroke="#EF9F27" stroke-width="1"/>
  <line x1="79" y1="29" x2="85" y2="29" stroke="#EF9F27" stroke-width="1"/>
  <line x1="82" y1="24" x2="82" y2="32" stroke="#EF9F27" stroke-width="1"/>
</svg>""",
    ("רוצה", "rotza"): """<svg viewBox="0 0 110 110" xmlns="http://www.w3.org/2000/svg">
  <circle cx="55" cy="55" r="53" fill="#FBEAF0"/>
  <circle cx="32" cy="60" r="11" fill="#F5C4B3"/>
  <path d="M21 56 C21 49 43 49 43 56 C43 51 21 51 21 56Z" fill="#D4537E"/>
  <circle cx="21" cy="63" r="3" fill="#FAC775" stroke="#EF9F27" stroke-width="1"/>
  <circle cx="43" cy="63" r="3" fill="#FAC775" stroke="#EF9F27" stroke-width="1"/>
  <circle cx="27" cy="58" r="2" fill="#444"/>
  <circle cx="37" cy="58" r="2" fill="#444"/>
  <path d="M26 65 Q32 69 38 65" stroke="#C8967A" stroke-width="1.5" fill="none" stroke-linecap="round"/>
  <path d="M23 71 L19 82 L12 108 L52 108 L45 82 L41 71 Z" fill="#D4537E"/>
  <line x1="19" y1="82" x2="41" y2="82" stroke="#F4C0D1" stroke-width="1.5"/>
  <path d="M25 71 L32 77 L39 71" fill="none" stroke="#F4C0D1" stroke-width="1.5"/>
  <rect x="10" y="71" width="9" height="13" rx="4" fill="#F5C4B3"/>
  <rect x="43" y="71" width="9" height="13" rx="4" fill="#F5C4B3"/>
  <circle cx="50" cy="48" r="3" fill="white" stroke="#5DCAA5" stroke-width="1.5"/>
  <circle cx="60" cy="38" r="5" fill="white" stroke="#5DCAA5" stroke-width="1.5"/>
  <ellipse cx="82" cy="23" rx="23" ry="16" fill="white" stroke="#5DCAA5" stroke-width="2"/>
  <circle cx="82" cy="19" r="6" fill="#ED93B1"/>
  <circle cx="79" cy="17" r="2" fill="white" opacity="0.5"/>
  <polygon points="78,24 82,33 86,24" fill="#FAC775"/>
  <line x1="79" y1="26" x2="85" y2="26" stroke="#EF9F27" stroke-width="1"/>
  <line x1="79" y1="29" x2="85" y2="29" stroke="#EF9F27" stroke-width="1"/>
  <line x1="82" y1="24" x2="82" y2="32" stroke="#EF9F27" stroke-width="1"/>
</svg>""",
    ("צריך", "tzarich"): """<svg viewBox="0 0 110 110" xmlns="http://www.w3.org/2000/svg">
  <circle cx="55" cy="55" r="53" fill="#EAF3DE"/>
  <circle cx="34" cy="52" r="13" fill="#F5C4B3"/>
  <path d="M21 48 C21 39 47 39 47 48 C47 41 21 41 21 48Z" fill="#85B7EB"/>
  <circle cx="29" cy="50" r="2" fill="#444"/>
  <circle cx="39" cy="50" r="2" fill="#444"/>
  <path d="M28 57 Q34 61 40 57" stroke="#C8967A" stroke-width="2" fill="none" stroke-linecap="round"/>
  <rect x="24" y="65" width="18" height="24" rx="7" fill="#3B6D11"/>
  <rect x="24" y="86" width="8" height="18" rx="4" fill="#27500A"/>
  <rect x="34" y="86" width="8" height="18" rx="4" fill="#27500A"/>
  <rect x="12" y="65" width="12" height="20" rx="5" fill="#F5C4B3"/>
  <rect x="42" y="65" width="12" height="20" rx="5" fill="#F5C4B3"/>
  <circle cx="54" cy="42" r="3.5" fill="white" stroke="#639922" stroke-width="1.5"/>
  <circle cx="64" cy="33" r="5" fill="white" stroke="#639922" stroke-width="1.5"/>
  <ellipse cx="82" cy="21" rx="18" ry="12" fill="white" stroke="#639922" stroke-width="2"/>
  <line x1="82" y1="13" x2="82" y2="20" stroke="#3B6D11" stroke-width="4" stroke-linecap="round"/>
  <circle cx="82" cy="26" r="3" fill="#3B6D11"/>
</svg>""",
    ("צריכה", "tzricha"): """<svg viewBox="0 0 110 110" xmlns="http://www.w3.org/2000/svg">
  <circle cx="55" cy="55" r="53" fill="#EAF3DE"/>
  <circle cx="32" cy="52" r="11" fill="#F5C4B3"/>
  <path d="M21 48 C21 40 43 40 43 48 C43 42 21 42 21 48Z" fill="#D4537E"/>
  <circle cx="21" cy="55" r="3" fill="#FAC775" stroke="#EF9F27" stroke-width="1"/>
  <circle cx="43" cy="55" r="3" fill="#FAC775" stroke="#EF9F27" stroke-width="1"/>
  <circle cx="27" cy="50" r="2" fill="#444"/>
  <circle cx="37" cy="50" r="2" fill="#444"/>
  <path d="M26 57 Q32 61 38 57" stroke="#C8967A" stroke-width="1.5" fill="none" stroke-linecap="round"/>
  <path d="M22 63 L18 75 L10 105 L54 105 L46 75 L42 63 Z" fill="#3B6D11"/>
  <line x1="18" y1="75" x2="42" y2="75" stroke="#5DCAA5" stroke-width="1.5"/>
  <path d="M24 63 L32 69 L40 63" fill="none" stroke="#5DCAA5" stroke-width="1.5"/>
  <rect x="9" y="63" width="9" height="13" rx="4" fill="#F5C4B3"/>
  <rect x="43" y="63" width="9" height="13" rx="4" fill="#F5C4B3"/>
  <circle cx="54" cy="42" r="3.5" fill="white" stroke="#639922" stroke-width="1.5"/>
  <circle cx="64" cy="33" r="5" fill="white" stroke="#639922" stroke-width="1.5"/>
  <ellipse cx="82" cy="21" rx="18" ry="12" fill="white" stroke="#639922" stroke-width="2"/>
  <line x1="82" y1="13" x2="82" y2="20" stroke="#3B6D11" stroke-width="4" stroke-linecap="round"/>
  <circle cx="82" cy="26" r="3" fill="#3B6D11"/>
</svg>""",
    ("ללמוד", "lilmod"): """<svg viewBox="0 0 110 110" xmlns="http://www.w3.org/2000/svg">
  <circle cx="55" cy="55" r="53" fill="#E6F1FB"/>
  <rect x="12" y="68" width="86" height="7" rx="3" fill="#85B7EB"/>
  <line x1="22" y1="75" x2="22" y2="96" stroke="#85B7EB" stroke-width="5" stroke-linecap="round"/>
  <line x1="88" y1="75" x2="88" y2="96" stroke="#85B7EB" stroke-width="5" stroke-linecap="round"/>
  <path d="M14 44 L14 68 C14 68 36 62 55 68 L55 44 C36 38 14 44 14 44Z" fill="#E6F1FB" stroke="#378ADD" stroke-width="2"/>
  <path d="M55 44 L55 68 C55 68 74 62 96 68 L96 44 C74 38 55 44 55 44Z" fill="#B5D4F4" stroke="#378ADD" stroke-width="2"/>
  <line x1="55" y1="44" x2="55" y2="68" stroke="#378ADD" stroke-width="1.5"/>
  <line x1="22" y1="52" x2="50" y2="52" stroke="#B5D4F4" stroke-width="1.5"/>
  <line x1="22" y1="58" x2="50" y2="58" stroke="#B5D4F4" stroke-width="1.5"/>
  <line x1="22" y1="64" x2="44" y2="64" stroke="#B5D4F4" stroke-width="1.5"/>
  <line x1="60" y1="52" x2="88" y2="52" stroke="#85B7EB" stroke-width="1.5"/>
  <line x1="60" y1="58" x2="88" y2="58" stroke="#85B7EB" stroke-width="1.5"/>
  <circle cx="55" cy="28" r="13" fill="#F5C4B3"/>
  <path d="M42 24 C42 14 68 14 68 24 C68 17 42 17 42 24Z" fill="#85B7EB"/>
  <circle cx="49" cy="26" r="2" fill="#444"/>
  <circle cx="61" cy="26" r="2" fill="#444"/>
  <ellipse cx="38" cy="46" rx="8" ry="5" fill="#F5C4B3"/>
  <ellipse cx="72" cy="46" rx="8" ry="5" fill="#F5C4B3"/>
</svg>""",
    ("לשלם", "leshalem"): """<svg viewBox="0 0 110 110" xmlns="http://www.w3.org/2000/svg">
  <circle cx="55" cy="55" r="53" fill="#FAEEDA"/>
  <circle cx="30" cy="26" r="13" fill="#F5C4B3"/>
  <path d="M17 22 C17 13 43 13 43 22 C43 15 17 15 17 22Z" fill="#EF9F27"/>
  <circle cx="25" cy="24" r="2" fill="#444"/>
  <circle cx="35" cy="24" r="2" fill="#444"/>
  <path d="M24 31 Q30 35 36 31" stroke="#C8967A" stroke-width="2" fill="none" stroke-linecap="round"/>
  <rect x="20" y="40" width="18" height="24" rx="7" fill="#BA7517"/>
  <rect x="20" y="61" width="8" height="22" rx="4" fill="#7A4F10"/>
  <rect x="30" y="61" width="8" height="22" rx="4" fill="#7A4F10"/>
  <rect x="8" y="40" width="12" height="20" rx="5" fill="#F5C4B3"/>
  <rect x="38" y="44" width="20" height="9" rx="4" fill="#F5C4B3"/>
  <ellipse cx="61" cy="48" rx="6" ry="5" fill="#F5C4B3"/>
  <circle cx="82" cy="34" r="18" fill="#FAC775" stroke="#EF9F27" stroke-width="2.5"/>
  <circle cx="82" cy="34" r="12" fill="#FAC775" stroke="#EF9F27" stroke-width="1" opacity="0.4"/>
  <text x="82" y="41" text-anchor="middle" font-size="18" fill="#BA7517" font-family="Arial" font-weight="bold">$</text>
  <line x1="92" y1="22" x2="96" y2="18" stroke="white" stroke-width="2" stroke-linecap="round"/>
</svg>""",
    ("לדבר", "ledaber"): """<svg viewBox="0 0 110 110" xmlns="http://www.w3.org/2000/svg">
  <circle cx="55" cy="55" r="53" fill="#EAF3DE"/>
  <circle cx="30" cy="52" r="13" fill="#F5C4B3"/>
  <path d="M17 48 C17 39 43 39 43 48 C43 41 17 41 17 48Z" fill="#97C459"/>
  <circle cx="25" cy="50" r="2" fill="#444"/>
  <circle cx="35" cy="50" r="2" fill="#444"/>
  <path d="M24 57 Q30 61 36 57" stroke="#C8967A" stroke-width="2" fill="none" stroke-linecap="round"/>
  <rect x="20" y="65" width="18" height="24" rx="7" fill="#3B6D11"/>
  <rect x="20" y="86" width="8" height="18" rx="4" fill="#27500A"/>
  <rect x="30" y="86" width="8" height="18" rx="4" fill="#27500A"/>
  <rect x="8" y="65" width="12" height="20" rx="5" fill="#F5C4B3"/>
  <rect x="38" y="65" width="12" height="20" rx="5" fill="#F5C4B3"/>
  <path d="M50 20 C50 12 100 12 100 20 L100 52 C100 60 50 60 50 52 L50 60 L40 52 Z" fill="white" stroke="#639922" stroke-width="2.5"/>
  <line x1="60" y1="28" x2="90" y2="28" stroke="#639922" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="60" y1="37" x2="90" y2="37" stroke="#639922" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="60" y1="46" x2="76" y2="46" stroke="#9FE1CB" stroke-width="2.5" stroke-linecap="round"/>
</svg>""",
    ("מי", "mi"): """<svg viewBox="0 0 110 110" xmlns="http://www.w3.org/2000/svg">
  <circle cx="55" cy="55" r="53" fill="#EEEDFE"/>
  <circle cx="26" cy="44" r="13" fill="#AFA9EC"/>
  <path d="M13 40 C13 31 39 31 39 40 C39 33 13 33 13 40Z" fill="#7F77DD"/>
  <circle cx="21" cy="42" r="2" fill="#444"/>
  <circle cx="31" cy="42" r="2" fill="#444"/>
  <path d="M20 49 Q26 53 32 49" stroke="#8878CC" stroke-width="1.5" fill="none" stroke-linecap="round"/>
  <rect x="16" y="57" width="20" height="22" rx="6" fill="#534AB7"/>
  <rect x="16" y="76" width="9" height="18" rx="4" fill="#3C3489"/>
  <rect x="27" y="76" width="9" height="18" rx="4" fill="#3C3489"/>
  <rect x="5" y="57" width="11" height="20" rx="5" fill="#CECBF6"/>
  <rect x="36" y="57" width="11" height="20" rx="5" fill="#CECBF6"/>
  <circle cx="76" cy="44" r="13" fill="#AFA9EC"/>
  <path d="M63 40 C63 31 89 31 89 40 C89 33 63 33 63 40Z" fill="#7F77DD"/>
  <circle cx="71" cy="42" r="2" fill="#444"/>
  <circle cx="81" cy="42" r="2" fill="#444"/>
  <path d="M70 49 Q76 53 82 49" stroke="#8878CC" stroke-width="1.5" fill="none" stroke-linecap="round"/>
  <rect x="66" y="57" width="20" height="22" rx="6" fill="#534AB7"/>
  <rect x="66" y="76" width="9" height="18" rx="4" fill="#3C3489"/>
  <rect x="77" y="76" width="9" height="18" rx="4" fill="#3C3489"/>
  <rect x="55" y="57" width="11" height="20" rx="5" fill="#CECBF6"/>
  <rect x="86" y="57" width="11" height="20" rx="5" fill="#CECBF6"/>
  <path d="M44 12 C44 5 66 3 66 12 C66 17 55 19 55 24" stroke="#534AB7" stroke-width="4.5" fill="none" stroke-linecap="round"/>
  <circle cx="55" cy="30" r="3.5" fill="#534AB7"/>
</svg>""",
    ("מה", "ma"): """<svg viewBox="0 0 110 110" xmlns="http://www.w3.org/2000/svg">
  <circle cx="55" cy="55" r="53" fill="#EEEDFE"/>
  <rect x="22" y="60" width="66" height="40" rx="4" fill="#AFA9EC"/>
  <rect x="18" y="50" width="74" height="14" rx="3" fill="#7F77DD"/>
  <path d="M36 50 C28 40 40 35 47 42 L55 50 L63 42 C70 35 82 40 74 50Z" fill="#534AB7"/>
  <circle cx="55" cy="50" r="5" fill="#CECBF6"/>
  <path d="M44 16 C44 8 66 6 66 16 C66 21 55 23 55 28" stroke="#534AB7" stroke-width="5" fill="none" stroke-linecap="round"/>
  <circle cx="55" cy="36" r="4" fill="#534AB7"/>
</svg>""",
    ("לא", "lo"): """<svg viewBox="0 0 110 110" xmlns="http://www.w3.org/2000/svg">
  <circle cx="55" cy="55" r="53" fill="#FCEBEB"/>
  <circle cx="34" cy="26" r="13" fill="#F5C4B3"/>
  <path d="M21 22 C21 13 47 13 47 22 C47 15 21 15 21 22Z" fill="#F09595"/>
  <circle cx="29" cy="24" r="2" fill="#444"/>
  <circle cx="39" cy="24" r="2" fill="#444"/>
  <path d="M28 31 Q34 35 40 31" stroke="#C8967A" stroke-width="2" fill="none" stroke-linecap="round"/>
  <rect x="24" y="39" width="20" height="26" rx="7" fill="#E24B4A"/>
  <rect x="24" y="62" width="9" height="20" rx="4" fill="#A32D2D"/>
  <rect x="35" y="62" width="9" height="20" rx="4" fill="#A32D2D"/>
  <rect x="12" y="39" width="12" height="20" rx="5" fill="#F5C4B3" transform="rotate(22 18 49)"/>
  <rect x="44" y="39" width="12" height="20" rx="5" fill="#F5C4B3" transform="rotate(-22 50 49)"/>
  <circle cx="82" cy="42" r="20" fill="white" stroke="#E24B4A" stroke-width="2.5"/>
  <line x1="70" y1="30" x2="94" y2="54" stroke="#E24B4A" stroke-width="4.5" stroke-linecap="round"/>
  <line x1="94" y1="30" x2="70" y2="54" stroke="#E24B4A" stroke-width="4.5" stroke-linecap="round"/>
</svg>""",
    ("עברית", "ivrit"): """<svg viewBox="0 0 110 110" xmlns="http://www.w3.org/2000/svg">
  <circle cx="55" cy="55" r="53" fill="#E6F1FB"/>
  <circle cx="26" cy="60" r="13" fill="#F5C4B3"/>
  <path d="M13 56 C13 48 39 48 39 56 C39 50 13 50 13 56Z" fill="#85B7EB"/>
  <circle cx="21" cy="58" r="2.5" fill="#444"/>
  <circle cx="31" cy="58" r="2.5" fill="#444"/>
  <path d="M20 65 Q26 69 32 65" stroke="#C8967A" stroke-width="2" fill="none" stroke-linecap="round"/>
  <rect x="16" y="73" width="18" height="22" rx="6" fill="#378ADD"/>
  <rect x="16" y="92" width="8" height="14" rx="4" fill="#185FA5"/>
  <rect x="26" y="92" width="8" height="14" rx="4" fill="#185FA5"/>
  <rect x="4" y="73" width="12" height="18" rx="5" fill="#F5C4B3"/>
  <rect x="34" y="73" width="12" height="18" rx="5" fill="#F5C4B3"/>
  <path d="M40 14 C40 6 106 6 106 14 L106 60 C106 68 40 68 40 60 L40 68 L30 60 Z" fill="white" stroke="#378ADD" stroke-width="2"/>
  <rect x="46" y="11" width="54" height="40" rx="2" fill="white" stroke="#ddd" stroke-width="0.5"/>
  <rect x="46" y="13" width="54" height="8" fill="#0038B8"/>
  <rect x="46" y="39" width="54" height="8" fill="#0038B8"/>
  <polygon points="73,21 80,33 66,33" fill="none" stroke="#0038B8" stroke-width="2.5"/>
  <polygon points="73,37 80,25 66,25" fill="none" stroke="#0038B8" stroke-width="2.5"/>
</svg>""",
}

# Voeg SVGs toe aan bestaande woorden — overschrijf NIETS anders
fixes = 0
for w in db['woorden']:
    key = (w.get('he_clean',''), w.get('uitspraak',''))
    if key in svg_data:
        w['svg'] = svg_data[key]
        fixes += 1
        print(f"  SVG toegevoegd: {w['he_clean']} ({w['uitspraak']})")

print(f"Totaal: {fixes} SVGs toegevoegd")

with open('vocab_database.json', 'w', encoding='utf-8') as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

print("Klaar — push nu")
