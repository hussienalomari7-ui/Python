# =========================================================
# Chapter 5 - Getting Started with pandas
# Educational & Academic Script
# Covers:
# 1) Importing pandas and NumPy
# 2) Series
# 3) DataFrame
# 4) Index Objects
# 5) Data Cleaning and Exploration
# =========================================================

import pandas as pd                  # استيراد مكتبة pandas للتعامل مع البيانات الجدولية
import numpy as np                   # استيراد NumPy للعمليات العددية والمصفوفات

# ---------------------------------------------------------
# 0) CHECK LIBRARY VERSION
# ---------------------------------------------------------
print("Pandas version:", pd.__version__)   # طباعة إصدار pandas للتأكد من البيئة البرمجية

# =========================================================
# 1) SERIES
# =========================================================
print("\n" + "=" * 60)
print("1) SERIES")
print("=" * 60)

# إنشاء Series بسيطة بدون index مخصص
obj = pd.Series([4, 7, -5, 3])      # إنشاء سلسلة بيانات أحادية البعد
print("\nBasic Series:")
print(obj)                          # عرض السلسلة

print("\nSeries values:", obj.values)   # استخراج القيم فقط كمصفوفة
print("Series index:", obj.index)       # استخراج الفهرس الخاص بالسلسلة

# إنشاء Series مع index مخصص
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])   # إنشاء Series بعناوين مخصصة
print("\nSeries with custom index:")
print(obj2)

print("\nValue at index 'a':", obj2['a'])   # الوصول لقيمة باستخدام label
obj2['d'] = 6                               # تعديل قيمة عنصر معين باستخدام label
print("\nAfter updating index 'd':")
print(obj2)

print("\nSelecting multiple labels ['c', 'a', 'd']:")
print(obj2[['c', 'a', 'd']])               # اختيار أكثر من عنصر باستخدام قائمة labels

# عمليات على Series
print("\nPositive values only:")
print(obj2[obj2 > 0])                      # تصفية القيم الموجبة فقط

print("\nSeries * 2:")
print(obj2 * 2)                            # ضرب كل عنصر في 2

print("\nExponential of Series:")
print(np.exp(obj2))                        # تطبيق دالة رياضية على السلسلة

# بعض الدوال الإحصائية على Series
ages = pd.Series([4, 7, 5, 3])             # إنشاء Series تمثل أعمارًا أو قيمًا عددية
print("\nSeries statistics:")
print("Mean:", ages.mean())                # المتوسط الحسابي
print("Min :", ages.min())                 # أقل قيمة
print("Max :", ages.max())                 # أكبر قيمة
print("Median:", ages.median())            # الوسيط
print("Unique values:", ages.unique())     # القيم الفريدة

# Series من dict
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}   # قاموس بيانات
obj3 = pd.Series(sdata)                    # تحويل القاموس إلى Series
print("\nSeries created from dict:")
print(obj3)

states = ['California', 'Ohio', 'Oregon', 'Texas']   # قائمة index مخصصة
obj4 = pd.Series(sdata, index=states)                # إعادة ترتيب وربط القيم حسب states
print("\nSeries with custom index from dict:")
print(obj4)

# التحقق من القيم المفقودة
print("\nMissing values check using isnull():")
print(obj4.isnull())                      # إرجاع True للقيم المفقودة

print("\nNot-null values check using notnull():")
print(pd.notnull(obj4))                   # إرجاع True للقيم غير المفقودة

# المحاذاة التلقائية حسب index
print("\nAutomatic alignment in arithmetic operations:")
print(obj3 + obj4)                        # الجمع يتم حسب أسماء الـ index وليس حسب الترتيب

# تسمية السلسلة والفهرس
obj4.name = 'population'                  # تسمية السلسلة
obj4.index.name = 'state'                 # تسمية الفهرس
print("\nNamed Series:")
print(obj4)

# تعديل index بالكامل
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']   # استبدال أسماء الفهرس
print("\nSeries after replacing index:")
print(obj)

# خصائص مهمة في Series
print("\nSeries attributes:")
print("dtype :", obj2.dtype)              # نوع بيانات السلسلة
print("shape :", obj2.shape)              # أبعاد السلسلة
print("size  :", obj2.size)               # عدد العناصر
print("loc['b']:", obj2.loc['b'])         # الوصول باستخدام label
print("iloc[1]:", obj2.iloc[1])           # الوصول باستخدام الموقع العددي

# =========================================================
# 2) DATAFRAME
# =========================================================
print("\n" + "=" * 60)
print("2) DATAFRAME")
print("=" * 60)

# إنشاء DataFrame من dict of lists
data = {
    'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],   # عمود الولاية
    'year': [2000, 2001, 2002, 2001, 2002, 2003],                      # عمود السنة
    'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]                              # عمود السكان
}

frame = pd.DataFrame(data)                 # إنشاء DataFrame
print("\nBasic DataFrame:")
print(frame)

print("\nFirst 5 rows using head():")
print(frame.head())                        # عرض أول 5 صفوف

print("\nFirst 3 rows using head(3):")
print(frame.head(3))                       # عرض أول 3 صفوف

# ترتيب الأعمدة يدويًا
frame_ordered = pd.DataFrame(data, columns=['pop', 'state', 'year'])   # تحديد ترتيب الأعمدة
print("\nDataFrame with reordered columns:")
print(frame_ordered)

# إضافة عمود غير موجود مسبقًا
frame2 = pd.DataFrame(
    data,
    columns=['year', 'state', 'pop', 'debt'],                          # debt غير موجود أصلًا
    index=['one', 'two', 'three', 'four', 'five', 'six']              # index مخصص للصفوف
)
print("\nDataFrame with custom index and extra column:")
print(frame2)

print("\nColumns of frame2:")
print(frame2.columns)                     # أسماء الأعمدة

# الوصول إلى عمود
print("\nColumn 'state' using bracket notation:")
print(frame2['state'])                    # العمود يرجع كـ Series

print("\nColumn 'year' using attribute notation:")
print(frame2.year)                        # الوصول للعمود كخاصية إذا كان الاسم صالحًا

# الوصول إلى صف باستخدام loc
print("\nRow 'three' using loc:")
print(frame2.loc['three'])                # استرجاع صف كامل باستخدام label

# تعديل عمود كامل بقيمة ثابتة
frame2['debt'] = 16.5                     # وضع نفس القيمة في كل الصفوف
print("\nAfter assigning constant value to 'debt':")
print(frame2)

# تعديل عمود كامل بمصفوفة
frame2['debt'] = np.arange(6.)            # تعبئة العمود بقيم من 0 إلى 5
print("\nAfter assigning np.arange(6.) to 'debt':")
print(frame2)

# إسناد Series إلى عمود مع محاذاة حسب index
val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])   # Series جزئية
frame2['debt'] = val                    # المحاذاة حسب أسماء الصفوف
print("\nAfter assigning Series to 'debt' with index alignment:")
print(frame2)

# إنشاء عمود جديد منطقي
frame2['eastern'] = frame2['state'] == 'Ohio'   # True إذا كانت الولاية Ohio
print("\nAfter creating boolean column 'eastern':")
print(frame2)

# حذف عمود
del frame2['eastern']                   # حذف العمود
print("\nAfter deleting 'eastern':")
print(frame2)

# الفرق بين view و copy
cl = frame2['debt'].copy()              # أخذ نسخة مستقلة لتجنب التعديل على الأصل
cl.iloc[0] = 10                         # تعديل النسخة فقط
print("\nCopied Series after modification:")
print(cl)

print("\nOriginal 'debt' column remains unchanged:")
print(frame2['debt'])

# DataFrame من nested dict
pop = {
    'Nevada': {2001: 2.4, 2002: 2.9},
    'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}
}

frame3 = pd.DataFrame(pop)              # إنشاء DataFrame من قاموس داخل قاموس
print("\nDataFrame from nested dict:")
print(frame3)

print("\nTranspose of frame3:")
print(frame3.T)                         # قلب الصفوف إلى أعمدة والعكس

print("\nDataFrame with specific index [2001, 2002, 2003]:")
print(pd.DataFrame(pop, index=[2001, 2002, 2003]))   # تحديد index معين

# DataFrame من dict of Series
pdata = {
    'Ohio': frame3['Ohio'][:-1],        # أخذ جزء من عمود Ohio
    'Nevada': frame3['Nevada'][:2]      # أخذ جزء من عمود Nevada
}
print("\nDataFrame from dict of Series:")
print(pd.DataFrame(pdata))

# أسماء الـ index والأعمدة
frame3.index.name = 'year'              # تسمية فهرس الصفوف
frame3.columns.name = 'state'           # تسمية فهرس الأعمدة
print("\nNamed index and columns:")
print(frame3)

print("\nDataFrame values as ndarray:")
print(frame3.values)                    # استخراج القيم كمصفوفة ثنائية الأبعاد

# =========================================================
# 3) INDEX OBJECTS
# =========================================================
print("\n" + "=" * 60)
print("3) INDEX OBJECTS")
print("=" * 60)

obj_index = pd.Series(range(3), index=['a', 'b', 'c'])   # Series جديدة لفهم index
index = obj_index.index                                  # استخراج index object

print("\nIndex object:")
print(index)

print("\nSliced index [1:]:")
print(index[1:])                                         # تقطيع الـ index

labels = pd.Index(["Sam", "Zac", "Al"])                  # إنشاء Index مستقل
obj_labels = pd.Series([1.5, -2.5, 0], index=labels)    # استخدامه في Series
print("\nSeries with shared Index object:")
print(obj_labels)

print("\nIs obj_labels.index the same object as labels?")
print(obj_labels.index is labels)                        # فحص الهوية وليس فقط المساواة

print("\nCheck membership:")
print("'Ohio' in frame3.columns ->", 'Ohio' in frame3.columns)   # فحص وجود label بالأعمدة
print("2003 in frame3.index ->", 2003 in frame3.index)           # فحص وجود label بالفهرس

dup_labels = pd.Index(['foo', 'foo', 'bar', 'bar'])      # Index يحتوي على تكرار
print("\nIndex with duplicate labels:")
print(dup_labels)

# عمليات set-like على index
print("\nUnion of indexes:")
print(frame2.index.union(frame3.index))                  # دمج الفهرسين

print("\nIntersection of indexes:")
print(frame2.index.intersection(frame3.index))           # العناصر المشتركة

print("\nDifference of indexes:")
print(frame2.index.difference(frame3.index))             # العناصر الموجودة في الأول فقط

# خواص وعمليات إضافية
print("\nDelete first label from frame2.index:")
print(frame2.index.delete(0))                            # حذف عنصر حسب الموقع

print("\nDrop label 'one' from frame2.index:")
print(frame2.index.drop('one'))                          # حذف حسب الاسم

print("\nInsert label 'ten' at position 0:")
print(frame2.index.insert(0, 'ten'))                     # إدراج label جديد

print("\nIs frame2.index monotonic?")
print(frame2.index.is_monotonic_increasing)              # هل القيم مرتبة تصاعديًا؟

print("\nIs frame2.index unique?")
print(frame2.index.is_unique)                            # هل الفهرس يحتوي على قيم فريدة؟

print("\nUnique labels in a duplicate index:")
print(dup_labels.unique())                               # القيم الفريدة فقط

# =========================================================
# 4) DATA CLEANING & EXPLORATION PROJECT
# =========================================================
print("\n" + "=" * 60)
print("4) DATA CLEANING & EXPLORATION PROJECT")
print("=" * 60)

# إنشاء بيانات مشابهة للمثال الموجود في الشابتر
student_data = {
    "ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],               # رقم الطالب
    "Age": [18, 19, 18, 20, 21, 17, 18, 19, 20, 21],     # العمر
    "StudyHours": [12, np.nan, 5, 8, 15, 3, 10, 7, 4, 13],   # ساعات الدراسة مع قيمة مفقودة
    "Absences": [3, 0, -1, 2, 4, 7, 1, 2, 3, 0],         # الغياب مع قيمة سالبة خاطئة
    "Assignments": [8, 10, 6, 9, 10, 5, np.nan, 8, 4, 10],   # الواجبات مع قيمة مفقودة
    "Test1": [75, 88, 40, 55, np.nan, 30, 65, 60, 35, 90],   # الاختبار الأول
    "Test2": [80, 82, 45, 60, 85, 35, 70, 62, 40, 92],       # الاختبار الثاني
    "Projects": [90, 85, 50, 70, 80, 40, 75, 65, 42, 95],    # المشاريع
    "Participation": [10, 9, 2, 8, 10, 3, 7, 6, 2, 10],      # المشاركة
    "FinalGrade": [85, 87, 48, 65, 88, 38, 72, 66, 44, 94],  # الدرجة النهائية
    "Class": ["Pass", "Pass", "Fail", "Pass", "Pass", "Fail", "Pass", "Pass", "Fail", "Pass"]  # النتيجة
}

df = pd.DataFrame(student_data)          # تحويل البيانات إلى DataFrame

print("\nOriginal Data:")
print(df)

print("\nLast 5 rows using tail():")
print(df.tail())                         # عرض آخر 5 صفوف

print("\nMissing values map:")
print(df.isnull())                       # إظهار مواقع القيم المفقودة

print("\nColumns:")
print(df.columns)                        # أسماء الأعمدة

print("\nIndex:")
print(df.index)                          # فهرس الصفوف

print("\nInfo:")
print(df.info())                         # معلومات شاملة عن الأعمدة وأنواعها

# ---------------------------------------------------------
# DATA CLEANING
# ---------------------------------------------------------
print("\n--- Data Cleaning ---")

# 1) تعويض القيم المفقودة بالوسيط median
numeric_cols = df.select_dtypes(include=[np.number]).columns   # اختيار الأعمدة العددية فقط
for col in numeric_cols:                                       # المرور على كل عمود عددي
    median_val = df[col].median()                              # حساب الوسيط
    df[col] = df[col].fillna(median_val)                       # تعويض القيم المفقودة بالوسيط

# 2) استبدال القيم السالبة في الأعمدة العددية بـ 0
for col in numeric_cols:                                       # المرور على الأعمدة العددية
    df[col] = df[col].where(df[col] >= 0, 0)                   # إذا القيمة سالبة تصبح 0

# 3) توحيد النصوص في عمود Class إلى lowercase
df["Class"] = df["Class"].str.lower()                          # تحويل pass/fail إلى حروف صغيرة

# 4) حذف الصفوف المكررة إن وجدت
df.drop_duplicates(inplace=True)                               # إزالة الصفوف المكررة من الجدول

print("\nCleaned Data:")
print(df)

# ---------------------------------------------------------
# EXPLORATORY DATA ANALYSIS
# ---------------------------------------------------------
print("\n--- Exploratory Data Analysis ---")

print("\nSummary statistics:")
print(df.describe())                                           # ملخص إحصائي للأعمدة العددية

# correlation matrix
correlations = df.corr(numeric_only=True)                      # حساب مصفوفة الارتباط
print("\nCorrelation matrix:")
print(correlations)

print("\nCorrelation with FinalGrade:")
print(correlations["FinalGrade"].sort_values(ascending=False)) # معرفة أكثر المتغيرات ارتباطًا بالدرجة النهائية

# covariance matrix
covariances = df.cov(numeric_only=True)                        # حساب مصفوفة التباين المشترك
print("\nCovariance matrix:")
print(covariances)

print("\nCorrelation between Test1 and Test2:")
print(correlations.loc["Test1", "Test2"])                      # استخراج ارتباط متغيرين محددين

# ---------------------------------------------------------
# FEATURE REDUCTION
# ---------------------------------------------------------
print("\n--- Feature Reduction ---")

# إذا كان Test1 و Test2 شديدي الارتباط، نحذف أحدهما
df_reduced = df.drop(columns=["Test1"])                        # حذف العمود Test1 لتقليل التكرار المعلوماتي
print("\nData after dropping 'Test1':")
print(df_reduced.head())

# ---------------------------------------------------------
# LABEL ENCODING
# ---------------------------------------------------------
print("\n--- Label Encoding ---")

df_reduced["Class"] = df_reduced["Class"].map({"pass": 1, "fail": 0})   # تحويل pass/fail إلى 1/0
print("\nAfter encoding 'Class':")
print(df_reduced[["ID", "Class"]])

# ---------------------------------------------------------
# SAVE CLEANED DATA
# ---------------------------------------------------------
output_file = "cleaned_student_data.csv"                       # اسم الملف النهائي
df_reduced.to_csv(output_file, index=False)                    # حفظ البيانات بعد التنظيف
print(f"\nCleaned data saved to: {output_file}")               # تأكيد عملية الحفظ

