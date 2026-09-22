import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

AMHARIC_MAP = {
    'sh': 'ሽ',
    'ch': 'ች',
    'ny': 'ኝ',
    'zh': 'ዥ',
    'ts': 'ጽ',
    'ph': 'ፍ',
    'kh': 'ኽ',
    'a': 'አ',
    'e': 'እ',
    'i': 'ኢ',
    'o': 'ኦ',
    'u': 'ኡ',
    'b': 'ብ',
    'c': 'ክ',
    'd': 'ድ',
    'f': 'ፍ',
    'g': 'ግ',
    'h': 'ህ',
    'j': 'ጅ',
    'k': 'ክ',
    'l': 'ል',
    'm': 'ም',
    'n': 'ን',
    'p': 'ፕ',
    'q': 'ቅ',
    'r': 'ር',
    's': 'ስ',
    't': 'ት',
    'v': 'ቭ',
    'w': 'ው',
    'x': 'ክስ',
    'y': 'ይ',
    'z': 'ዝ',
}


def latin_to_amharic(text):
  text = text.lower()
  for latin, geez in AMHARIC_MAP.items():
    text = text.replace(latin, geez)
  return text


def process_pdfs():
  source_dir = filedialog.askdirectory(title='የተበታተኑት ፎልደሮች ያሉበትን ዋና ፎልደር መርጥ')
  if not source_dir:
    return

  dest_dir = filedialog.askdirectory(title='ሁሉም PDF ተሰብስበው እንዲቀመጡበት አዲሱን ፎልደር መርጥ')
  if not dest_dir:
    return

  moved_count = 0
  for root, dirs, files in os.walk(source_dir):
    if os.path.abspath(root) == os.path.abspath(dest_dir):
      continue

    for file in files:
      if file.lower().endswith('.pdf'):
        source_file = os.path.join(root, file)
        parent_folder_name = os.path.basename(root)

        if os.path.abspath(root) == os.path.abspath(source_dir):
          base_name = os.path.splitext(file)[0]
        else:
          base_name = latin_to_amharic(parent_folder_name)

        new_file_name = f'{base_name}.pdf'
        dest_file = os.path.join(dest_dir, new_file_name)

        counter = 1
        while os.path.exists(dest_file):
          dest_file = os.path.join(dest_dir, f'{base_name}_{counter}.pdf')
          counter += 1

        shutil.move(source_file, dest_file)
        moved_count += 1

  messagebox.showinfo(
      'ተጠናቋል',
      f'በጠቅላላ {moved_count} PDF ፋይሎች በፎልደራቸው የአማርኛ ስም ብቻ ተሰይመው ተሰብስበዋል!',
  )


root = tk.Tk()
root.title('PDF Amharic Renamer')
root.geometry('420x220')
root.resizable(False, False)

lbl = tk.Label(
    root,
    text='PDF ፋይሎችን በፎልደራቸው የአማርኛ ስም ብቻ\nአደራጅቶ በአንድ ፎልደር የሚሰበስብ',
    font=('Arial', 11),
    pady=20,
)
lbl.pack()

btn = tk.Button(
    root,
    text='ፎልደር መርጠህ ጀምር',
    command=process_pdfs,
    bg='#4CAF50',
    fg='white',
    font=('Arial', 12, 'bold'),
    padx=10,
    pady=5,
)
btn.pack()

root.mainloop()
