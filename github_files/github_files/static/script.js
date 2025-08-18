// Barcode Reader App JavaScript

document.addEventListener('DOMContentLoaded', function() {
    const uploadForm = document.getElementById('uploadForm');
    const filesInput = document.getElementById('files');
    const uploadBtn = document.getElementById('uploadBtn');
    const loadingModal = new bootstrap.Modal(document.getElementById('loadingModal'));
    
    // File selection feedback
    filesInput.addEventListener('change', function() {
        const fileCount = this.files.length;
        const uploadBtn = document.getElementById('uploadBtn');
        
        if (fileCount > 0) {
            uploadBtn.innerHTML = `
                <i class="fas fa-cogs me-2"></i>
                ประมวลผล ${fileCount} ไฟล์
            `;
            uploadBtn.disabled = false;
            
            // Validate file types and sizes
            let validFiles = 0;
            let invalidFiles = [];
            const maxSize = 16 * 1024 * 1024; // 16MB
            
            for (let file of this.files) {
                const fileExtension = file.name.split('.').pop().toLowerCase();
                
                if (!['jpg', 'jpeg'].includes(fileExtension)) {
                    invalidFiles.push(`${file.name} - ไฟล์ต้องเป็น .jpg หรือ .jpeg`);
                } else if (file.size > maxSize) {
                    invalidFiles.push(`${file.name} - ขนาดไฟล์เกิน 16 MB`);
                } else {
                    validFiles++;
                }
            }
            
            // Show validation results
            const existingAlert = document.querySelector('.file-validation-alert');
            if (existingAlert) {
                existingAlert.remove();
            }
            
            if (invalidFiles.length > 0) {
                const alertDiv = document.createElement('div');
                alertDiv.className = 'alert alert-warning file-validation-alert mt-2';
                alertDiv.innerHTML = `
                    <i class="fas fa-exclamation-triangle me-2"></i>
                    <strong>พบไฟล์ที่ไม่รองรับ:</strong>
                    <ul class="mb-0 mt-2">
                        ${invalidFiles.map(error => `<li>${error}</li>`).join('')}
                    </ul>
                `;
                filesInput.parentNode.appendChild(alertDiv);
            }
            
            if (validFiles === 0) {
                uploadBtn.disabled = true;
                uploadBtn.innerHTML = `
                    <i class="fas fa-exclamation-triangle me-2"></i>
                    ไม่มีไฟล์ที่ถูกต้อง
                `;
            }
            
        } else {
            uploadBtn.innerHTML = `
                <i class="fas fa-cogs me-2"></i>
                ประมวลผลไฟล์
            `;
            uploadBtn.disabled = true;
        }
    });
    
    // Form submission
    uploadForm.addEventListener('submit', function(e) {
        if (filesInput.files.length === 0) {
            e.preventDefault();
            alert('กรุณาเลือกไฟล์ก่อนส่ง');
            return;
        }
        
        // Show loading modal
        loadingModal.show();
        
        // Disable form elements
        uploadBtn.disabled = true;
        filesInput.disabled = true;
        
        // Update button text
        uploadBtn.innerHTML = `
            <span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>
            กำลังประมวลผล...
        `;
    });
    
    // Hide loading modal when page loads (in case of redirect back)
    window.addEventListener('load', function() {
        loadingModal.hide();
    });
    
    // Auto-dismiss alerts after 5 seconds
    document.querySelectorAll('.alert-dismissible').forEach(function(alert) {
        setTimeout(function() {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
    
    // Drag and drop functionality
    const dropZone = document.querySelector('.card-body');
    let dragCounter = 0;
    
    dropZone.addEventListener('dragenter', function(e) {
        e.preventDefault();
        dragCounter++;
        this.classList.add('drag-over');
    });
    
    dropZone.addEventListener('dragleave', function(e) {
        e.preventDefault();
        dragCounter--;
        if (dragCounter === 0) {
            this.classList.remove('drag-over');
        }
    });
    
    dropZone.addEventListener('dragover', function(e) {
        e.preventDefault();
    });
    
    dropZone.addEventListener('drop', function(e) {
        e.preventDefault();
        this.classList.remove('drag-over');
        dragCounter = 0;
        
        const files = e.dataTransfer.files;
        if (files.length > 0) {
            filesInput.files = files;
            // Trigger change event
            const event = new Event('change', { bubbles: true });
            filesInput.dispatchEvent(event);
        }
    });
    
    // Add drag over styles
    const style = document.createElement('style');
    style.textContent = `
        .drag-over {
            border: 2px dashed var(--bs-primary) !important;
            background-color: var(--bs-primary-bg-subtle) !important;
            transition: all 0.3s ease;
        }
    `;
    document.head.appendChild(style);
    
    // Download progress feedback
    document.querySelectorAll('a[href*="/download/"]').forEach(function(link) {
        link.addEventListener('click', function(e) {
            const btn = this;
            const originalHTML = btn.innerHTML;
            
            btn.innerHTML = `
                <span class="spinner-border spinner-border-sm me-1" role="status" aria-hidden="true"></span>
                กำลังดาวน์โหลด...
            `;
            btn.classList.add('disabled');
            
            // Reset button after 3 seconds
            setTimeout(function() {
                btn.innerHTML = originalHTML;
                btn.classList.remove('disabled');
            }, 3000);
        });
    });
    
    // Keyboard shortcuts
    document.addEventListener('keydown', function(e) {
        // Ctrl+U or Cmd+U to focus file input
        if ((e.ctrlKey || e.metaKey) && e.key === 'u') {
            e.preventDefault();
            filesInput.click();
        }
        
        // Escape to clear selection
        if (e.key === 'Escape') {
            if (filesInput.files.length > 0) {
                filesInput.value = '';
                const event = new Event('change', { bubbles: true });
                filesInput.dispatchEvent(event);
            }
        }
    });
    
    // Show keyboard shortcuts tooltip
    const shortcutsTooltip = `
        <div class="position-fixed bottom-0 end-0 p-3" style="z-index: 1000;">
            <div class="toast show" role="alert">
                <div class="toast-header">
                    <i class="fas fa-keyboard me-2"></i>
                    <strong class="me-auto">คีย์ลัด</strong>
                    <button type="button" class="btn-close" data-bs-dismiss="toast"></button>
                </div>
                <div class="toast-body">
                    <small>
                        <strong>Ctrl+U:</strong> เลือกไฟล์<br>
                        <strong>Esc:</strong> ยกเลิกการเลือก
                    </small>
                </div>
            </div>
        </div>
    `;
    
    // Show shortcuts tooltip after 3 seconds if no files are selected
    setTimeout(function() {
        if (filesInput.files.length === 0 && !localStorage.getItem('shortcuts-shown')) {
            document.body.insertAdjacentHTML('beforeend', shortcutsTooltip);
            localStorage.setItem('shortcuts-shown', 'true');
        }
    }, 3000);
});
