# วิธีการ Build EXE จาก GitHub

## อัตโนมัติผ่าน GitHub Actions

### 1. สร้าง Repository บน GitHub
1. สร้าง Repository ใหม่บน GitHub
2. อัปโหลดไฟล์ทั้งหมดจากโฟลเดอร์ `github_files`
3. ตรวจสอบให้แน่ใจว่าโฟลเดอร์ `.github/workflows/` มีไฟล์ `build-exe.yml`

### 2. สร้าง Release เพื่อ Build EXE
1. ไปที่หน้า Repository บน GitHub
2. คลิก "Releases" ทางด้านขวา
3. คลิก "Create a new release"
4. ใส่ tag version เช่น `v1.0.0`
5. ใส่ title เช่น "Barcode Reader v1.0.0"
6. คลิก "Publish release"

### 3. ดาวน์โหลด EXE
1. GitHub Actions จะเริ่มทำงานอัตโนมัติ
2. รอสักครู่ให้ build เสร็จ (ประมาณ 5-10 นาที)
3. EXE จะปรากฏในหน้า Release ให้ดาวน์โหลด

## Manual Build (ในเครื่องตัวเอง)

### ความต้องการ
- Python 3.8 หรือใหม่กว่า
- Windows 10/11

### ขั้นตอน
1. **Clone Repository**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **ติดตั้ง Dependencies**
   ```bash
   pip install -r requirements_desktop.txt
   ```

3. **Build EXE**
   ```bash
   python pyinstaller_spec.py
   ```

4. **ผลลัพธ์**
   - ไฟล์ `BarcodeReader.exe` จะอยู่ในโฟลเดอร์ `dist/`
   - ไฟล์นี้สามารถใช้งานได้โดยไม่ต้องติดตั้ง Python

## การทดสอบ

### ทดสอบ Desktop App
```bash
python barcode_desktop.py
```

### ทดสอบ Web App
```bash
python app.py
```
เปิดเว็บบราวเซอร์ไปที่ `http://localhost:5000`

### ทดสอบ EXE ที่ Build แล้ว
```bash
.\dist\BarcodeReader.exe
```

## หมายเหตุ

- EXE ที่สร้างจะมีขนาดประมาณ 200-300 MB
- ใช้งานได้บน Windows โดยไม่ต้องติดตั้งโปรแกรมเพิ่มเติม
- รองรับไฟล์ .jpg และ .jpeg เท่านั้น
- หากมีปัญหาในการ build ให้ตรวจสอบ Python version และ dependencies

## การแก้ไขปัญหา

### ปัญหา: ImportError
```bash
pip install --upgrade pip
pip install -r requirements_desktop.txt
```

### ปัญหา: PyInstaller ไม่ทำงาน
```bash
pip uninstall pyinstaller
pip install pyinstaller==5.13.0
```

### ปัญหา: EXE ไม่ทำงาน
- ตรวจสอบ Windows Defender
- รันด้วยสิทธิ์ Administrator
- ตรวจสอบ dependencies ในไฟล์ `requirements_desktop.txt`