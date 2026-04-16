# =========================================================
# Chapter: Data Visualization using Matplotlib & Seaborn
# Author: Educational Version
# الهدف: تغطية جميع أفكار الشابتر بشكل عملي وتعليمي
# =========================================================

# -------------------------------
# 1) استيراد المكتبات المطلوبة
# -------------------------------
import numpy as np                      # للتعامل مع الأرقام والمصفوفات
import pandas as pd                     # للتعامل مع الجداول والبيانات
import matplotlib.pyplot as plt         # مكتبة الرسم الأساسية
import seaborn as sns                   # مكتبة رسم مبنية فوق matplotlib
from sklearn.datasets import load_iris  # لتحميل بيانات Iris الشهيرة

# -------------------------------
# 2) إعداد الشكل العام للرسومات
# -------------------------------
sns.set_style("whitegrid")              # تفعيل نمط شبكي جميل للرسوم
plt.rcParams["figure.figsize"] = (9, 5) # تحديد الحجم الافتراضي للرسومات
plt.rcParams["font.size"] = 11          # تكبير الخط قليلًا ليكون أوضح

# -------------------------------
# 3) تحميل وتجهيز البيانات
# -------------------------------
iris_raw = load_iris()                                  # تحميل بيانات Iris
iris = pd.DataFrame(iris_raw.data, columns=iris_raw.feature_names)  # تحويلها إلى DataFrame
iris["species"] = [iris_raw.target_names[i] for i in iris_raw.target]  # إضافة اسم النوع بدل الرقم

# إعادة تسمية الأعمدة لأسماء أبسط وأسهل في الاستخدام
iris.columns = [
    "sepal_length",   # طول السبل
    "sepal_width",    # عرض السبل
    "petal_length",   # طول البتلة
    "petal_width",    # عرض البتلة
    "species"         # نوع الزهرة
]

# عرض أول خمس صفوف للتأكد من شكل البيانات
print("First 5 rows of the dataset:")
print(iris.head())                                        # طباعة أول الصفوف
print("\nDataset information:")
print(iris.describe())                                    # وصف إحصائي سريع للبيانات

# =========================================================
# 4) مقدمة: Matplotlib vs Seaborn
# =========================================================
# Matplotlib:
# - أكثر مرونة وتخصيصًا
# - مناسب عندما نريد التحكم الكامل في الرسم
#
# Seaborn:
# - أسهل وأجمل بشكل افتراضي
# - ممتاز للرسومات الإحصائية
#
# سنستخدم المكتبتين معًا لنرى الفرق عمليًا

# =========================================================
# 5) Visualizing Distributions
# =========================================================
# الهدف من عرض التوزيع:
# - معرفة مدى انتشار القيم
# - معرفة المركز (Central Tendency)
# - اكتشاف الانحراف (Skewness)
# - ملاحظة القيم الشاذة (Outliers)

# -------------------------------
# 5.1 رسم Boxplot لمعرفة القيم الشاذة
# -------------------------------
plt.figure()                                              # إنشاء شكل جديد
sns.boxplot(x=iris["sepal_length"])                       # رسم Boxplot لطول السبل
plt.title("Boxplot of Sepal Length")                      # عنوان الرسم
plt.xlabel("Sepal Length")                                # تسمية المحور الأفقي
plt.show()                                                # عرض الرسم

# -------------------------------
# 5.2 رسم Distribution Plot
# -------------------------------
plt.figure()                                              # إنشاء شكل جديد
sns.histplot(iris["sepal_length"], kde=True, bins=12)    # Histogram مع منحنى كثافة KDE
plt.title("Distribution of Sepal Length")                 # عنوان الرسم
plt.xlabel("Sepal Length")                                # اسم المحور الأفقي
plt.ylabel("Frequency")                                   # اسم المحور العمودي
plt.show()                                                # عرض الرسم

# =========================================================
# 6) Scatter Plot
# =========================================================
# Scatter Plot يستخدم لعرض العلاقة بين متغيرين رقميين
# كل نقطة تمثل ملاحظة واحدة
# من أهم استخداماته: اكتشاف العلاقات والأنماط بين المتغيرات

# -------------------------------
# 6.1 Scatter Plot باستخدام Matplotlib
# -------------------------------
plt.figure()                                                          # إنشاء شكل جديد
plt.scatter(iris["sepal_length"], iris["petal_length"], alpha=0.7)   # رسم النقاط
plt.title("Scatter Plot: Sepal Length vs Petal Length")              # عنوان الرسم
plt.xlabel("Sepal Length")                                           # المحور الأفقي
plt.ylabel("Petal Length")                                           # المحور العمودي
plt.show()                                                           # عرض الرسم

# -------------------------------
# 6.2 Scatter Plot ملون حسب الفئة باستخدام Seaborn
# -------------------------------
plt.figure()                                                         # إنشاء شكل جديد
sns.scatterplot(
    data=iris,                                                       # مصدر البيانات
    x="sepal_length",                                                # المتغير على المحور X
    y="petal_length",                                                # المتغير على المحور Y
    hue="species",                                                   # تلوين النقاط حسب النوع
    s=80                                                             # حجم النقاط
)
plt.title("Scatter Plot Colored by Species")                         # عنوان الرسم
plt.xlabel("Sepal Length")                                           # اسم المحور X
plt.ylabel("Petal Length")                                           # اسم المحور Y
plt.legend(title="Species")                                          # إظهار وسيلة الإيضاح
plt.show()                                                           # عرض الرسم

# =========================================================
# 7) Line Plot
# =========================================================
# Line Plot مناسب للبيانات المستمرة
# ويُستخدم لتتبع التغيرات والاتجاهات مع الزمن أو التسلسل

# سننشئ بيانات افتراضية تمثل درجات طالب خلال 6 اختبارات
tests = ["Test 1", "Test 2", "Test 3", "Test 4", "Test 5", "Test 6"]  # أسماء الاختبارات
scores = [60, 68, 72, 78, 85, 90]                                     # درجات الطالب

# -------------------------------
# 7.1 Line Plot باستخدام Matplotlib
# -------------------------------
plt.figure()                                              # إنشاء شكل جديد
plt.plot(
    tests,                                                # المحور الأفقي
    scores,                                               # المحور العمودي
    marker="o",                                           # وضع نقطة على كل قيمة
    linewidth=2                                           # زيادة سماكة الخط
)
plt.title("Student Progress Over Tests")                  # عنوان الرسم
plt.xlabel("Tests")                                       # تسمية المحور X
plt.ylabel("Score")                                       # تسمية المحور Y
plt.ylim(0, 100)                                          # تحديد مدى المحور الرأسي
plt.show()                                                # عرض الرسم

# -------------------------------
# 7.2 Line Plot لمقارنة مجموعتين
# -------------------------------
student_a = [60, 68, 72, 78, 85, 90]                      # درجات الطالب الأول
student_b = [55, 65, 70, 74, 80, 88]                      # درجات الطالب الثاني

plt.figure()                                              # إنشاء شكل جديد
plt.plot(tests, student_a, marker="o", label="Student A") # رسم خط الطالب الأول
plt.plot(tests, student_b, marker="s", label="Student B") # رسم خط الطالب الثاني
plt.title("Comparison of Two Students Over Time")         # عنوان الرسم
plt.xlabel("Tests")                                       # اسم المحور X
plt.ylabel("Score")                                       # اسم المحور Y
plt.ylim(0, 100)                                          # تحديد المجال الرأسي
plt.legend()                                              # عرض وسيلة الإيضاح
plt.show()                                                # عرض الرسم

# =========================================================
# 8) Bar Chart
# =========================================================
# Bar Chart يستخدم لمقارنة القيم بين الفئات المختلفة
# مناسب جدًا للبيانات الفئوية (Categorical Data)

# سنحسب متوسط طول البتلة لكل نوع زهرة
avg_petal_length = iris.groupby("species")["petal_length"].mean()    # حساب المتوسط لكل فئة

# -------------------------------
# 8.1 Bar Chart باستخدام Matplotlib
# -------------------------------
plt.figure()                                              # إنشاء شكل جديد
plt.bar(
    avg_petal_length.index,                               # أسماء الفئات على المحور X
    avg_petal_length.values                               # القيم على المحور Y
)
plt.title("Average Petal Length by Species")              # عنوان الرسم
plt.xlabel("Species")                                     # تسمية المحور X
plt.ylabel("Average Petal Length")                        # تسمية المحور Y
plt.show()                                                # عرض الرسم

# -------------------------------
# 8.2 Bar Chart أفقي باستخدام Seaborn
# -------------------------------
plt.figure()                                              # إنشاء شكل جديد
sns.barplot(
    data=iris,                                            # مصدر البيانات
    x="petal_length",                                     # القيم العددية
    y="species",                                          # الفئات
    estimator=np.mean                                     # حساب المتوسط
)
plt.title("Average Petal Length by Species (Horizontal)") # عنوان الرسم
plt.xlabel("Average Petal Length")                        # المحور الأفقي
plt.ylabel("Species")                                     # المحور العمودي
plt.show()                                                # عرض الرسم

# =========================================================
# 9) Histogram
# =========================================================
# Histogram يعرض توزيع البيانات العددية داخل فترات (Bins)
# ويساعدنا على فهم شكل التوزيع وعدد القيم في كل مجال

# -------------------------------
# 9.1 Histogram باستخدام Matplotlib
# -------------------------------
plt.figure()                                              # إنشاء شكل جديد
plt.hist(
    iris["petal_length"],                                 # المتغير المراد رسم توزيعه
    bins=10,                                              # عدد الصناديق (الفترات)
    edgecolor="black"                                     # لون حدود الأعمدة
)
plt.title("Histogram of Petal Length")                    # عنوان الرسم
plt.xlabel("Petal Length")                                # تسمية المحور X
plt.ylabel("Frequency")                                   # تسمية المحور Y
plt.show()                                                # عرض الرسم

# -------------------------------
# 9.2 Histogram باستخدام Seaborn
# -------------------------------
plt.figure()                                              # إنشاء شكل جديد
sns.histplot(
    data=iris,                                            # مصدر البيانات
    x="petal_length",                                     # المتغير
    bins=10,                                              # عدد الفترات
    kde=True                                              # إضافة منحنى كثافة
)
plt.title("Histogram of Petal Length with KDE")           # عنوان الرسم
plt.xlabel("Petal Length")                                # المحور X
plt.ylabel("Frequency")                                   # المحور Y
plt.show()                                                # عرض الرسم
