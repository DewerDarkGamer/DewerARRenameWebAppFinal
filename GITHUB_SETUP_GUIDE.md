# คำแนะนำการตั้งค่า GitHub สำหรับ Barcode Reader

## ไฟล์ที่เตรียมไว้สำหรับ GitHub

ไฟล์ทั้งหมดอยู่ในโฟลเดอร์ `github_files/` และพร้อมอัปโหลดไปยัง GitHub:

### ไฟล์หลัก
- `README.md` - คำแนะนำการใช้งาน
- `main.py` - จุดเริ่มต้นหลักของโปรแกรม
- `app.py` - เว็บแอปพลิเคชัน Flask
- `barcode_desktop.py` - แอปพลิเคชัน Desktop GUI
- `pyinstaller_spec.py` - สคริปต์สำหรับ build EXE

### ไฟล์การตั้งค่า
- `requirements.txt` - Dependencies สำหรับเว็บแอป
- `requirements_desktop.txt` - Dependencies สำหรับ desktop app
- `.gitignore` - ไฟล์ที่ไม่ต้องการใน git
- `LICENSE` - สัญญาอนุญาต MIT

### GitHub Actions
- `.github/workflows/build-exe.yml` - Workflow สำหรับ build EXE อัตโนมัติ

### เอกสาร
- `build_instructions.md` - วิธีการ build EXE แบบละเอียด

### โฟลเดอร์
- `templates/` - HTML templates สำหรับเว็บแอป
- `static/` - CSS, JS files สำหรับเว็บแอป

## ขั้นตอนการอัปโหลดไปยัง GitHub

### 1. สร้าง Repository
1. ไปที่ https://github.com
2. คลิก "New repository"
3. ตั้งชื่อ repository เช่น "barcode-reader"
4. เลือก "Public" หรือ "Private"
5. ไม่ต้องเลือก "Add README file" (เพราะเรามีแล้ว)
6. คลิก "Create repository"

### 2. อัปโหลดไฟล์
**วิธีที่ 1: ผ่าน GitHub Web Interface**
1. ในหน้า repository ที่เพิ่งสร้าง
2. คลิก "uploading an existing file"
3. ลากไฟล์ทั้งหมดจากโฟลเดอร์ `github_files/` มาวาง
4. ใส่ commit message "Initial commit"
5. คลิก "Commit changes"

**วิธีที่ 2: ผ่าน Git Command Line** (ถ้ามี Git ติดตั้ง)
```bash
git clone https://github.com/username/repository-name.git
cd repository-name
# คัดลอกไฟล์จาก github_files/ มาใส่
git add .
git commit -m "Initial commit"
git push
```

### 3. เปิดใช้งาน GitHub Actions
1. ไปที่แท็บ "Actions" ใน repository
2. GitHub จะเจอไฟล์ workflow อัตโนมัติ
3. คลิก "I understand my workflows, go ahead and enable them"

### 4. สร้าง Release แรกเพื่อ Build EXE
1. ไปที่แท็บ "Releases"
2. คลิก "Create a new release"
3. ใส่ Tag version: `v1.0.0`
4. ใส่ Release title: `Barcode Reader v1.0.0`
5. ใส่คำอธิบาย:
   ```
   ## Barcode Reader เวอร์ชันแรก
   
   ### คุณสมบัติ
   - อ่าน Barcode จากไฟล์ภาพ JPG/JPEG
   - เปลี่ยนชื่อไฟล์อัตโนมัติ
   - รองรับประมวลผลหลายไฟล์และทั้งโฟลเดอร์
   - ใช้งานได้โดยไม่ต้องติดตั้งโปรแกรมเพิ่มเติม
   ```
6. คลิก "Publish release"

### 5. รอ Build เสร็จ
- GitHub Actions จะเริ่มทำงานอัตโนมัติ
- ใช้เวลาประมาณ 5-10 นาที
- ไฟล์ `BarcodeReader.exe` จะปรากฏในหน้า Release

## การใช้งาน EXE ที่ Build แล้ว

1. ดาวน์โหลดไฟล์ `BarcodeReader.exe` จากหน้า Release
2. วางไฟล์ในโฟลเดอร์ที่ต้องการ
3. เรียกใช้โปรแกรมโดยไม่ต้องติดตั้ง
4. โปรแกรมจะเปลี่ยนชื่อไฟล์ในตำแหน่งเดิม

## หมายเหตุ

- EXE ที่สร้างจะมีขนาดประมาณ 200-300 MB
- ใช้งานได้บน Windows 10/11
- ไม่ต้องติดตั้ง Python หรือไลบรารีเพิ่มเติม
- รองรับไฟล์ .jpg และ .jpeg เท่านั้น

## การแก้ไขปัญหา

### ถ้า GitHub Actions ล้มเหลว
1. ตรวจสอบไฟล์ `.github/workflows/build-exe.yml`
2. ดูใน "Actions" tab ว่าข้อผิดพลาดคืออะไร
3. แก้ไขและ push ใหม่

### ถ้า EXE ไม่ทำงาน
1. ตรวจสอบ Windows Defender
2. รันด้วยสิทธิ์ Administrator
3. ตรวจสอบว่าไฟล์ไม่เสียหาย