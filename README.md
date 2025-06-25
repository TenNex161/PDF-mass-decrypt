>[!WARNING]
>Repository is not being updated and is archived

# PDF-mass-decrypt
Python script to interactively decrypt several encrypted PDF files with alternating passwords

Dependencies: os, pypdf
```
pip install os pypdf
```

# How to use:

1. Start script in command line
```
python3 decrypt.py
```
2. Script asks for:
  - Input path: Enter path where PDFs are located.
  - Output Path: Enter path where the decrypted files should be written, will overwrite files with same filename.
  - Filter: Filter PDFs with entered string in filename, useful for big folders.
3. Enter Password(s): Each password entered will be tried on every encrypted PDF.
4. Ta-da!
