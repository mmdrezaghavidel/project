class User:  
    def __init__(self, username, password):  
        self.address = []  
        self.username = username  
        self.password = password  
        self.is_logged_in = False  

    def sign_up(self):  
        with open('info.txt', 'r') as inf:  
            for line in inf:  
                cs = line.rstrip().split('-')  
                if cs[0] == self.username:   
                    print('This username is already taken.')  
                    return  
        
        address = input('Enter your address: ')  
        self.address.append(address)  
        
        with open('info.txt', 'a') as inf:  
            info = f"{self.username}-{self.password}-{','.join(self.address)}\n"  
            inf.write(info)  
        
        print("Registration successful!")  

    def sign_in(self):  
        with open('info.txt', 'r') as inf:  
            for line in inf:  
                cs = line.rstrip().split('-')  
                if cs[0] == self.username and cs[1] == self.password:  
                    self.is_logged_in = True    
                    print('Welcome!')  
                    return True  
        print('Incorrect username or password.')  
        return False  

class Product:  
    def __init__(self):  
        pass  
    
    def add_item(self, name, price, inventory, detail):  
        with open('shop.txt', 'a') as sh:  
            sh.write(f"{name}-{price}-{inventory}-{detail}\n")  
    
    def show_items(self):  
        if not self._file_exists('shop.txt'):  
            print("No products available.")  
            return  
            
        with open('shop.txt', 'r') as sh:  
            for line in sh:  
                cs = line.rstrip().split('-')  
                print(f'Product Name: {cs[0]}, Price: {cs[1]}, Inventory: {cs[2]}, Details: {cs[3]}')  

    def _file_exists(self, filename):  
        """Check if the file exists."""  
        try:  
            with open(filename, 'r'):  
                return True  
        except FileNotFoundError:  
            return False  

class ShoppingCart:  
    def __init__(self):  
        self.cart_items = []  

    def add_to_cart(self, user, item_name):  
        if not user.is_logged_in:  
            print('You need to log in to purchase items.')  
            return  

        found_item = False  
        with open('shop.txt', 'r') as sh:  
            for line in sh:  
                cs = line.rstrip().split('-')  
                if cs[0].lower() == item_name.lower():  
                    found_item = True  
                    price = int(cs[1])  
                    quantity = int(input('How many of this item would you like to buy? '))  
                    inventory = int(cs[2])  
                    if quantity <= inventory:  
                        self.cart_items.append((cs[0], price, quantity))  
                        print(f"{quantity} of {cs[0]} added to the cart.")  
                    else:  
                        print('Not enough inventory.')  
                    break  

        if not found_item:  
            print("Item not found.")  

    def get_cart_summary(self):  
        if not self.cart_items:  
            print('Your shopping cart is empty.')  
            return  

        total_cost = 0 
        summary = "Your shopping cart contains:\n"    

       
        for item_name, price, quantity in self.cart_items:  
            item_cost = price * quantity    
            total_cost += item_cost    
            summary += f"{item_name}: {quantity} x {price} = {item_cost}\n"    

        summary += f"Total cost: {total_cost}"    
        print(summary)  


def main():  
    username = input("Enter username: ")  
    password = input("Enter password: ")  
    
    user = User(username, password)  
    
    user.sign_up()    
    user.sign_in()   

    product_manager = Product()  
    product_manager.add_item("Product1", "10000", "50", "Details of Product1")  
    product_manager.add_item("Product2", "20000", "30", "Details of Product2")  

    product_manager.show_items()  
    cart = ShoppingCart()  
    cart.add_to_cart(user, "Product1")  
    cart.add_to_cart(user, "Product2") 
    cart.get_cart_summary()  

if __name__ == "__main__":  
    main()