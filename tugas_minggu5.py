class Account:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Saldo tidak boleh negatif!")

        self.__balance = amount

    def purchase_product(self, product):
        if self.__balance < product.price:
            raise ValueError("Saldo tidak mencukupi!")

        self.__balance -= product.price
        product.stock -= 1

        print(f"Berhasil membeli {product.name}")


class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.__price = price
        self.stock = stock

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Harga tidak boleh negatif!")

        self.__price = value

    def __str__(self):
        return f"{self.name} | Harga: Rp{self.price:,.0f} | Stok: {self.stock}"


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"{self.name} | Gaji: Rp{self.salary:,.0f}"


class Company:
    def __init__(self, name):
        self.name = name

        self.__employees = []

        self.__products = []

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.__employees.append(employee)
            print(f"Karyawan {employee.name} berhasil ditambahkan.")
        else:
            print("Input harus berupa object Employee.")

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            print(f"Produk {product.name} berhasil ditambahkan.")
        else:
            print("Input harus berupa object Product.")

    def __calculate_payroll(self):
        total = 0

        for employee in self.__employees:
            total += employee.salary

        return total

    def show_employees(self):
        print("\n=== DATA KARYAWAN ===")

        if len(self.__employees) == 0:
            print("Belum ada karyawan.")
        else:
            for employee in self.__employees:
                print(employee)

    def show_inventory(self):
        print("\n=== DATA INVENTARIS ===")

        if len(self.__products) == 0:
            print("Inventaris masih kosong.")
        else:
            for product in self.__products:
                print(product)

    def show_payroll(self):
        print("\n=== TOTAL PAYROLL ===")
        print(f"Total gaji: Rp{self.__calculate_payroll():,.0f}")


company = Company("PT Teknologi Nusantara")

employee1 = Employee("Jesica", 5000000)
employee2 = Employee("Rey", 4500000)
employee3 = Employee("Debora", 5500000)

company.add_employee(employee1)
company.add_employee(employee2)
company.add_employee(employee3)

product1 = Product("Laptop", 8000000, 10)
product2 = Product("Keyboard", 500000, 20)
product3 = Product("Mouse", 250000, 25)

company.add_product(product1)
company.add_product(product2)
company.add_product(product3)

print("\n================================")
print(f"Nama Perusahaan : {company.name}")
print("================================")

company.show_employees()
company.show_payroll()
company.show_inventory()

akun = Account(10000000)

print("\n=== TRANSAKSI PEMBELIAN ===")

try:
    akun.purchase_product(product1)
except ValueError as e:
    print(f"Error: {e}")

print(f"Saldo setelah pembelian: Rp{akun.balance:,.0f}")

company.show_inventory()