from store.models import Product, Customer


class Cart():
    def __init__(self, request):
        self.session = request.session
        self.request = request

        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def __len__(self):
        return len(self.cart)
    
    def get_products(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        return products
    
    def get_quantities(self):
        quantities = self.cart
        return quantities
    
    def add(self, product_id, quantity):
        product_id = str(product_id)
        quantity = str(quantity)

        if product_id not in self.cart:
            self.cart[product_id] = int(quantity)

        self.session.modified = True

        if self.request.user.is_authenticated:
            user = Customer.objects.filter(user=self.request.user)
            cart = str(self.cart).replace("'", '"')
            
            user.update(cart=cart)

        return self.cart

    def delete(self, product_id):
        product_id = str(product_id)

        if product_id in self.cart:
            del self.cart[product_id]
        
        self.session.modified = True

        if self.request.user.is_authenticated:
            user = Customer.objects.filter(user=self.request.user)
            cart = str(self.cart).replace("'", '"')
            
            user.update(cart=cart)

        return self.cart

    def update(self, product_id, quantity):
        product_id = str(product_id)
        quantity = int(quantity)

        cart = self.cart
        cart[product_id] = quantity

        self.session.modified = True

        if self.request.user.is_authenticated:
            user = Customer.objects.filter(user=self.request.user)
            cart = str(self.cart).replace("'", '"')
            
            user.update(cart=cart)

        return self.cart
    
    def total(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart

        total = 0
        for key, value in cart.items():
            key = int(key)
            product = products.filter(id=key).first()
            if product.is_sale:
                total += product.sale_price * value
            else:
                total += product.price * value

        return total
