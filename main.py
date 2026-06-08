def export_report():
    p_id = input("أدخل رقم (ID) المريض لاستخراج التقرير: ")
    conn = sqlite3.connect('al_yusr_lab.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients WHERE id=?", (p_id,))
    row = cursor.fetchone()
    
    if row:
        status = get_status(row[4], row[6], row[7])
        filename = f"Report_{row[1]}_{row[0]}.txt"
        
        # تنسيق التقرير بشكل احترافي
        report_content = f"""
======================================
       معمل اليُسر للتحاليل الطبية
======================================
التاريخ      : {row[8]}
رقم السجل    : {row[0]}
اسم المريض   : {row[1]}
العمر        : {row[2]}
--------------------------------------
التحليل      : {row[3]}
النتيجة      : {row[4]} {row[5]}
الحالة       : {status}
النطاق الطبيعي: {row[6]} - {row[7]}
--------------------------------------
توقيع المختبر: ____________________
======================================
"""
        with open(filename, "w", encoding="utf-8") as f:
            f.write(report_content)
        print(f"\n✅ تم إنشاء التقرير بنجاح!")
        print(f"📂 اسم الملف: {filename}")
    else:
        print("❌ المريض غير موجود في السجلات.")
    conn.close()