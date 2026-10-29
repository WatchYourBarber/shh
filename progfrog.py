# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import sys
import os


#окно авторизации
class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(340, 180)
        Login.setWindowTitle("Вход в систему")
        self.verticalLayout = QtWidgets.QVBoxLayout(Login)
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout.setSpacing(8)

        self.label_login = QtWidgets.QLabel(Login)
        self.label_login.setText("Логин:")
        self.verticalLayout.addWidget(self.label_login)

        self.lineEdit_login = QtWidgets.QLineEdit(Login)
        self.lineEdit_login.setPlaceholderText("введите логин...")
        self.verticalLayout.addWidget(self.lineEdit_login)

        self.label_info = QtWidgets.QLabel(Login)
        self.label_info.setText("(можно оставить пустым - вход как гость)")
        self.label_info.setStyleSheet("color: gray; font-size: 11px;")
        self.verticalLayout.addWidget(self.label_info)

        #кнопки входа
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.btn_ok = QtWidgets.QPushButton(Login)
        self.btn_ok.setText("Войти")
        self.btn_ok.setMinimumWidth(90)
        self.horizontalLayout.addWidget(self.btn_ok)
        self.btn_cancel = QtWidgets.QPushButton(Login)
        self.btn_cancel.setText("Отмена")
        self.btn_cancel.setMinimumWidth(90)
        self.horizontalLayout.addWidget(self.btn_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)


#диалог добавления заказа
class Ui_AddOrder(object):
    def setupUi(self, AddOrder):
        AddOrder.setObjectName("AddOrder")
        AddOrder.resize(380, 520)
        AddOrder.setWindowTitle("Новый заказ")
        self.verticalLayout = QtWidgets.QVBoxLayout(AddOrder)
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout.setSpacing(6)

        self.label1 = QtWidgets.QLabel(AddOrder)
        self.label1.setText("Номер заказа:")
        self.verticalLayout.addWidget(self.label1)
        self.edit_num = QtWidgets.QLineEdit(AddOrder)
        self.verticalLayout.addWidget(self.edit_num)

        self.label2 = QtWidgets.QLabel(AddOrder)
        self.label2.setText("Дата заказа:")
        self.verticalLayout.addWidget(self.label2)
        self.edit_date = QtWidgets.QLineEdit(AddOrder)
        self.edit_date.setPlaceholderText("дд.мм.гггг")
        self.verticalLayout.addWidget(self.edit_date)

        self.label3 = QtWidgets.QLabel(AddOrder)
        self.label3.setText("Логин:")
        self.verticalLayout.addWidget(self.label3)
        self.edit_login = QtWidgets.QLineEdit(AddOrder)
        self.verticalLayout.addWidget(self.edit_login)

        self.label4 = QtWidgets.QLabel(AddOrder)
        self.label4.setText("Категория:")
        self.verticalLayout.addWidget(self.label4)
        self.edit_cat = QtWidgets.QLineEdit(AddOrder)
        self.verticalLayout.addWidget(self.edit_cat)

        self.label5 = QtWidgets.QLabel(AddOrder)
        self.label5.setText("Наименование товара:")
        self.verticalLayout.addWidget(self.label5)
        self.edit_name = QtWidgets.QLineEdit(AddOrder)
        self.verticalLayout.addWidget(self.edit_name)

        self.label6 = QtWidgets.QLabel(AddOrder)
        self.label6.setText("ID товара:")
        self.verticalLayout.addWidget(self.label6)
        self.edit_id_tov = QtWidgets.QLineEdit(AddOrder)
        self.verticalLayout.addWidget(self.edit_id_tov)

        self.label7 = QtWidgets.QLabel(AddOrder)
        self.label7.setText("Производство:")
        self.verticalLayout.addWidget(self.label7)
        self.edit_proiz = QtWidgets.QLineEdit(AddOrder)
        self.verticalLayout.addWidget(self.edit_proiz)

        self.label8 = QtWidgets.QLabel(AddOrder)
        self.label8.setText("Размер:")
        self.verticalLayout.addWidget(self.label8)
        self.edit_size = QtWidgets.QLineEdit(AddOrder)
        self.verticalLayout.addWidget(self.edit_size)

        self.label9 = QtWidgets.QLabel(AddOrder)
        self.label9.setText("Количество:")
        self.verticalLayout.addWidget(self.label9)
        self.edit_qty = QtWidgets.QLineEdit(AddOrder)
        self.verticalLayout.addWidget(self.edit_qty)

        self.label10 = QtWidgets.QLabel(AddOrder)
        self.label10.setText("Цена за единицу:")
        self.verticalLayout.addWidget(self.label10)
        self.edit_price = QtWidgets.QLineEdit(AddOrder)
        self.verticalLayout.addWidget(self.edit_price)

        self.btn_save = QtWidgets.QPushButton(AddOrder)
        self.btn_save.setText("Сохранить")
        self.btn_save.setMinimumHeight(32)
        self.verticalLayout.addWidget(self.btn_save)


#диалог добавления товара
class Ui_AddProduct(object):
    def setupUi(self, AddProduct):
        AddProduct.setObjectName("AddProduct")
        AddProduct.resize(380, 460)
        AddProduct.setWindowTitle("Новый товар")
        self.verticalLayout = QtWidgets.QVBoxLayout(AddProduct)
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout.setSpacing(6)

        self.label1 = QtWidgets.QLabel(AddProduct)
        self.label1.setText("Категория:")
        self.verticalLayout.addWidget(self.label1)
        self.edit_cat = QtWidgets.QLineEdit(AddProduct)
        self.verticalLayout.addWidget(self.edit_cat)

        self.label2 = QtWidgets.QLabel(AddProduct)
        self.label2.setText("Подкатегория:")
        self.verticalLayout.addWidget(self.label2)
        self.edit_sub = QtWidgets.QLineEdit(AddProduct)
        self.verticalLayout.addWidget(self.edit_sub)

        self.label3 = QtWidgets.QLabel(AddProduct)
        self.label3.setText("Изображение:")
        self.verticalLayout.addWidget(self.label3)
        self.edit_img = QtWidgets.QLineEdit(AddProduct)
        self.edit_img.setPlaceholderText("имя файла картинки")
        self.verticalLayout.addWidget(self.edit_img)

        self.label4 = QtWidgets.QLabel(AddProduct)
        self.label4.setText("Наименование товара:")
        self.verticalLayout.addWidget(self.label4)
        self.edit_name = QtWidgets.QLineEdit(AddProduct)
        self.verticalLayout.addWidget(self.edit_name)

        self.label5 = QtWidgets.QLabel(AddProduct)
        self.label5.setText("Производство:")
        self.verticalLayout.addWidget(self.label5)
        self.edit_proiz = QtWidgets.QLineEdit(AddProduct)
        self.verticalLayout.addWidget(self.edit_proiz)

        self.label6 = QtWidgets.QLabel(AddProduct)
        self.label6.setText("Описание:")
        self.verticalLayout.addWidget(self.label6)
        self.edit_desc = QtWidgets.QLineEdit(AddProduct)
        self.verticalLayout.addWidget(self.edit_desc)

        self.label7 = QtWidgets.QLabel(AddProduct)
        self.label7.setText("Состав:")
        self.verticalLayout.addWidget(self.label7)
        self.edit_sostav = QtWidgets.QLineEdit(AddProduct)
        self.verticalLayout.addWidget(self.edit_sostav)

        self.label8 = QtWidgets.QLabel(AddProduct)
        self.label8.setText("Цена:")
        self.verticalLayout.addWidget(self.label8)
        self.edit_price = QtWidgets.QLineEdit(AddProduct)
        self.verticalLayout.addWidget(self.edit_price)

        self.btn_save = QtWidgets.QPushButton(AddProduct)
        self.btn_save.setText("Сохранить")
        self.btn_save.setMinimumHeight(32)
        self.verticalLayout.addWidget(self.btn_save)


#главное окно
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(8, 8, 8, 8)

        #верхняя панель
        self.horizontalLayout_top = QtWidgets.QHBoxLayout()
        self.horizontalLayout_top.setSpacing(15)

        self.label_role = QtWidgets.QLabel(self.centralwidget)
        self.label_role.setObjectName("label_role")
        self.label_role.setStyleSheet("font-weight: bold;")
        self.horizontalLayout_top.addWidget(self.label_role)

        self.label_fio = QtWidgets.QLabel(self.centralwidget)
        self.label_fio.setObjectName("label_fio")
        self.horizontalLayout_top.addWidget(self.label_fio)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_top.addItem(spacerItem)

        self.verticalLayout.addLayout(self.horizontalLayout_top)

        #таблицы
        self.horizontalLayout_tables = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tables.setSpacing(10)

        #таблица товаров
        self.products_widget = QtWidgets.QWidget(self.centralwidget)
        self.products_layout = QtWidgets.QVBoxLayout(self.products_widget)
        self.products_layout.setContentsMargins(0, 0, 0, 0)

        self.lbl_products = QtWidgets.QLabel("Товары")
        self.lbl_products.setStyleSheet("font-weight: bold; font-size: 13px;")
        self.products_layout.addWidget(self.lbl_products)

        self.tableWidget = QtWidgets.QTableWidget(self.products_widget)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        for i in range(8):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
        self.products_layout.addWidget(self.tableWidget)

        #кнопки товаров
        self.prod_btn_layout = QtWidgets.QHBoxLayout()
        self.btn_add_prod = QtWidgets.QPushButton(self.products_widget)
        self.btn_add_prod.setText("Добавить товар")
        self.prod_btn_layout.addWidget(self.btn_add_prod)
        self.btn_del_prod = QtWidgets.QPushButton(self.products_widget)
        self.btn_del_prod.setText("Удалить товар")
        self.prod_btn_layout.addWidget(self.btn_del_prod)
        self.prod_btn_layout.addStretch()
        self.products_layout.addLayout(self.prod_btn_layout)

        self.horizontalLayout_tables.addWidget(self.products_widget)

        #таблица заказов
        self.orders_widget = QtWidgets.QWidget(self.centralwidget)
        self.orders_layout = QtWidgets.QVBoxLayout(self.orders_widget)
        self.orders_layout.setContentsMargins(0, 0, 0, 0)

        self.lbl_orders = QtWidgets.QLabel("Заказы")
        self.lbl_orders.setStyleSheet("font-weight: bold; font-size: 13px;")
        self.orders_layout.addWidget(self.lbl_orders)

        self.tableOrders = QtWidgets.QTableWidget(self.orders_widget)
        self.tableOrders.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableOrders.setAlternatingRowColors(True)
        self.tableOrders.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableOrders.setObjectName("tableOrders")
        self.tableOrders.setColumnCount(11)
        self.tableOrders.setRowCount(0)
        for i in range(11):
            item = QtWidgets.QTableWidgetItem()
            self.tableOrders.setHorizontalHeaderItem(i, item)
        self.orders_layout.addWidget(self.tableOrders)

        #кнопки заказов
        self.btn_layout = QtWidgets.QHBoxLayout()
        self.btn_add = QtWidgets.QPushButton(self.orders_widget)
        self.btn_add.setText("Добавить заказ")
        self.btn_layout.addWidget(self.btn_add)
        self.btn_del = QtWidgets.QPushButton(self.orders_widget)
        self.btn_del.setText("Удалить заказ")
        self.btn_layout.addWidget(self.btn_del)
        self.btn_layout.addStretch()
        self.orders_layout.addLayout(self.btn_layout)

        self.horizontalLayout_tables.addWidget(self.orders_widget)

        self.verticalLayout.addLayout(self.horizontalLayout_tables)
        MainWindow.setCentralWidget(self.centralwidget)

        #меню
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Чудообувь - каталог"))
        #заголовки таблицы товаров
        headers_prod = ["Категория", "Подкатегория", "Изображение",
                        "Наименование товара", "Производство", "Описание", "Состав", "Цена"]
        for i, h in enumerate(headers_prod):
            self.tableWidget.horizontalHeaderItem(i).setText(_translate("MainWindow", h))
        #заголовки таблицы заказов
        headers_ord = ["id", "Номер заказа", "Дата заказа", "логин", "Категория",
                       "Наименование товара", "ID товара", "Производство",
                       "Размер", "Количество", "Цена за единицу"]
        for i, h in enumerate(headers_ord):
            self.tableOrders.horizontalHeaderItem(i).setText(_translate("MainWindow", h))
        self.label_role.setText(_translate("MainWindow", "Роль: "))
        self.label_fio.setText(_translate("MainWindow", "ФИО: "))


#проверка логина
class Login(QtWidgets.QDialog, Ui_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_ok.clicked.connect(self.check)
        self.btn_cancel.clicked.connect(self.reject)
        self.user = None
        self.lineEdit_login.returnPressed.connect(self.check)

    def check(self):
        login = self.lineEdit_login.text().strip()

        #вход как гость
        if login == "":
            self.user = ("Гость", "Гость")
            self.accept()
            return

        #поиск в БД
        conn = sqlite3.connect("чудообувь.db")
        cur = conn.cursor()
        cur.execute('SELECT "Роль", "Фамилия", "Имя", "Отчество" FROM "Пользовтели" WHERE "Логин" = ?', (login,))
        row = cur.fetchone()
        conn.close()

        if row:
            fio = f"{row[1]} {row[2]} {row[3]}"
            self.user = (row[0], fio)
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Неверный логин")


#сохранение заказа
class AddOrder(QtWidgets.QDialog, Ui_AddOrder):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_save.clicked.connect(self.save)
        self.ok = False

    def save(self):
        try:
            num = int(self.edit_num.text())
            date = self.edit_date.text().strip()
            login = self.edit_login.text().strip()
            cat = self.edit_cat.text().strip()
            name = self.edit_name.text().strip()
            id_tov = int(self.edit_id_tov.text())
            proiz = self.edit_proiz.text().strip()
            size = float(self.edit_size.text())
            qty = int(self.edit_qty.text())
            price = float(self.edit_price.text())
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Проверьте правильность заполнения полей")
            return

        conn = sqlite3.connect("чудообувь.db")
        cur = conn.cursor()
        #получение следующего id
        cur.execute('SELECT MAX(id) FROM "Заказы"')
        max_id = cur.fetchone()[0]
        new_id = 1 if max_id is None else max_id + 1

        cur.execute('INSERT INTO "Заказы" VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                    (new_id, num, date, login, cat, name, id_tov, proiz, size, qty, price))
        conn.commit()
        conn.close()
        self.ok = True
        self.accept()


#сохранение товара
class AddProduct(QtWidgets.QDialog, Ui_AddProduct):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_save.clicked.connect(self.save)
        self.ok = False

    def save(self):
        try:
            cat = self.edit_cat.text().strip()
            sub = self.edit_sub.text().strip()
            img = self.edit_img.text().strip()
            name = self.edit_name.text().strip()
            proiz = self.edit_proiz.text().strip()
            desc = self.edit_desc.text().strip()
            sostav = self.edit_sostav.text().strip()
            price = float(self.edit_price.text())
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Проверьте правильность заполнения полей")
            return

        if not name:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Наименование обязательно")
            return

        conn = sqlite3.connect("чудообувь.db")
        cur = conn.cursor()
        cur.execute('INSERT INTO "Продукты" VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                    (cat, sub, img, name, proiz, desc, sostav, price))
        conn.commit()
        conn.close()
        self.ok = True
        self.accept()


#главное окно с логикой
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, role, fio):
        super().__init__()
        self.setupUi(self)
        self.role = role
        self.label_role.setText("Роль: " + role)
        self.label_fio.setText("ФИО: " + fio)

        self.load_products()

        #доступ к товарам
        if role == "Администратор":
            self.btn_add_prod.clicked.connect(self.add_product)
            self.btn_del_prod.clicked.connect(self.del_product)
        else:
            self.btn_add_prod.hide()
            self.btn_del_prod.hide()

        #доступ к заказам
        if role in ("Менеджер", "Администратор"):
            self.load_orders()
            self.btn_add.clicked.connect(self.add_order)
            self.btn_del.clicked.connect(self.del_order)
        else:
            self.orders_widget.hide()
            self.horizontalLayout_tables.setStretch(0, 1)

    #загрузка товаров
    def load_products(self):
        conn = sqlite3.connect("чудообувь.db")
        cur = conn.cursor()
        cur.execute('SELECT * FROM "Продукты"')
        rows = cur.fetchall()
        self.tableWidget.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, val in enumerate(row):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(val) if val is not None else ""))
        conn.close()
        self.tableWidget.resizeColumnsToContents()

    #загрузка заказов
    def load_orders(self):
        conn = sqlite3.connect("чудообувь.db")
        cur = conn.cursor()
        cur.execute('SELECT * FROM "Заказы"')
        rows = cur.fetchall()
        self.tableOrders.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, val in enumerate(row):
                self.tableOrders.setItem(i, j, QtWidgets.QTableWidgetItem(str(val) if val is not None else ""))
        conn.close()
        self.tableOrders.resizeColumnsToContents()

    #добавление заказа
    def add_order(self):
        dlg = AddOrder()
        if dlg.exec_() == QtWidgets.QDialog.Accepted and dlg.ok:
            self.load_orders()

    #удаление заказа
    def del_order(self):
        row = self.tableOrders.currentRow()
        if row < 0:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Выберите заказ")
            return
        order_id = self.tableOrders.item(row, 0).text()
        reply = QtWidgets.QMessageBox.question(
            self, "Удаление",
            f"Удалить заказ id={order_id}?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )
        if reply == QtWidgets.QMessageBox.Yes:
            conn = sqlite3.connect("чудообувь.db")
            cur = conn.cursor()
            cur.execute('DELETE FROM "Заказы" WHERE id = ?', (order_id,))
            conn.commit()
            conn.close()
            self.load_orders()

    #добавление товара
    def add_product(self):
        dlg = AddProduct()
        if dlg.exec_() == QtWidgets.QDialog.Accepted and dlg.ok:
            self.load_products()

    #удаление товара
    def del_product(self):
        row = self.tableWidget.currentRow()
        if row < 0:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Выберите товар")
            return
        name = self.tableWidget.item(row, 3).text()
        reply = QtWidgets.QMessageBox.question(
            self, "Удаление",
            f"Удалить товар «{name}»?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )
        if reply == QtWidgets.QMessageBox.Yes:
            conn = sqlite3.connect("чудообувь.db")
            cur = conn.cursor()
            cur.execute('DELETE FROM "Продукты" WHERE "Наименование товара" = ?', (name,))
            conn.commit()
            conn.close()
            self.load_products()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    #иконка приложения
    icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Icon.ico")
    if os.path.exists(icon_path):
        app.setWindowIcon(QtGui.QIcon(icon_path))

    login = Login()
    if login.exec_() == QtWidgets.QDialog.Accepted:
        role, fio = login.user
        window = MainWindow(role, fio)
        if os.path.exists(icon_path):
            window.setWindowIcon(QtGui.QIcon(icon_path))
        window.show()
        sys.exit(app.exec_())
    else:
        sys.exit()
