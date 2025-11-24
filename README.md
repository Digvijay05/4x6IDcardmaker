# Aadhaar Card Print Tool

A Python-based utility that converts a password-protected Aadhaar PDF into a clean, print-ready front–back image. The backend handles PDF decryption, page conversion, cropping, and final image composition, while the frontend provides a simple Tkinter interface for file selection.

---

## ✅ Features

* Remove password from encrypted PDFs
* Convert PDF pages to PNG images
* Crop front and back sections based on coordinates in `crop.txt`
* Resize and rotate images to match print orientation
* Combine both sides into a single printable layout
* Simple GUI for browsing files

---

## 🔧 Requirements

* Python 3.8+
* Poppler (for `pdf2image`)
* The following Python packages:

  ```bash
  pip install PyPDF2 pdf2image pillow
  ```

---

## 📁 Project Structure

```
project/
│
├─ backend.py
├─ frontend.py
├─ crop.txt
├─ temp/                # Output folder
└─ poppler/             # Poppler binaries (Windows)
```

---

## ⚙️ How It Works

1. **Remove Password**
   `remove_password()` decrypts the PDF (if encrypted) and rewrites it as a temporary unprotected file.

2. **Convert to Images**
   `convert_to_images()` converts PDF pages into PNG files using Poppler.

3. **Crop**
   `crop_image()` reads coordinates from `crop.txt` to extract the front and back areas.

4. **Compose Final Image**
   `create_image()` pastes both sides onto a fixed-size canvas and saves `aadhar.png` in `temp/`.

5. **GUI**
   `frontend.py` opens a window where the user selects a PDF and enters a password if required.

---

## ▶️ Running the Application

1. Install dependencies and Poppler.
2. Update the Poppler path in `backend.py` under `convert_to_images()`.
3. Ensure `crop.txt` contains crop coordinates:

   ```
   ##front
   left
   right
   top
   bottom
   ##back
   left
   right
   top
   bottom
   ```
4. Run:

   ```bash
   python frontend.py
   ```

---

## 📝 Output

* Final image saved as:

  ```
  temp/aadhar.png
  ```

---

## ⚠️ Notes

* Paths are currently Windows-style; adjust for other OSes.
* Incorrect coordinates will result in improper cropping.
* Only use this tool for your own Aadhaar card. Aadhaar data is sensitive.

---

## ✅ Future Improvements

* Error handling for invalid passwords/pages
* Progress indicators in the UI
* Cross-platform path support
* Automatic crop detection

---
