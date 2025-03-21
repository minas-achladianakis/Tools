# 🛠️ Tools & Utilities

This folder contains scripts and small utilities that support academic and project work. These are designed to be practical, self-contained, and easy to reuse.


## 📄 Protect Your Work

**`protect_your_work.py`** is a utility that converts a PDF into images and reassembles them into a flattened PDF. This helps protect your work by preventing easy text extraction, copy-pasting, or direct editing — useful for submissions, limited-distribution documents, or academic sharing.

### 🔍 How It Works
- Takes a PDF input file (e.g., `My_Work'+ input_name+ '.pdf`) and converts each page to a high-resolution image.
- Temporarily saves these images as `image_1.jpg`, `image_2.jpg`, etc., in the **same folder where the script is run**.
- Reassemble's the images into a new PDF (e.g., `Protected'+ input_name+ '.pdf`) in the same folder.

### ⚠️ Usage Notes
- ✅ Make sure your input PDF file is in the **same folder** as the script.
- 📛 The script uses the **PDF filename format** `My_Work<task_number>.pdf` — update this if needed.
- 📂 All generated image files will be saved in the working directory.
- 🧹 Temporary image files **are not automatically deleted**, so you may want to remove them afterward.

### 💡 Example Use Case
> You want to share a problem set or partial solution but don’t want the content to be easily copied or altered. This script generates a clean, read-only version.

---

More tools will be added here over time.
