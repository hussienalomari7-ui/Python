# ==========================================================
# Chapter 7 - Array-Oriented Programming with NumPy
# Educational / Academic Version
# This script explains the main NumPy ideas step by step.
# ==========================================================

# -----------------------------
# 1) IMPORTS
# -----------------------------
import numpy as np                      # استيراد مكتبة NumPy واختصارها إلى np لأنها الطريقة القياسية
import math                             # سنستخدمها للمقارنة بين Python العادي و NumPy
import time                             # لقياس الزمن بشكل تقريبي في مثال الأداء

# ملاحظة:
# من الأفضل استعمال:
# import numpy as np
# بدل:
# from numpy import *
# حتى لا يحدث تعارض أسماء مع دوال Python الأساسية.


# -----------------------------
# 2) CREATING ARRAYS FROM EXISTING DATA
# -----------------------------
print("\n" + "=" * 60)
print("2) Creating arrays from existing data")
print("=" * 60)

numbers = np.array([2, 3, 5, 7, 11])   # إنشاء مصفوفة 1D من قائمة Python
print("numbers =", numbers)             # طباعة المصفوفة
print("type(numbers) =", type(numbers)) # نوع الكائن: ndarray

matrix = np.array([[1, 2, 3],           # إنشاء مصفوفة 2D من قائمة داخل قائمة
                   [4, 5, 6]])
print("matrix =\n", matrix)             # عرض المصفوفة الثنائية

# 1D array يسمى غالبًا vector
# 2D array يسمى غالبًا matrix


# -----------------------------
# 3) ARRAY ATTRIBUTES
# -----------------------------
print("\n" + "=" * 60)
print("3) Array attributes")
print("=" * 60)

x3 = np.random.randint(10, size=(5, 4, 5))  # إنشاء مصفوفة 3D عشوائية أبعادها (5,4,5)

print("x3.ndim =", x3.ndim)             # عدد الأبعاد
print("x3.shape =", x3.shape)           # شكل المصفوفة
print("x3.size =", x3.size)             # عدد العناصر الكلي
print("x3.dtype =", x3.dtype)           # نوع البيانات داخل المصفوفة
print("x3.itemsize =", x3.itemsize)     # حجم العنصر الواحد بالبايت
print("x3.nbytes =", x3.nbytes)         # الحجم الكلي للمصفوفة بالبايت


# -----------------------------
# 4) ITERATING THROUGH ARRAYS
# -----------------------------
print("\n" + "=" * 60)
print("4) Iterating through arrays")
print("=" * 60)

integers = np.array([[1, 2, 3],
                     [4, 5, 6]])        # مصفوفة 2D للتكرار عليها

print("Iterate row by row:")
for row in integers:                    # المرور على كل صف
    for column in row:                  # المرور على كل عنصر داخل الصف
        print(column, end=" ")          # طباعة العنصر في نفس السطر
    print()                             # الانتقال لسطر جديد بعد انتهاء الصف

print("Iterate as 1D using flat:")
for value in integers.flat:             # flat يعامل كل العناصر كسلسلة 1D
    print(value, end=" ")
print()


# -----------------------------
# 5) 1D, ROW VECTOR, COLUMN VECTOR
# -----------------------------
print("\n" + "=" * 60)
print("5) 1D vector vs row/column vector")
print("=" * 60)

x = np.array([1, 2, 3, 4])              # متجه 1D
x_row = np.array([[1, 2, 3, 4]])        # متجه صف Row Vector
x_col = np.array([[1], [2], [3], [4]])  # متجه عمود Column Vector

print("x.shape =", x.shape)             # الشكل (4,) يعني 1D فقط
print("x_row.shape =", x_row.shape)     # الشكل (1,4)
print("x_col.shape =", x_col.shape)     # الشكل (4,1)


# -----------------------------
# 6) FILLING ARRAYS WITH SPECIFIC VALUES
# -----------------------------
print("\n" + "=" * 60)
print("6) Filling arrays with specific values")
print("=" * 60)

zeros_arr = np.zeros(5)                 # إنشاء مصفوفة كلها أصفار
ones_arr = np.ones((2, 4), dtype=int)   # إنشاء مصفوفة كلها 1 بنوع int
full_arr = np.full((3, 5), 13)          # إنشاء مصفوفة كلها 13
eye_arr = np.eye(3)                     # إنشاء Identity Matrix
empty_arr = np.empty((2, 3))            # حجز ذاكرة فقط وقد تحتوي قيمًا غير مهيأة

print("zeros_arr =", zeros_arr)
print("ones_arr =\n", ones_arr)
print("full_arr =\n", full_arr)
print("eye_arr =\n", eye_arr)
print("empty_arr =\n", empty_arr)       # قد تظهر قيم غير متوقعة


# -----------------------------
# 7) CREATING ARRAYS FROM RANGES
# -----------------------------
print("\n" + "=" * 60)
print("7) Creating arrays from ranges")
print("=" * 60)

arr1 = np.arange(10)                    # من 0 إلى 9
arr2 = np.arange(2, 12)                 # من 2 إلى 11
arr3 = np.arange(2, 12, 0.5)            # خطوة 0.5
arr4 = np.linspace(0.0, 1.0, num=5)     # تقسيم منتظم يشمل النهاية
rand_ints = np.random.randint(10, size=(2, 2))  # أعداد صحيحة عشوائية
rand_norm = np.random.randn(2, 3)       # توزيع طبيعي قياسي
rand_uni = np.random.rand(2, 5)         # توزيع منتظم بين 0 و 1

print("np.arange(10) =", arr1)
print("np.arange(2, 12) =", arr2)
print("np.arange(2, 12, 0.5) =", arr3)
print("np.linspace(0.0, 1.0, num=5) =", arr4)
print("rand_ints =\n", rand_ints)
print("rand_norm =\n", rand_norm)
print("rand_uni =\n", rand_uni)


# -----------------------------
# 8) TYPE CASTING WITH astype
# -----------------------------
print("\n" + "=" * 60)
print("8) Type casting with astype")
print("=" * 60)

arr = np.array([1.2, 2.7, 3.9])         # مصفوفة float
int_arr = arr.astype(np.int64)          # تحويل العناصر إلى int64
numeric_strings = np.array(['1.25', '-9.6', '42'])  # نصوص تمثل أرقامًا
converted = numeric_strings.astype(float)            # تحويل النصوص إلى أرقام float

print("Original arr =", arr)
print("int_arr =", int_arr)
print("numeric_strings =", numeric_strings)
print("converted =", converted)


# -----------------------------
# 9) RESHAPING
# -----------------------------
print("\n" + "=" * 60)
print("9) Reshaping")
print("=" * 60)

reshaped = np.arange(1, 21).reshape(4, 5)  # إعادة تشكيل 20 عنصرًا إلى 4x5
print("reshaped =\n", reshaped)

# ملاحظة:
# يجب أن يبقى عدد العناصر ثابتًا أثناء reshape


# -----------------------------
# 10) LIST VS ARRAY PERFORMANCE
# -----------------------------
print("\n" + "=" * 60)
print("10) Performance: Python list vs NumPy array")
print("=" * 60)

N = 100000                              # عدد العناصر للاختبار

start = time.perf_counter()             # بداية قياس زمن Python العادي
x_list = [math.sin(x) for x in range(N)]# تطبيق sin باستخدام list comprehension
list_time = time.perf_counter() - start # نهاية القياس

start = time.perf_counter()             # بداية قياس NumPy
x_np = np.sin(np.arange(N))             # تطبيق sin على كامل المصفوفة دفعة واحدة
numpy_time = time.perf_counter() - start# نهاية القياس

print(f"Python list time  : {list_time:.6f} sec")
print(f"NumPy array time  : {numpy_time:.6f} sec")
print("Same first 5 results?")
print("list  :", x_list[:5])
print("numpy :", x_np[:5])

# في Jupyter عادة نستعمل:
# %timeit
# لكنه ليس أمر Python عادي، بل magic command في IPython/Jupyter.


# -----------------------------
# 11) ARRAY OPERATORS
# -----------------------------
print("\n" + "=" * 60)
print("11) Array operators")
print("=" * 60)

numbers = np.arange(1, 6)               # [1 2 3 4 5]
numbers2 = np.linspace(1.1, 5.5, 5)     # [1.1 2.2 3.3 4.4 5.5]

print("numbers =", numbers)
print("numbers2 =", numbers2)

print("numbers + 2 =", numbers + 2)     # جمع scalar على كل العناصر
print("numbers * 2 =", numbers * 2)     # ضرب scalar على كل العناصر
print("numbers ** 3 =", numbers ** 3)   # رفع كل عنصر للقوة 3
print("numbers * numbers2 =", numbers * numbers2)  # ضرب عنصر-بعنصر

numbers_copy = numbers.copy()           # نسخة مستقلة حتى لا نغيّر الأصل
numbers_copy += 10                      # جمع تراكمي inplace
print("numbers_copy after += 10 =", numbers_copy)


# -----------------------------
# 12) BROADCASTING
# -----------------------------
print("\n" + "=" * 60)
print("12) Broadcasting")
print("=" * 60)

a = np.arange(3)                        # [0 1 2]
print("a + 5 =", a + 5)                 # كأن 5 تم تمديدها إلى [5 5 5]

numbers3 = np.arange(1, 7).reshape(2, 3) # مصفوفة 2x3
numbers4 = np.array([2, 4, 6])           # مصفوفة 1D طولها 3

print("numbers3 =\n", numbers3)
print("numbers4 =", numbers4)
print("numbers3 * numbers4 =\n", numbers3 * numbers4)  # تمديد الأبعاد تلقائيًا

# مثال إضافي يوضح القاعدة:
a1 = np.ones((1, 3, 5))                # شكل (1,3,5)
a2 = np.ones((4, 1, 1))                # شكل (4,1,1)
a3 = a1 + a2                           # النتيجة شكلها (4,3,5)
print("a3.shape =", a3.shape)


# -----------------------------
# 13) COMPARISONS
# -----------------------------
print("\n" + "=" * 60)
print("13) Comparisons")
print("=" * 60)

numbers = np.array([11, 12, 13, 14, 15])   # مصفوفة للمقارنات
numbers2 = np.array([1.1, 2.2, 3.3, 4.4, 5.5])

print("numbers >= 13 ->", numbers >= 13)   # نتيجة منطقية عنصر-بعنصر
print("numbers2 < numbers ->", numbers2 < numbers)
print("numbers == numbers2 ->", numbers == numbers2)
print("numbers == numbers ->", numbers == numbers)


# -----------------------------
# 14) NUMPY CALCULATION METHODS
# -----------------------------
print("\n" + "=" * 60)
print("14) NumPy calculation methods")
print("=" * 60)

grades = np.array([[87, 96, 70],
                   [100, 87, 90],
                   [94, 77, 90],
                   [100, 81, 82]])      # درجات 4 طلاب في 3 اختبارات

print("grades =\n", grades)
print("grades.sum() =", grades.sum())   # مجموع كل العناصر
print("grades.min() =", grades.min())   # أصغر قيمة
print("grades.max() =", grades.max())   # أكبر قيمة
print("grades.mean() =", grades.mean()) # المتوسط الكلي
print("grades.std() =", grades.std())   # الانحراف المعياري
print("grades.var() =", grades.var())   # التباين

print("Mean by column (axis=0) =", grades.mean(axis=0))  # متوسط كل عمود
print("Mean by row (axis=1) =", grades.mean(axis=1))     # متوسط كل صف


# -----------------------------
# 15) UNIVERSAL FUNCTIONS (ufuncs)
# -----------------------------
print("\n" + "=" * 60)
print("15) Universal functions (ufuncs)")
print("=" * 60)

numbers = np.array([1, 4, 9, 16, 25, 36])   # مربعات كاملة
print("np.sqrt(numbers) =", np.sqrt(numbers))   # الجذر التربيعي عنصر-بعنصر

numbers2 = np.arange(1, 7) * 10             # [10 20 30 40 50 60]
print("numbers2 =", numbers2)

print("np.add(numbers, numbers2) =", np.add(numbers, numbers2))           # جمع باستخدام ufunc
print("np.multiply(numbers2, 5) =", np.multiply(numbers2, 5))             # ضرب في scalar
print("np.multiply(numbers2.reshape(2,3), np.array([2,4,6])) =\n",
      np.multiply(numbers2.reshape(2, 3), np.array([2, 4, 6])))           # broadcasting

arr = np.random.randn(7) * 5                 # قيم عشوائية عشرية
remainder, whole_part = np.modf(arr)         # فصل الجزء الكسري عن الصحيح
print("arr =", arr)
print("remainder =", remainder)
print("whole_part =", whole_part)

nan_arr = np.array([1.0, np.nan, 3.5, np.nan, 5.0])  # مصفوفة فيها NaN
print("np.isnan(nan_arr) =", np.isnan(nan_arr))       # كشف القيم المفقودة

# advanced ufunc methods
print("np.add.reduce([1,2,3,4]) =", np.add.reduce([1, 2, 3, 4]))                # اختزال إلى قيمة واحدة
print("np.multiply.accumulate([1,2,3]) =", np.multiply.accumulate([1, 2, 3]))    # نتائج تراكمية

a = np.array([10, 20, 30, 40, 50])           # مصفوفة للتقسيم إلى مقاطع
print("np.add.reduceat(a, [0, 2, 4]) =", np.add.reduceat(a, [0, 2, 4]))          # اختزال على مقاطع محددة


# -----------------------------
# 16) INDEXING AND SLICING - 1D
# -----------------------------
print("\n" + "=" * 60)
print("16) Indexing and slicing - 1D")
print("=" * 60)

arr = np.arange(10)                           # [0 1 2 3 4 5 6 7 8 9]
print("arr =", arr)
print("arr[5] =", arr[5])                     # الوصول لعنصر مفرد

arr[5:8] = 12                                 # تعيين قيمة واحدة على عدة مواقع (broadcasted assignment)
print("arr after arr[5:8] = 12 ->", arr)

arr_slice = arr[5:8]                          # هذا slice عبارة عن view وليس نسخة مستقلة
print("arr_slice =", arr_slice)

arr_slice[1] = 12345                          # تعديل الـ view
print("arr after modifying arr_slice =", arr) # سيتغير الأصل أيضًا


# -----------------------------
# 17) SHALLOW COPY (VIEW) VS DEEP COPY
# -----------------------------
print("\n" + "=" * 60)
print("17) View vs Copy")
print("=" * 60)

numbers = np.arange(1, 6)                     # [1 2 3 4 5]
numbers_view = numbers.view()                 # إنشاء view يشارك نفس البيانات
numbers_copy = numbers.copy()                 # إنشاء copy مستقلة

numbers[1] *= 10                              # تعديل الأصل
print("numbers =", numbers)
print("numbers_view =", numbers_view)         # سيتأثر لأنه view
print("numbers_copy =", numbers_copy)         # لن يتأثر لأنه copy

slice_view = numbers[0:3]                     # الـ slice أيضًا view
slice_view[1] = 999                           # تعديل view
print("numbers after slice_view edit =", numbers)

deep_slice = numbers[0:3].copy()              # نسخة مستقلة من slice
deep_slice[0] = -100                          # تعديل النسخة فقط
print("deep_slice =", deep_slice)
print("numbers remains =", numbers)


# -----------------------------
# 18) INDEXING IN 2D ARRAYS
# -----------------------------
print("\n" + "=" * 60)
print("18) Indexing in 2D arrays")
print("=" * 60)

grades = np.array([[87, 96, 70],
                   [100, 87, 90],
                   [94, 77, 90],
                   [100, 81, 82]])

print("grades =\n", grades)
print("grades[0, 1] =", grades[0, 1])         # الصف 0 العمود 1
print("grades[1] =", grades[1])               # الصف الثاني كاملًا
print("grades[0:2] =\n", grades[0:2])         # أول صفين
print("grades[[1, 3]] =\n", grades[[1, 3]])   # صفوف غير متتالية
print("grades[:, 0] =", grades[:, 0])         # العمود الأول
print("grades[:, 1:3] =\n", grades[:, 1:3])   # أعمدة متتالية
print("grades[:, [0, 2]] =\n", grades[:, [0, 2]])  # أعمدة غير متتالية


# -----------------------------
# 19) BOOLEAN INDEXING
# -----------------------------
print("\n" + "=" * 60)
print("19) Boolean indexing")
print("=" * 60)

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])  # أسماء مرتبطة بالصفوف
data = np.random.randn(7, 4)                                            # بيانات عشوائية 7x4

print("names =", names)
print("data =\n", data)

mask_bob = (names == 'Bob')                    # قناع منطقي يحدد أماكن Bob
print("mask_bob =", mask_bob)
print("data[names == 'Bob'] =\n", data[mask_bob])   # اختيار صفوف Bob

print("data[names == 'Bob', 2:] =\n", data[names == 'Bob', 2:])  # صفوف Bob والأعمدة من 2 للنهاية
print("data[names == 'Bob', 3] =\n", data[names == 'Bob', 3])    # العمود الرابع لصفوف Bob

mask_not_bob = ~(names == 'Bob')               # نفي القناع
print("data[~(names == 'Bob')] =\n", data[mask_not_bob])

mask_bob_or_will = (names == 'Bob') | (names == 'Will')   # دمج شرطين باستخدام |
print("data[mask_bob_or_will] =\n", data[mask_bob_or_will])

data_copy = data.copy()                        # نسخة حتى لا نفسد data الأصلية
data_copy[data_copy < 0] = 0                   # استبدال القيم السالبة بـ 0
print("data_copy after negative->0 =\n", data_copy)


# -----------------------------
# 20) FANCY INDEXING
# -----------------------------
print("\n" + "=" * 60)
print("20) Fancy indexing")
print("=" * 60)

arr = np.empty((8, 4))                         # حجز مصفوفة 8x4
for i in range(8):                             # تعبئة كل صف بالقيمة i
    arr[i] = i

print("arr =\n", arr)
print("arr[[4, 3, 0, 6]] =\n", arr[[4, 3, 0, 6]])   # اختيار صفوف بترتيب خاص
print("arr[[-3, -5, -7]] =\n", arr[[-3, -5, -7]])   # فهرسة سالبة

arr2 = np.arange(32).reshape((8, 4))           # مصفوفة 8x4 من 0 إلى 31
print("arr2 =\n", arr2)
print("arr2[[1, 5, 7, 2], [0, 3, 1, 2]] =",
      arr2[[1, 5, 7, 2], [0, 3, 1, 2]])        # اختيار عناصر محددة بالإحداثيات

# ملاحظة:
# fancy indexing يعيد copy وليس view غالبًا.


# -----------------------------
# 21) RESHAPE VS RESIZE
# -----------------------------
print("\n" + "=" * 60)
print("21) reshape vs resize")
print("=" * 60)

grades = np.array([[87, 96, 70],
                   [100, 87, 90]])

reshaped = grades.reshape(1, 6)                # يعيد array جديدة/أو view دون تغيير الأصل
print("reshaped =\n", reshaped)
print("grades still =\n", grades)

grades_resize = grades.copy()                  # نأخذ نسخة للاستخدام مع resize
grades_resize.resize(1, 6)                     # يغير نفس المصفوفة inplace
print("grades_resize after resize =\n", grades_resize)


# -----------------------------
# 22) FLATTEN VS RAVEL
# -----------------------------
print("\n" + "=" * 60)
print("22) flatten vs ravel")
print("=" * 60)

grades = np.array([[87, 96, 70],
                   [100, 87, 90]])

flattened = grades.flatten()                   # deep copy
raveled = grades.ravel()                       # shallow copy غالبًا

flattened[0] = -1                              # تعديل النسخة المستقلة
print("After flattened[0] = -1")
print("flattened =", flattened)
print("grades =", grades)                      # الأصل لن يتغير

raveled[0] = -2                                # تعديل الـ view
print("After raveled[0] = -2")
print("raveled =", raveled)
print("grades =", grades)                      # الأصل سيتغير


# -----------------------------
# 23) TRANSPOSE
# -----------------------------
print("\n" + "=" * 60)
print("23) Transpose")
print("=" * 60)

grades = np.array([[100, 96, 70],
                   [100, 87, 90]])

print("grades =\n", grades)
print("grades.T =\n", grades.T)                # تبديل الصفوف بالأعمدة


# -----------------------------
# 24) HSTACK AND VSTACK
# -----------------------------
print("\n" + "=" * 60)
print("24) hstack and vstack")
print("=" * 60)

grades = np.array([[100, 96, 70],
                   [100, 87, 90]])

grades2 = np.array([[94, 77, 90],
                    [100, 81, 82]])

print("np.hstack((grades, grades2)) =\n", np.hstack((grades, grades2)))  # دمج أفقي
print("np.vstack((grades, grades2)) =\n", np.vstack((grades, grades2)))  # دمج رأسي


# -----------------------------
# 25) APPLICATION: IDS DATA INTEGRATION
# -----------------------------
print("\n" + "=" * 60)
print("25) Application: IDS data integration")
print("=" * 60)

# Dataset1 يحتوي على 3 ميزات رقمية
d1 = np.array([
    [3.3,  2.2, 1.1],
    [4.4, -5.5, np.nan],
    [np.nan, 6.6, 3.3]
], dtype=float)

# Dataset2 يحتوي على 4 ميزات، لكننا نريد حذف sbytes والإبقاء على dur, spkts, rate
d2 = np.array([
    [1.2,  3.4, 100, np.nan],
    [4.5, -2.1,  50, 5.3],
    [np.nan, 6.1, 330, 7.2]
], dtype=float)

# Dataset3 يحتوي على 3 ميزات فئوية/تصنيفية
d3 = np.array([
    [1, 1, 1],
    [2, 2, 0],
    [3, 3, 0],
    [2, 1, 0],
    [1, 3, 0],
    [3, 1, 1]
], dtype=float)

print("d1 =\n", d1)
print("d2 =\n", d2)
print("d3 =\n", d3)

# حذف العمود الثالث sbytes من d2 والإبقاء على الأعمدة 0 و1 و3
d2_without_sbytes = d2[:, [0, 1, 3]]          # اختيار أعمدة dur, spkts, rate فقط
print("d2_without_sbytes =\n", d2_without_sbytes)

# دمج d1 و d2_without_sbytes رأسيًا لأنهما لهما نفس عدد الأعمدة
combined_d1_d2 = np.vstack((d1, d2_without_sbytes))
print("combined_d1_d2 =\n", combined_d1_d2)

# دمج البيانات الرقمية مع d3 أفقيًا للحصول على Dataset كامل
full_dataset = np.hstack((combined_d1_d2, d3))
print("full_dataset =\n", full_dataset)

# حفظ الملف إذا رغبت
# np.save("FullDataset.npy", full_dataset)     # حفظ المصفوفة بصيغة NumPy


# -----------------------------
# 26) IDS DATA CLEANSING
# -----------------------------
print("\n" + "=" * 60)
print("26) IDS data cleansing")
print("=" * 60)

numeric_part = full_dataset[:, :3]             # أول 3 أعمدة عددية
categorical_part = full_dataset[:, 3:]         # بقية الأعمدة فئوية/تصنيفية

print("numeric_part =\n", numeric_part)
print("categorical_part =\n", categorical_part)

# 26.1) Replace NaN with column mean
nan_mask = np.isnan(numeric_part)              # كشف أماكن القيم المفقودة
col_means = np.nanmean(numeric_part, axis=0)   # متوسط كل عمود مع تجاهل NaN
numeric_clean = np.where(nan_mask, col_means, numeric_part)  # التعويض بمتوسط العمود

print("Column means =", col_means)
print("After replacing NaN =\n", numeric_clean)

# 26.2) Replace negative values with 0
numeric_clean = np.where(numeric_clean < 0, 0, numeric_clean) # كل قيمة سالبة تصبح صفرًا
print("After replacing negatives with 0 =\n", numeric_clean)

# تقريب النتائج لتظهر بشكل أوضح
numeric_clean = np.round(numeric_clean, 2)     # تقريب إلى منزلتين عشريتين
print("Rounded numeric_clean =\n", numeric_clean)

# إعادة بناء الداتا النظيفة كاملة
cleaned_dataset = np.hstack((numeric_clean, categorical_part))
print("cleaned_dataset =\n", cleaned_dataset)


# -----------------------------
# 27) BASIC ANALYSIS ON THE CLEANED DATASET
# -----------------------------
print("\n" + "=" * 60)
print("27) Basic analysis on cleaned dataset")
print("=" * 60)

feature_names = np.array(["dur", "spkts", "rate", "proto", "service", "attack_cat"])  # أسماء الأعمدة

print("Feature names =", feature_names)

# unique values لكل عمود
for i, name in enumerate(feature_names):       # المرور على الأعمدة مع الاسم
    print(f"Unique values in {name} =", np.unique(cleaned_dataset[:, i]))

# labels الفريدة لعمود التصنيف attack_cat
class_labels = np.unique(cleaned_dataset[:, -1])   # آخر عمود
print("Unique class labels =", class_labels)

# توزيع الفئات
labels, counts = np.unique(cleaned_dataset[:, -1], return_counts=True)
print("Class distribution:")
for label, count in zip(labels, counts):       # طباعة كل label مع عدد مرات ظهوره
    print(f"Class {int(label)} -> {count}")

# إحصاءات الأعمدة الرقمية
numeric_names = feature_names[:3]              # أول 3 أعمدة رقمية
numeric_data = cleaned_dataset[:, :3]          # البيانات الرقمية

for i, name in enumerate(numeric_names):       # حساب إحصاءات كل عمود رقمي
    print(f"\nStatistics for {name}:")
    print("mean =", np.mean(numeric_data[:, i]))   # المتوسط
    print("min  =", np.min(numeric_data[:, i]))    # الأصغر
    print("max  =", np.max(numeric_data[:, i]))    # الأكبر

# فحص الصفوف المكررة
unique_rows, row_counts = np.unique(cleaned_dataset, axis=0, return_counts=True)  # unique rows
duplicates_exist = np.any(row_counts > 1)      # هل يوجد أي صف مكرر؟
print("\nAre there duplicate rows?", duplicates_exist)


# -----------------------------
# 28) LARGE ARRAYS DISPLAY
# -----------------------------
print("\n" + "=" * 60)
print("28) Displaying large arrays")
print("=" * 60)

large_arr = np.arange(1, 100001).reshape(100, 1000)  # مصفوفة كبيرة جدًا
print(large_arr)                                      # NumPy سيختصر الوسط تلقائيًا


