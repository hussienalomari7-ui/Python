# ==========================================================
# Chapter 9 - Object-Oriented Programming (Educational Code)
# ==========================================================
# هذا الملف التعليمي يجمع أهم أفكار الشابتر في مثال واحد واضح:
# 1) تعريف Class و Object
# 2) استخدام __init__ لبناء الكائن
# 3) استخدام self للوصول لبيانات الكائن نفسه
# 4) تغليف البيانات Encapsulation باستخدام __
# 5) استخدام getter / setter
# 6) استخدام __repr__ و __str__
# 7) استخدام __eq__ للمقارنة بين الكائنات
# 8) استخدام __add__ لتجميع الأسعار
# 9) استخدام datetime من مكتبة بايثون
# 10) التعامل مع List of Objects
# ==========================================================

from datetime import datetime   # استيراد datetime لاستخدام التاريخ والوقت الحالي


class Purchase:
    """
    هذا الكلاس يمثل عملية شراء واحدة.
    كل كائن من هذا الكلاس يحتوي على:
    - اسم الزبون
    - اسم المنتج
    - السعر
    - تاريخ إنشاء عملية الشراء
    """

    def __init__(self, customer_name, item, price):
        """
        Constructor / Initializer
        يتم استدعاؤه تلقائيًا عند إنشاء كائن جديد من الكلاس.
        """
        self.__customer_name = customer_name          # متغير خاص private لتخزين اسم الزبون
        self.__item = item                            # متغير خاص private لتخزين اسم المنتج
        self.__price = 0.0                            # تهيئة أولية للسعر بقيمة افتراضية
        self.__created_at = datetime.now()            # تخزين وقت إنشاء الكائن الحالي
        self.set_price(price)                         # استخدام setter بدل التعيين المباشر للتحقق من صحة السعر

    # =========================
    # Getters (دوال إرجاع القيم)
    # =========================

    def get_customer_name(self):
        return self.__customer_name                   # إرجاع اسم الزبون

    def get_item(self):
        return self.__item                            # إرجاع اسم المنتج

    def get_price(self):
        return self.__price                           # إرجاع السعر

    def get_created_at(self):
        return self.__created_at                      # إرجاع تاريخ ووقت إنشاء الكائن

    # =========================
    # Setters (دوال تعديل القيم)
    # =========================

    def set_customer_name(self, customer_name):
        self.__customer_name = customer_name          # تعديل اسم الزبون

    def set_item(self, item):
        self.__item = item                            # تعديل اسم المنتج

    def set_price(self, price):
        # التحقق من أن السعر ليس سالبًا
        if price >= 0:
            self.__price = float(price)               # تحويل السعر إلى float ثم تخزينه
        else:
            print("Error: price cannot be negative.") # رسالة خطأ إذا كانت القيمة غير صحيحة

    # ======================================
    # Regular methods (دوال سلوك خاصة بالكائن)
    # ======================================

    def apply_discount(self, percent):
        """
        هذه الدالة تطبق خصم بنسبة مئوية على السعر.
        مثال: إذا كانت النسبة 10 فهذا يعني خصم 10%
        """
        if 0 <= percent <= 100:                       # التحقق أن النسبة منطقية
            discount_value = self.__price * (percent / 100)   # حساب قيمة الخصم
            self.__price -= discount_value            # طرح قيمة الخصم من السعر
        else:
            print("Error: discount percent must be between 0 and 100.")

    def age_in_seconds(self):
        """
        تحسب كم ثانية مرت منذ إنشاء الكائن.
        هنا نستخدم datetime كما ورد في الشابتر.
        """
        now = datetime.now()                          # الحصول على الوقت الحالي
        diff = now - self.__created_at                # الفرق بين الوقت الحالي ووقت إنشاء الكائن
        return diff.total_seconds()                   # إرجاع الفرق بالثواني

    # ==========================================
    # Special methods (الدوال الخاصة في بايثون)
    # ==========================================

    def __str__(self):
        """
        هذه الدالة تُستدعى عند استخدام print(object)
        ونعيد نصًا مرتبًا وواضحًا للمستخدم.
        """
        return (f"Customer: {self.__customer_name}, "
                f"Item: {self.__item}, "
                f"Price: ${self.__price:.2f}")

    def __repr__(self):
        """
        تمثيل نصي أوضح للمبرمج.
        غالبًا يُستخدم أثناء الفحص أو الطباعة داخل القوائم.
        """
        return (f"Purchase(customer_name='{self.__customer_name}', "
                f"item='{self.__item}', "
                f"price={self.__price:.2f})")

    def __eq__(self, other):
        """
        مقارنة كائنين من نوع Purchase باستخدام ==
        سنعتبر عمليتي الشراء متساويتين إذا كان:
        - اسم الزبون نفسه بدون حساسية لحالة الأحرف
        - اسم المنتج نفسه بدون حساسية لحالة الأحرف
        """
        if not isinstance(other, Purchase):           # التحقق أن الكائن الآخر من نفس النوع
            return False                              # إذا لم يكن من نفس النوع فالمقارنة False

        return (
            self.__customer_name.lower() == other.__customer_name.lower() and
            self.__item.lower() == other.__item.lower()
        )                                             # إعادة نتيجة المقارنة

    def __add__(self, other):
        """
        هذه الدالة تسمح بجمع كائنين باستخدام +
        وسنعتبر أن الناتج هو مجموع السعرين.
        """
        if isinstance(other, Purchase):               # إذا كان الطرف الآخر كائن Purchase
            return self.__price + other.__price       # أرجع مجموع السعرين
        return NotImplemented                         # نخبر بايثون أن هذه العملية غير مدعومة مع هذا النوع


# ==========================================================
# كلاس إضافي لشرح مفهوم class / object / self بشكل أبسط
# ==========================================================
class Counter:
    """
    هذا الكلاس يمثل عدادًا بسيطًا.
    الفكرة منه شرح:
    - instance variable
    - self
    - methods
    """

    def __init__(self):
        self._value = 0                               # متغير خاص بعداد الكائن الحالي

    def click(self):
        self._value += 1                              # زيادة قيمة العداد بمقدار 1

    def reset(self):
        self._value = 0                               # إعادة العداد إلى الصفر

    def get_value(self):
        return self._value                            # إرجاع القيمة الحالية للعداد

    def __repr__(self):
        return f"Counter(value={self._value})"        # تمثيل نصي للكائن


# ==========================================================
# Main Program
# ==========================================================
# هنا نبدأ باستخدام الكلاسات التي أنشأناها فوق
# ==========================================================

print("========== Counter Demo ==========")

counter1 = Counter()                                  # إنشاء كائن أول من الكلاس Counter
counter2 = Counter()                                  # إنشاء كائن ثانٍ مستقل عن الأول

counter1.click()                                      # زيادة قيمة counter1 إلى 1
counter1.click()                                      # زيادة قيمة counter1 إلى 2
counter2.click()                                      # زيادة قيمة counter2 إلى 1 فقط

print("counter1 value =", counter1.get_value())       # طباعة قيمة الكائن الأول
print("counter2 value =", counter2.get_value())       # طباعة قيمة الكائن الثاني
print()                                               # سطر فارغ للتنسيق


print("========== Purchase Objects Demo ==========")

purchase1 = Purchase("Alice", "Laptop", 1200)         # إنشاء كائن شراء أول
purchase2 = Purchase("Bob", "Mouse", 25)              # إنشاء كائن شراء ثانٍ
purchase3 = Purchase("alice", "laptop", 1500)         # كائن ثالث للمقارنة مع الأول

print(purchase1)                                      # تستدعي __str__ تلقائيًا
print(repr(purchase1))                                # تستدعي __repr__ بشكل صريح
print()                                               # سطر فارغ


print("========== Getters / Setters Demo ==========")

print("Original price:", purchase2.get_price())       # قراءة السعر باستخدام getter
purchase2.set_price(30)                               # تعديل السعر باستخدام setter
print("Updated price:", purchase2.get_price())        # قراءة السعر بعد التعديل
print()                                               # سطر فارغ


print("========== Encapsulation Demo ==========")

# لا يفضل الوصول المباشر للمتغيرات الخاصة مثل:
# purchase1.__price
# لأن المتغير معرف كـ private باستخدام __
# والطريقة الصحيحة هي عبر getters و setters

print("Customer name:", purchase1.get_customer_name())  # الوصول الصحيح للبيانات
print("Item name:", purchase1.get_item())               # الوصول الصحيح للبيانات
print()                                                 # سطر فارغ


print("========== Equality Demo (__eq__) ==========")

print("purchase1 == purchase2 ?", purchase1 == purchase2)  # مقارنة بين كائنين مختلفين
print("purchase1 == purchase3 ?", purchase1 == purchase3)  # مقارنة بين كائنين متشابهين بالاسم والمنتج
print()                                                    # سطر فارغ


print("========== Add Operator Demo (__add__) ==========")

total_two_purchases = purchase1 + purchase2            # تستدعي __add__ لجمع السعرين
print("Total of purchase1 and purchase2 =", total_two_purchases)
print()                                               # سطر فارغ


print("========== Discount Demo ==========")

print("Before discount:", purchase1.get_price())       # السعر قبل الخصم
purchase1.apply_discount(10)                           # تطبيق خصم 10%
print("After discount:", purchase1.get_price())        # السعر بعد الخصم
print()                                                # سطر فارغ


print("========== Datetime Demo ==========")

print("Purchase created at:", purchase1.get_created_at())   # وقت إنشاء الكائن
print("Age in seconds:", purchase1.age_in_seconds())        # كم ثانية مرّت منذ إنشاء الكائن
print()                                                     # سطر فارغ


print("========== List of Objects Demo ==========")

purchases = [                                           # قائمة تحتوي كائنات من نوع Purchase
    purchase1,
    purchase2,
    Purchase("Charlie", "Keyboard", 75),
    Purchase("Alice", "Monitor", 300),
    Purchase("Bob", "Headphones", 150)
]

print("All purchases:")                                 # عنوان
for purchase in purchases:                              # المرور على جميع الكائنات داخل القائمة
    print(purchase)                                     # طباعة كل كائن (تستدعي __str__)
print()                                                 # سطر فارغ


print("========== Unique Customers and Items ==========")

customers = set()                                       # set لتخزين أسماء الزبائن بدون تكرار
items = set()                                           # set لتخزين أسماء المنتجات بدون تكرار

for purchase in purchases:                              # المرور على كل عملية شراء
    customers.add(purchase.get_customer_name())         # إضافة اسم الزبون إلى المجموعة
    items.add(purchase.get_item())                      # إضافة اسم المنتج إلى المجموعة

print("Unique customers:", customers)                   # عرض الزبائن بدون تكرار
print("Unique items:", items)                           # عرض المنتجات بدون تكرار
print()                                                 # سطر فارغ


print("========== User Input Demo ==========")

# يمكن فك التعليق عن الأسطر التالية لتجربة إضافة عنصر جديد من المستخدم
# customer_name = input("Enter customer name: ")        # قراءة اسم الزبون من المستخدم
# item = input("Enter item name: ")                     # قراءة اسم المنتج من المستخدم
# price = float(input("Enter item price: "))            # قراءة السعر وتحويله إلى float
# new_purchase = Purchase(customer_name, item, price)   # إنشاء كائن جديد من البيانات المدخلة
# purchases.append(new_purchase)                        # إضافة الكائن الجديد إلى القائمة
# print("New purchase added successfully!")             # رسالة نجاح


print("========== End of Program ==========")