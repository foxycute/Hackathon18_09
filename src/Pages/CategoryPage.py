from src.Pages import BasePage
from src.Locators import CategoryPage


class Category(BasePage):
    def shop_by(self, text: str):
        # method search shop
        self.input(CategoryPage.CategoryPage.shop_input, value=text)
        self.click(CategoryPage.CategoryPage.search_button)

    def find_stores_near_by_me(self):
        # this method find stores near by me
        self.click(CategoryPage.CategoryPage.find_stores_button)

    def check_shop_near_by_me(self):
        # this method check first store near by me
        self.click(CategoryPage.CategoryPage.shop_checkbox)

    def shop_by_price_checkbox(self, price: str):
        # this method filter items by price
        bonds = {
            '0': CategoryPage.CategoryPage.price_checkbox_0,
            '20': CategoryPage.CategoryPage.price_checkbox_20,
            '50': CategoryPage.CategoryPage.price_checkbox_50,
            '100': CategoryPage.CategoryPage.price_checkbox_100,
            '200': CategoryPage.CategoryPage.price_checkbox_200,
            '300': CategoryPage.CategoryPage.price_checkbox_300,
            '400': CategoryPage.CategoryPage.price_checkbox_400,
            '500': CategoryPage.CategoryPage.price_checkbox_500,
            '600': CategoryPage.CategoryPage.price_checkbox_600,
            '700': CategoryPage.CategoryPage.price_checkbox_700
        }
        self.click(bonds[price])

    def shop_by_colour(self):
        # this method check black colour items
        self.click(CategoryPage.CategoryPage.shop_by_colour)

    def shop_by_size(self):
        # this method check M size items
        self.click(CategoryPage.CategoryPage.shop_by_size)

    def shop_by_gender(self):
        # this method check Male items
        self.click(CategoryPage.CategoryPage.shop_by_gender)

    def shop_by_collection(self):
        # this method choose items by Surf collection
        self.click(CategoryPage.CategoryPage.shop_by_collection)

    def shop_by_category(self):
        # this method choose category 'Clothes'
        self.click(CategoryPage.CategoryPage.shop_by_category)

    def shop_by_brand(self):
        # this method choose brand Billabong
        self.click(CategoryPage.CategoryPage.shop_by_brand)

    def sort_by_selector(self, text: str):
        # this method sort items in shop list
        self.select(selector=CategoryPage.CategoryPage.sort_by_selector, value=text)

    def check_product_item(self):
        # pagination top
        self.click(CategoryPage.CategoryPage.pag_top)
        # pagination bottom
        self.click(CategoryPage.CategoryPage.pag_bottom)
        # pick first item
        self.click(CategoryPage.CategoryPage.pick_item)
        # click product available button
        self.click(CategoryPage.CategoryPage.product_available)
        # add to cart button
        self.click(CategoryPage.CategoryPage.add_to_cart)

    def product_available(self):
        # input city
        self.input(CategoryPage.ProductAvailable.input_city, 'London')
        # click search button for searching city
        self.click(CategoryPage.ProductAvailable.search_button)
        # pickup city
        self.click(CategoryPage.ProductAvailable.pickup_city)
        # pagination
        self.click(CategoryPage.ProductAvailable.next_page)
        self.click(CategoryPage.ProductAvailable.prev_page)




