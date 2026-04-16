# ============================================================
# Chapter 14 Educational Code
# Topic: Lists, Tuples, Sets, and Dictionaries
# ============================================================
# هذا الملف التعليمي يجمع أهم أفكار الشابتر في برنامج واحد
# مع أمثلة واضحة ومخرجات منظمة وتعليقات تفسيرية.
# ============================================================


# ------------------------------------------------------------
# دالة مساعدة لطباعة عنوان كل جزء بشكل جميل
# ------------------------------------------------------------
def print_title(title):
    print("\n" + "=" * 70)   # يرسم خط علوي للفصل بين الأجزاء
    print(title.center(70))  # يطبع العنوان في المنتصف
    print("=" * 70)          # يرسم خط سفلي للفصل بين الأجزاء


# ============================================================
# 1) REVIEW LISTS - مراجعة القوائم
# ============================================================
print_title("1) LISTS REVIEW - مراجعة القوائم")

# إنشاء قائمة تحتوي أنواع بيانات مختلفة
values = [32, 54, 67.5, 29, 35, 80, 115, 44.5, 100, 65]  # قائمة عناصرها أرقام صحيحة وعشرية

print("Original list:", values)                           # طباعة القائمة الأصلية
print("Length of list:", len(values))                     # عدد عناصر القائمة باستخدام len()

# الوصول إلى عنصر باستخدام الفهرس
print("Element at index 2:", values[2])                  # الوصول للعنصر الثالث لأن الفهرسة تبدأ من 0

# تعديل عنصر داخل القائمة
values[5] = 87                                           # تغيير قيمة العنصر عند الفهرس 5
print("After changing index 5:", values)                 # عرض القائمة بعد التعديل

# استخدام الفهرسة السالبة
print("Last element:", values[-1])                       # آخر عنصر في القائمة
print("Second last element:", values[-2])                # العنصر قبل الأخير


# ============================================================
# 2) LOOPING THROUGH LISTS - الدوران على القوائم
# ============================================================
print_title("2) LOOPING THROUGH LISTS - الدوران على القوائم")

# الدوران باستخدام الفهارس
print("Loop using indexes:")
for i in range(len(values)):                             # يمر على الفهارس من 0 حتى آخر فهرس
    print(f"Index {i} -> {values[i]}")                  # يطبع الفهرس والعنصر المقابل له

# الدوران المباشر على العناصر
print("\nLoop using elements directly:")
for element in values:                                   # يمر مباشرة على كل عنصر في القائمة
    print(element)                                       # يطبع العنصر الحالي


# ============================================================
# 3) LIST ALIASING VS COPYING - الربط والنسخ
# ============================================================
print_title("3) LIST ALIASING VS COPYING - الربط والنسخ")

scores = [10, 9, 7, 4, 5]                                # قائمة أصلية
alias_scores = scores                                    # هذا ليس نسخاً حقيقياً، بل اسم آخر لنفس القائمة

scores[3] = 10                                           # تعديل عنصر في القائمة الأصلية
print("scores       :", scores)                          # القائمة الأصلية بعد التعديل
print("alias_scores :", alias_scores)                    # ستتأثر لأنها تشير لنفس القائمة

# النسخ الحقيقي للقائمة
copied_scores = scores.copy()                            # إنشاء نسخة مستقلة من القائمة
scores[0] = 999                                          # تعديل القائمة الأصلية مرة أخرى

print("\nAfter true copy:")
print("scores        :", scores)                         # القائمة الأصلية بعد التعديل
print("copied_scores :", copied_scores)                  # النسخة المستقلة لن تتأثر


# ============================================================
# 4) LIST OPERATIONS - العمليات على القوائم
# ============================================================
print_title("4) LIST OPERATIONS - العمليات على القوائم")

friends = []                                             # إنشاء قائمة فارغة
friends.append("Harry")                                  # إضافة عنصر في نهاية القائمة
friends.append("Emily")                                  # إضافة عنصر آخر
friends.append("Bob")                                    # إضافة عنصر آخر
friends.append("Cari")                                   # إضافة عنصر آخر
print("After append:", friends)                          # عرض القائمة بعد الإضافة

friends.insert(1, "Cindy")                               # إدخال عنصر عند الفهرس 1
print("After insert:", friends)                          # عرض القائمة بعد الإدخال

# البحث عن عنصر
if "Cindy" in friends:                                   # التحقق هل العنصر موجود داخل القائمة
    print("Cindy is in friends list")                    # يطبع رسالة إذا كانت موجودة

# إيجاد موقع عنصر
index_of_emily = friends.index("Emily")                  # إرجاع أول فهرس لظهور Emily
print("Index of Emily:", index_of_emily)                 # طباعة الفهرس

# حذف عنصر باستخدام pop
removed_name = friends.pop(1)                            # حذف العنصر عند الفهرس 1 وإرجاعه
print("Removed name:", removed_name)                     # طباعة الاسم المحذوف
print("After pop(1):", friends)                          # عرض القائمة بعد الحذف

# حذف آخر عنصر
last_removed = friends.pop()                             # حذف آخر عنصر من القائمة
print("Last removed:", last_removed)                     # طباعة العنصر المحذوف
print("After pop():", friends)                           # عرض القائمة بعد حذف آخر عنصر

# concatenation
my_friends = ["Fritz", "Cindy"]                          # قائمة أولى
your_friends = ["Lee", "Pat", "Phuong"]                  # قائمة ثانية
our_friends = my_friends + your_friends                  # دمج القائمتين في قائمة جديدة
print("Concatenation:", our_friends)                     # عرض نتيجة الدمج

# replication
month_in_quarter = [1, 2, 3] * 4                         # تكرار القائمة 4 مرات
print("Replication:", month_in_quarter)                  # عرض النتيجة

# المقارنة
print("[1, 4, 9] == [1, 4, 9] ->", [1, 4, 9] == [1, 4, 9])   # مقارنة قائمتين متطابقتين
print("[1, 4, 9] != [4, 9] ->", [1, 4, 9] != [4, 9])         # مقارنة عدم التساوي

# دوال sum و min و max
numbers = [1, 4, 9, 16]                                 # قائمة أعداد
print("Sum:", sum(numbers))                              # مجموع العناصر
print("Min:", min(numbers))                              # أصغر قيمة
print("Max:", max(numbers))                              # أكبر قيمة

# الترتيب
unsorted_numbers = [8, 2, 6, 1, 9, 3]                   # قائمة غير مرتبة
unsorted_numbers.sort()                                  # ترتيب تصاعدي داخل نفس القائمة
print("Sorted ascending:", unsorted_numbers)             # عرض القائمة بعد الترتيب

unsorted_numbers.sort(reverse=True)                      # ترتيب تنازلي
print("Sorted descending:", unsorted_numbers)            # عرض الترتيب التنازلي


# ============================================================
# 5) SLICES - الشرائح
# ============================================================
print_title("5) SLICES - الشرائح")

temperatures = [18, 21, 24, 33, 39, 40, 39, 36, 30, 22, 18]  # درجات حرارة شهرية

third_quarter = temperatures[6:9]                       # استخراج العناصر من الفهرس 6 إلى 8
print("Third quarter temperatures:", third_quarter)     # عرض الجزء المستخرج

print("First six months:", temperatures[:6])            # من البداية حتى قبل الفهرس 6
print("From index 6 to end:", temperatures[6:])         # من الفهرس 6 حتى النهاية

temperatures[6:9] = [45, 44, 40]                        # استبدال جزء من القائمة
print("After slice replacement:", temperatures)         # عرض القائمة بعد التعديل


# ============================================================
# 6) LISTS AS FUNCTION PARAMETERS - القوائم كوسائط للدوال
# ============================================================
print_title("6) LISTS AS FUNCTION PARAMETERS - القوائم كوسائط للدوال")

# دالة تجمع عناصر قائمة
def sum_list(values):
    total = 0                                            # متغير لتجميع المجموع
    for element in values:                               # المرور على كل عنصر
        total += element                                 # إضافة العنصر إلى المجموع
    return total                                         # إرجاع الناتج

# دالة تعدل القائمة الأصلية نفسها
def multiply_in_place(values, factor):
    for i in range(len(values)):                         # المرور على الفهارس
        values[i] = values[i] * factor                   # تعديل كل عنصر داخل نفس القائمة

# دالة لا تغيّر الأصل، بل تعيد نسخة جديدة
def multiply_copy(values, factor):
    new_values = values.copy()                           # إنشاء نسخة مستقلة
    for i in range(len(new_values)):                     # المرور على عناصر النسخة
        new_values[i] *= factor                          # تعديل النسخة فقط
    return new_values                                    # إرجاع النسخة المعدلة

scores = [32, 54, 67.5, 29, 35]                         # قائمة درجات
print("Sum of scores:", sum_list(scores))                # استخدام دالة المجموع

multiply_in_place(scores, 10)                            # تعديل القائمة الأصلية مباشرة
print("After multiply_in_place:", scores)                # عرض التغيير

safe_scores = [1, 2, 3, 4]                               # قائمة جديدة
new_safe_scores = multiply_copy(safe_scores, 5)          # إنشاء نسخة مضروبة في 5
print("Original safe_scores:", safe_scores)              # الأصل لن يتغير
print("New multiplied copy :", new_safe_scores)          # النسخة المعدلة


# ============================================================
# 7) 2D LISTS / TABLES - الجداول ثنائية الأبعاد
# ============================================================
print_title("7) 2D LISTS / TABLES - الجداول ثنائية الأبعاد")

COUNTRIES = 8                                            # عدد الصفوف
MEDALS = 3                                               # عدد الأعمدة

# إنشاء جدول جاهز كما في المثال
counts = [
    [0, 3, 0],   # Canada
    [0, 0, 1],   # Italy
    [0, 0, 1],   # Germany
    [1, 0, 0],   # Japan
    [0, 0, 1],   # Kazakhstan
    [3, 1, 1],   # Russia
    [0, 1, 0],   # South Korea
    [1, 0, 1]    # United States
]

countries_names = [
    "Canada", "Italy", "Germany", "Japan",
    "Kazakhstan", "Russia", "South Korea", "United States"
]

medal_names = ["Gold", "Silver", "Bronze"]              # أسماء الأعمدة

# طباعة الجدول بشكل منسق
print(f"{'Country':<15} {'Gold':<8} {'Silver':<8} {'Bronze':<8}")
print("-" * 45)
for row in range(COUNTRIES):                             # المرور على الصفوف
    print(f"{countries_names[row]:<15} "
          f"{counts[row][0]:<8} "
          f"{counts[row][1]:<8} "
          f"{counts[row][2]:<8}")                        # طباعة كل صف

# الوصول إلى عنصر محدد
medal_count = counts[3][1]                               # الصف 3 العمود 1
print("\nJapan silver medals:", medal_count)             # عرض قيمة محددة

# مجموع ميداليات دولة معينة (مجموع صف)
i = 0                                                    # كندا في الصف الأول
total_canada = 0                                         # متغير للتجميع
for j in range(MEDALS):                                  # المرور على أعمدة الصف
    total_canada += counts[i][j]                         # جمع القيم
print("Total medals won by Canada:", total_canada)       # طباعة الناتج

# مجموع الميداليات الفضية عالمياً (مجموع عمود)
j = 1                                                    # العمود 1 يمثل Silver
total_silver = 0                                         # متغير للتجميع
for i in range(COUNTRIES):                               # المرور على الصفوف
    total_silver += counts[i][j]                         # جمع قيم العمود
print("Total silver medals worldwide:", total_silver)    # طباعة الناتج

# تحديد أكثر نوع ميداليات تم الفوز به
column_totals = [0] * MEDALS                             # قائمة لتخزين مجموع كل عمود
for j in range(MEDALS):                                  # المرور على الأعمدة
    for i in range(COUNTRIES):                           # المرور على الصفوف
        column_totals[j] += counts[i][j]                 # جمع كل عمود

most_won_medal = medal_names[column_totals.index(max(column_totals))]  # إيجاد اسم أكبر عمود
print("Most won medal class:", most_won_medal)           # طباعة النوع الأكثر

# إنشاء جدول كبير ديناميكياً
dynamic_rows = 4                                         # عدد صفوف جديد
dynamic_cols = 3                                         # عدد أعمدة جديد
dynamic_table = []                                       # قائمة فارغة ستصبح جدولاً

for _ in range(dynamic_rows):                            # تكرار بعدد الصفوف
    row = [0] * dynamic_cols                             # إنشاء صف مليء بالأصفار
    dynamic_table.append(row)                            # إضافة الصف للجدول

print("\nDynamically created table:")
for row in dynamic_table:                                # المرور على الصفوف
    print(row)                                           # طباعة كل صف


# ============================================================
# 8) TUPLES - الصفوف الثابتة
# ============================================================
print_title("8) TUPLES - الصفوف الثابتة")

t1 = ()                                                  # إنشاء tuple فارغ
t2 = (1, 3, 5)                                           # tuple بثلاثة عناصر
t3 = tuple([2 * x for x in range(1, 5)])                 # تحويل list إلى tuple
t4 = tuple("abac")                                       # تحويل string إلى tuple

print("t1:", t1)                                         # عرض tuple الفارغ
print("t2:", t2)                                         # عرض tuple عادي
print("t3:", t3)                                         # عرض tuple ناتج من list
print("t4:", t4)                                         # عرض tuple ناتج من string

print("Element at index 1 in t2:", t2[1])                # الوصول لعنصر داخل tuple
print("Length of t2:", len(t2))                          # عدد عناصر tuple
print("Is 3 in t2?", 3 in t2)                            # اختبار وجود عنصر

# ملاحظة تعليمية:
# tuple غير قابلة للتعديل، لذلك السطر التالي لو فُعّل سيعطي خطأ:
# t2[0] = 99


# ============================================================
# 9) SETS - المجموعات
# ============================================================
print_title("9) SETS - المجموعات")

s1 = set()                                               # إنشاء set فارغ
s2 = {1, 3, 5, 5}                                        # القيم المكررة لا تُخزن مرتين
s3 = set([1, 3, 3, 5])                                   # إنشاء set من list
s4 = set([x * 2 for x in range(1, 10)])                  # set باستخدام comprehension
s5 = set("abac")                                         # set من string

print("s1:", s1)                                         # عرض s1
print("s2:", s2)                                         # سيظهر بدون تكرار
print("s3:", s3)                                         # بدون تكرار أيضاً
print("s4:", s4)                                         # عرض عناصر مضاعفة
print("s5:", s5)                                         # أحرف فريدة فقط

# إضافة وحذف
s_example = {1, 2, 4}                                    # مجموعة أولية
s_example.add(6)                                         # إضافة عنصر
print("After add:", s_example)                           # عرض بعد الإضافة

s_example.remove(4)                                      # حذف عنصر موجود
print("After remove:", s_example)                        # عرض بعد الحذف

# دوال أساسية
print("Length:", len(s_example))                         # عدد العناصر
print("Max:", max(s_example))                            # أكبر قيمة
print("Min:", min(s_example))                            # أصغر قيمة
print("Sum:", sum(s_example))                            # مجموع العناصر
print("Is 3 in set?", 3 in s_example)                    # اختبار عضوية

# subset / superset
a = {1, 2, 4}                                            # مجموعة أولى
b = {1, 2, 4, 5, 6}                                      # مجموعة ثانية
print("a issubset b:", a.issubset(b))                    # هل a مجموعة جزئية من b؟
print("b issuperset a:", b.issuperset(a))                # هل b تحتوي a بالكامل؟

# مساواة المجموعات
print("{1,2,4} == {1,4,2} ->", {1, 2, 4} == {1, 4, 2})  # الترتيب لا يهم في sets

# عمليات المجموعات
x = {1, 2, 4}                                            # مجموعة x
y = {1, 3, 5}                                            # مجموعة y

print("Union:", x | y)                                   # الاتحاد
print("Intersection:", x & y)                            # التقاطع
print("Difference x-y:", x - y)                          # الفرق
print("Symmetric difference:", x ^ y)                    # العناصر غير المشتركة


# ============================================================
# 10) SETS VS LISTS PERFORMANCE - مقارنة الأداء
# ============================================================
print_title("10) SETS VS LISTS PERFORMANCE - مقارنة الأداء")

import time                                              # استيراد time لقياس الزمن

large_list = list(range(1_000_000))                      # إنشاء قائمة كبيرة
large_set = set(large_list)                              # تحويلها إلى set
target = 999_999                                         # العنصر المراد البحث عنه

# قياس زمن البحث في list
start_time = time.perf_counter()                         # بداية القياس
found_in_list = target in large_list                     # اختبار العضوية في list
list_time = time.perf_counter() - start_time             # الزمن المستغرق

# قياس زمن البحث في set
start_time = time.perf_counter()                         # بداية قياس جديدة
found_in_set = target in large_set                       # اختبار العضوية في set
set_time = time.perf_counter() - start_time              # الزمن المستغرق

print(f"Found in list? {found_in_list} | Time: {list_time:.8f} sec")  # نتيجة list
print(f"Found in set?  {found_in_set} | Time: {set_time:.8f} sec")    # نتيجة set

# ملاحظة:
# غالباً سيكون set أسرع في البحث لأن الوصول فيه أكثر كفاءة عند اختبار العضوية.


# ============================================================
# 11) DICTIONARIES - القواميس
# ============================================================
print_title("11) DICTIONARIES - القواميس")

student_ages = {}                                        # إنشاء قاموس فارغ
student_ages["john"] = 40                                # إضافة مدخل جديد
student_ages["peter"] = 45                               # إضافة مدخل جديد
student_ages["susan"] = 50                               # إضافة مدخل جديد

print("Dictionary after adding:", student_ages)          # عرض القاموس

student_ages["john"] = 41                                # تعديل قيمة مفتاح موجود
print("After modifying john:", student_ages)             # عرض بعد التعديل

del student_ages["susan"]                                # حذف عنصر من القاموس
print("After deleting susan:", student_ages)             # عرض بعد الحذف

# اختبار len و in
print("Length of dictionary:", len(student_ages))        # عدد الأزواج المفتاح/القيمة
print("'john' in dictionary?", "john" in student_ages)   # هل المفتاح موجود؟
print("'johnson' in dictionary?", "johnson" in student_ages)  # هل المفتاح غير موجود؟

# الدوران على القاموس
print("\nLooping through dictionary:")
for key in student_ages:                                 # المرور على المفاتيح
    print(key + " : " + str(student_ages[key]))          # طباعة المفتاح وقيمته

# بعض الدوال المهمة
print("\nKeys   :", list(student_ages.keys()))           # استخراج المفاتيح
print("Values :", list(student_ages.values()))           # استخراج القيم
print("Items  :", list(student_ages.items()))            # استخراج الأزواج (مفتاح، قيمة)

print("Get peter:", student_ages.get("peter"))           # جلب القيمة بأمان
print("Pop john :", student_ages.pop("john"))            # حذف john وإرجاع قيمته
print("After pop:", student_ages)                        # عرض القاموس بعد الحذف


# ============================================================
# 12) DICTIONARY APPLICATION - تطبيق عملي على المشتريات
# ============================================================
print_title("12) DICTIONARY APPLICATION - تطبيق عملي على المشتريات")

purchases = [
    ["Alice", "Laptop", 1200],
    ["Bob", "Smartphone", 800],
    ["Alice", "Mouse", 25],
    ["Alice", "Keyboard", 75],
    ["Bob", "Headphones", 150],
    ["Charlie", "Smartphone", 800]
]                                                        # بيانات المشتريات

# استخراج أسماء العملاء بدون تكرار باستخدام set
customers = set()                                        # مجموعة فارغة للأسماء الفريدة
for purchase in purchases:                               # المرور على كل عملية شراء
    customers.add(purchase[0])                           # إضافة اسم العميل

print("Unique customers:", customers)                    # عرض العملاء الفريدين

# حساب مجموع إنفاق كل عميل باستخدام dictionary
spending = {}                                            # قاموس لتخزين مجموع الإنفاق

for purchase in purchases:                               # المرور على البيانات
    name, item, price = purchase                         # تفكيك كل سجل إلى اسم وصنف وسعر

    if name in spending:                                 # إذا كان العميل موجوداً مسبقاً
        spending[name] += price                          # نجمع السعر على القيمة الحالية
    else:                                                # إذا لم يكن موجوداً
        spending[name] = price                           # ننشئ له قيمة أولية

print("Total spending per customer:", spending)          # عرض مجموع الإنفاق

# تحديد أغلى عملية شراء
def get_price(purchase):
    return purchase[2]                                   # ترجع السعر من سجل الشراء

most_expensive = max(purchases, key=get_price)           # إيجاد السجل ذو السعر الأكبر
print("Most expensive purchase:", most_expensive)        # عرض النتيجة

# طباعة جدول منسق
print("\nCustomer Purchases Table:")
print("{:<10} {:<15} {:<10}".format("Customer", "Item", "Price"))  # رؤوس الأعمدة
print("-" * 35)                                          # خط فاصل

for row in purchases:                                    # المرور على السجلات
    print("{:<10} {:<15} {:<10}".format(row[0], row[1], row[2]))   # طباعة منسقة


# ============================================================
# 13) OPTIONAL CASE STUDY - عدّ الكلمات
# ============================================================
print_title("13) OPTIONAL CASE STUDY - عدّ الكلمات")

text = "python is fun and python is powerful and fun"    # نص تجريبي
words = text.split()                                     # تقسيم النص إلى كلمات
word_count = {}                                          # قاموس لحفظ عدد تكرار الكلمات

for word in words:                                       # المرور على الكلمات
    if word in word_count:                               # إذا كانت الكلمة موجودة
        word_count[word] += 1                            # زيادة العداد
    else:                                                # إذا ظهرت لأول مرة
        word_count[word] = 1                             # تعيين العداد إلى 1

print("Word occurrences:")
for word in sorted(word_count.keys()):                   # ترتيب الكلمات أبجدياً
    print(f"{word:<10} -> {word_count[word]}")           # طباعة الكلمة وعددها
