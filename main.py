from menu import Pizza, Burger, Drinks, Menu
from restuarent import Restuarent
from users import Chef,Server,Manager,Customer
from order import Order

def main():
    menu = Menu()
    pizza_1 = Pizza('shutki Pizza',600, 'large',['shutki','capsicam'])
    menu.add_menu_item('pizza',pizza_1)
    pizza_2 = Pizza('Alu Vorta Pizza', 400 , 'Medium',['Potato','spice'])
    menu.add_menu_item('pizza',pizza_2)
    pizza_3 = Pizza('Dal Pizza', 500, 'large',['dal','spice','onion'])
    menu.add_menu_item('pizza',pizza_3 )

    burger_1 = Burger('Naga Burger',350, 'chicken',['chicken','naga spice'])
    menu.add_menu_item('burger',burger_1)
    burger_2 = Burger('Beef BUrger',450,'Beef',['goru','onion'])
    menu.add_menu_item('burger',burger_2)
    burger_3 = Burger('Mexican Burger', 550,'beef',['beef','chicken','camsicam','sauces'])
    menu.add_menu_item('burger',burger_3)


    coke = Drinks('coke',25,True)
    menu.add_menu_item('drinks',coke)
    coffee = Drinks('mocha',300,False)
    menu.add_menu_item('drinks',coffee)

    menu.show_menu()

    sai_baba = Restuarent('Sai Baba Restaurent',2000, menu)

    manager = Manager('Kala chan',159, 'kala@chan.com','kaliakur',1500,'jan 1 2020 ','core')

    sai_baba.add_employee('manager',manager)

    chef  = Chef('Kupa samsu',456,'kupa@samsu.com','jongol',1100,'jul 5 2020','kitchen',['pizza','burger','coffee'])
    sai_baba.add_employee('chef',chef)

    server_1 = Server('picchi',753,'nai@kono.com','restaurent',300,'apr 3 2020','server')

    sai_baba.add_employee('server',server_1)


    sai_baba.show_employees()

    customer_1 = Customer('shakib khan',789,'sakib@khan.com','malibag',10000)

    # customer_1 placing an order
    order_1 = Order(customer_1,[pizza_3,burger_3,burger_1,coke,pizza_3,coffee])
    customer_1.pay_for_order(order_1)
    sai_baba.add_order(order_1)

    # customer_1 paying for order
    sai_baba.receive_payment(order_1,20000,customer_1)

    print('Revenue: ', sai_baba.revenue,'balacnce: ', sai_baba.balance)

    customer_2 = Customer('dola mia',145,'dola@mia.com','banani',25000)
    order_2 = Order(customer_2,[pizza_1,pizza_2,pizza_3,burger_1,burger_2,burger_3,coffee,coffee])
    customer_2.pay_for_order(order_2)
    sai_baba.add_order(order_2)
    sai_baba.receive_payment(order_2,15000,customer_2)

    print('Revenue: ', sai_baba.revenue,'balacnce: ', sai_baba.balance)

    # pary rent
    sai_baba.pay_expense(sai_baba.rent,'Rent')

    print('after rent, revenue is: ', sai_baba.revenue, 'balace : ',sai_baba.balance,'expense',sai_baba.expense)

    sai_baba.pay_slary(chef)
    print('after salary , revenue is: ', sai_baba.revenue, 'balace : ',sai_baba.balance,'expense',sai_baba.expense)


# call the main
if __name__ == '__main__':
    main()