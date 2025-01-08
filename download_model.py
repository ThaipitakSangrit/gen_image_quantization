from huggingface_hub import hf_hub_download, list_repo_files
import os

# ระบุชื่อโมเดลที่ต้องการดาวน์โหลด
model_id = "stabilityai/stable-diffusion-3.5-medium"

# เพิ่ม Token
token = "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"

# ดึงรายชื่อไฟล์ทั้งหมดใน repository ของโมเดล
try:
    files = list_repo_files(repo_id=model_id, token=token)
except Exception as e:
    print(f"ไม่สามารถดึงรายชื่อไฟล์ได้: {e}")
    exit()

# ระบุโฟลเดอร์ที่จะเก็บไฟล์ที่ดาวน์โหลด
cache_dir = "./models"

# สร้างโฟลเดอร์หากยังไม่มี
os.makedirs(cache_dir, exist_ok=True)

# วนลูปดาวน์โหลดทุกไฟล์จาก repository
for file in files:
    try:
        # ดาวน์โหลดไฟล์จาก Hugging Face
        file_path = hf_hub_download(repo_id=model_id, filename=file, cache_dir=cache_dir, use_auth_token=token)
        print(f"ดาวน์โหลดไฟล์: {file} ไปที่ {file_path}")
    except Exception as e:
        print(f"ไม่สามารถดาวน์โหลดไฟล์ {file} ได้: {e}")
