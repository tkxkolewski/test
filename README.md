# 🇵🇱 Polski Konwerter 2.0
> **Profesjonalna, nowoczesna i bezpieczna aplikacja internetowa do konwersji plików**  
> Przebudowana architektura wielu silników z wbudowanym FFmpeg, obsługą formatów CAD, HEIC/AVIF oraz dojrzałym, redakcyjnym interfejsem bez schematów AI.

---

## 🌟 Najważniejsze zmiany w wersji 2.0

1. **Rzeczywisty silnik FFmpeg**:
   - Bezpośrednia obsługa ekstrakcji i transkodowania multimediów (`MP4 → MP3`, `MKV → MP4`, `WAV → MP3`, `FLAC → WAV`, `MP4 → GIF`).
   - Rzeczywista ekstrakcja ścieżki dźwiękowej z MP4:  
     `ffmpeg -nostdin -y -i input.mp4 -map 0:a:0 -vn -c:a libmp3lame -q:a 2 output.mp3`
   - Inteligentne wykrywanie braku ścieżki audio w plikach wideo i zwracanie czytelnego komunikatu:  
     *„Plik wideo nie zawiera ścieżki dźwiękowej do wyodrębnienia”*.
2. **Nowy, dojrzały kierunek artystyczny (brak schematów AI)**:
   - Rezygnacja ze sztucznych zagnieżdżonych kart w kartach, setek drobnych kapsułek i nadmiaru neonowych poświat.
   - Nowoczesny skład redakcyjny na spokojnym, jasnym tle (`#F8FAFC`) z możliwością włączenia motywu ciemnego (`#0B0F19`).
   - Jeden szlachetny błękit akcentowy (`#0F62FE`), naturalna polska wielkość liter i wysoka czytelność.
   - Jedno dominujące, przejrzyste pole przesyłania plików z natychmiastowym przejściem do wyboru formatu docelowego.
3. **Jedno uniwersalne BrandLogo w całej aplikacji**:
   - Współdzielony komponent wektorowy SVG o identycznej geometrii w nagłówku, stopce, menu mobilnym, panelach i ikonie favicon (`/static/brand-logo.svg`).
4. **Rozszerzona obsługa formatów**:
   - **Multimedia**: MP4, MKV, MOV, AVI, WEBM, MP3, WAV, FLAC, OGG, OPUS, M4A, AAC.
   - **Obrazy**: PNG, JPG, WEBP, BMP, TIFF, ICO, GIF, TGA, **HEIC**, **AVIF**.
   - **CAD**: DXF → SVG (wektorowy eksport geometrii), DXF → CSV (współrzędne elementów).
   - **Dokumenty**: DOCX ↔ TXT ↔ MD ↔ HTML ↔ PDF.
   - **PDF**: PDF → TXT, PDF → DOCX.
   - **Tabele**: CSV ↔ XLSX ↔ TSV ↔ JSON.
   - **Dane programistyczne**: JSON ↔ YAML ↔ TOML ↔ XML (z ochroną przed XXE).
   - **Napisy**: SRT ↔ VTT ↔ TXT.
   - **Czcionki**: TTF ↔ WOFF ↔ WOFF2, OTF → WOFF/WOFF2 (z Brotli).
   - **Modele 3D**: STL (ASCII & Binary) ↔ OBJ ↔ PLY.
   - **Archiwa**: ZIP ↔ TAR ↔ TAR.GZ (ochrona przed Zip Bomb).
   - **GPS**: GPX ↔ GeoJSON ↔ KML ↔ CSV.
5. **Diagnostyka silników**:
   - Endpoint `GET /api/diagnostics` raportuje stan FFmpeg, Pillow, ezdxf, fonttools oraz uprawnienia do zapisu.

---

## 🚀 Uruchomienie lokalne

### 1. Wymagania wstępne
- **Python 3.12+** (FFmpeg jest wbudowany automatycznie przez pakiet `imageio-ffmpeg`).

### 2. Instalacja zależności
```bash
py -3 -m pip install -r requirements.txt
```

### 3. Start serwera
```bash
py run_server.py
```
- Aplikacja WWW: **http://localhost:8000**
- Diagnostyka silników: **http://localhost:8000/api/diagnostics**
- Dokumentacja Swagger API: **http://localhost:8000/docs**

### 4. Uruchomienie testów (30 testów jednostkowych i integracyjnych)
```bash
py -3 -m pytest backend/tests -v
```

---

## 🧪 Wykaz testów automatycznych

Wszystkie 30 testów przechodzi pomyślnie z wynikiem 100%:
- `test_convert_mp4_to_mp3_real` — autentyczna ekstrakcja audio z wygenerowanego pliku MP4.
- `test_convert_mp4_no_audio_returns_clean_error` — test obsługi wideo bez audio.
- `test_convert_wav_to_mp3` — transkodowanie PCM WAV do MP3 LAME.
- `test_convert_dxf_to_svg` — renderowanie wektorów CAD DXF do SVG.
- `test_convert_png_to_jpg`, `test_convert_jpg_to_webp` — konwersje graficzne z regulacją jakości.
- `test_convert_docx_to_txt_and_pdf`, `test_convert_txt_to_pdf` — konwersje dokumentów.
- `test_convert_csv_to_xlsx_and_back` — tworzenie i odczyt arkuszy Excel.
- `test_convert_json_yaml_toml` — transformacje danych strukturalnych.
- `test_convert_srt_to_vtt_and_txt` — synchronizacja napisów.
- `test_convert_stl_to_obj` — geometria siatki 3D.
- `test_convert_gpx_to_geojson` — współrzędne tras GPS.
- `test_convert_zip_to_tar` — operacje na archiwach z weryfikacją bezpieczeństwa.
- `test_forbidden_cross_type_conversions` — bezwzględna blokada niedozwolonych par (`DOCX → MP3`, `CSV → MP3`, itp.).
- `test_sanitize_filename_prevents_traversal` oraz `test_ensure_safe_path_blocks_escape` — ochrona przed Path Traversal.
- `test_verify_file_signature_catches_fake_png` i `test_verify_file_signature_catches_fake_pdf` — weryfikacja Magic Bytes.
- `test_api_health`, `test_api_categories`, `test_api_upload_valid_file_and_allowed_targets`.

---

## 🔒 Bezpieczeństwo i Prywatność
1. Weryfikacja sygnatur binarnych (**Magic Bytes**) przed dopuszczeniem pliku.
2. Bezwzględna ochrona przed **Path Traversal** i **Command Injection** (procesy uruchamiane wyłącznie z tablicą argumentów).
3. Ochrona przed **Zip Bombami** (maks. współczynnik kompresji 100x, maks. 200 MB, maks. 500 plików).
4. Automatyczna retencja i **czyszczenie plików po 30 minutach** (TTL).
5. Bezpieczne nagłówki HTTP: `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`, `Referrer-Policy: strict-origin-when-cross-origin`.
