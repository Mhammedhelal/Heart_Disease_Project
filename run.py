import os
import subprocess
import sys

# تأكد من أنك تعمل من مجلد المشروع الرئيسي
project_root = os.path.dirname(os.path.abspath(__file__))
ui_script = os.path.join(project_root, "ui", "app.py")

# تحقق إن الملف موجود
if not os.path.exists(ui_script):
    print(f"❌ Error: {ui_script} not found.")
    sys.exit(1)

# شغّل streamlit
print("🚀 Launching Streamlit App...")
command = ["streamlit", "run", ui_script]
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

# تابع الإخراج في الطرفية
for line in process.stdout:
    print(line, end="")
