from src.Pages import BasePage
from src.Locators import CategoryPage


class Category(BasePage):
    def shop_by(self):
        # by store
        self.input(CategoryPage.CategoryPage.shop_input, 'London School')
        self.click(CategoryPage.CategoryPage.shop_button)
        self.click(CategoryPage.CategoryPage.shop_checkbox)

    def price_checkbox(self):
        # by price
        self.click(CategoryPage.CategoryPage.price_checkbox)

    def shop_by_colour(self):
        # shop_by_colour
        self.click(CategoryPage.CategoryPage.shop_by_colour)

    def shop_by_size(self):
        # shop_by_size
        self.click(CategoryPage.CategoryPage.shop_by_size)

    def shop_by_gender(self):
        # shop_by_gender
        self.click(CategoryPage.CategoryPage.shop_by_gender)

    def shop_by_collection(self):
        # shop_by_collection
        self.click(CategoryPage.CategoryPage.shop_by_collection)

    def shop_by_category(self):
        # shop_by_category
        self.click(CategoryPage.CategoryPage.shop_by_category)

    def shop_by_brand(self):
        # shop_by_brand
        self.click(CategoryPage.CategoryPage.shop_by_brand)

    def sort_by(self):
        # sort_by_relevance
        self.click(CategoryPage.CategoryPage.sort_by_relevance)
        # sort_by_name
        self.click(CategoryPage.CategoryPage.sort_by_name)

    def item(self):
        # pagination top
        self.click(CategoryPage.CategoryPage.pag_top)
        # pagination bottom
        self.click(CategoryPage.CategoryPage.pag_bottom)
        # pick item
        self.click(CategoryPage.CategoryPage.pick_item)
        # product_available button
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




