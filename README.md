Quyida `README.md` faylining to'liq kodini keltiraman. Bu fayl dasturdan foydalanish bo'yicha barcha kerakli ma'lumotlarni o'z ichiga oladi:

```markdown
# PDF Fayllarni Siqish Dasturi

Bu dastur PyQt5 kutubxonasidan foydalanib yaratilgan bo'lib, PDF fayllarni hajmini kichiklashtirish imkonini beradi. Siqilgan PDF fayl ish stoliga (`Desktop`) yuklanadi.

---

## Xususiyatlari
- PDF faylning dastlabki hajmini ko'rish.
- Faylni maksimal darajada siqish.
- Siqilgan PDF faylni avtomatik ravishda ish stoliga yuklash.
- Foydalanuvchi uchun qulay interfeys.

---

## Talablar
Dastur quyidagi talablarni talab qiladi:
- **Python**: 3.8 yoki undan yuqori versiyasi
- **Kutubxonalar**:
  - `PyQt5`
  - `PyPDF2`

---

## O'rnatish

1. Python o'rnatilganligini tekshiring:
   ```bash
   python --version
   ```

2. Kerakli kutubxonalarni o'rnating:
   ```bash
   pip install PyQt5 PyPDF2
   ```

3. Loyihani yuklab oling yoki nusxa ko'chiring.

---

## Foydalanish

1. Terminal yoki komandalar satrini oching va dasturni joylashgan papkaga o'ting:
   ```bash
   cd <papka_nom>
   ```

2. Dasturni ishga tushiring:
   ```bash
   python press_pdf.py
   ```

3. Dasturda quyidagi amallarni bajaring:
   - **Select PDF** tugmasini bosib, siqmoqchi bo'lgan PDF faylni tanlang.
   - Fayl hajmini ko'rsangiz, **Press** tugmasini bosing. Fayl maksimal darajada siqiladi.
   - Siqilgan fayl ish stoliga **`Siqilgan-pdf_tempiltin.pdf`** nomi bilan yuklanadi.

---

## Xatoliklar va Muammolar

Agar dasturda xatolik yuz bersa:
1. PDF fayli to'g'ri tanlanganligini tekshiring.
2. Terminalda chiqgan xatolik haqida ma'lumotni kuzatib, yechim izlang.
3. Kutubxonalarni yangilang:
   ```bash
   pip install --upgrade PyQt5 PyPDF2
   ```

4. Agar xatolik hal qilinmasa, ishlab chiquvchi bilan bog'laning.

---

## Dasturdan Foydalanish Qoidalari

- Siqish jarayonida dastur faqat `.pdf` formatdagi fayllarni qo'llab-quvvatlaydi.
- Siqilgan PDF fayl avtomatik ravishda ish stoliga yuklanadi.

---

## Loyihani Qayta Ishlash

Agar loyihani qayta ishlashni xohlasangiz, quyidagi amallarni bajaring:

1. Python muharririda dastur kodini oching.
2. Zarur bo'lsa, o'zgartirishlar kiritib saqlang.
3. Dasturni qayta ishga tushiring.

---

## Litsenziya

Mazkur dastur **Tempiltin** tomonidan ishlab chiqilgan. Barcha huquqlar himoyalangan.

- **Websayt:** [Tempiltin](https://tempiltin.uz)

---

## Dastur Interfeysi

Dastur interfeysi quyidagi tarkibiy qismlardan iborat:

- **Navbar**: "PDF fayllarni siqish dasturi"
- **Header**:
  - Chap tomon: Siz tanlagan PDF fayl: `<Hajmi: 0.0 MB>`
  - O'ng tomon: Siqilgan PDF fayl: `<Hajmi: 0.0 MB>`
- **Section**:
  - Chapda: "Select PDF" tugmasi
  - O'ngda: "Press" tugmasi
- **Footer**: Markazda `"Created by Tempiltin | Info: https://tempiltin.uz/"` yozuvi.

---

## Muallif

Dastur muallifi: **Tempiltin**. Agar yordam kerak bo'lsa, quyidagi manzillar orqali bog'laning:

- **Websayt:** [Tempiltin](https://tempiltin.uz)
```

Ushbu `README.md` fayli foydalanuvchilar va dasturchilar uchun to'liq qo'llanmani taqdim etadi. Agar qo'shimcha qo'llab-quvvatlash kerak bo'lsa, so'rang! 😊