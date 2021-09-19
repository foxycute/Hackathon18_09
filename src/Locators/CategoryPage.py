class CategoryPage:
    shop_input = {"XPATH": "//input[@id='user_location_query']"}
    search_button = {"ID", "user_location_query_button"}
    find_stores_button = {"ID": "findStoresNearMeAjax"}
    shop_checkbox = {"XPATH": "(//span[@class='facet__list__label'])[1]"}
    price_checkbox_0 = {"XPATH": "(//input[@type='checkbox'])[52]"}
    price_checkbox_20 = {"XPATH": "(//input[@type='checkbox'])[53]"}
    price_checkbox_50 = {"XPATH": "(//input[@type='checkbox'])[54]"}
    price_checkbox_100 = {"XPATH": "(//input[@type='checkbox'])[55]"}
    price_checkbox_200 = {"XPATH": "(//input[@type='checkbox'])[56]"}
    price_checkbox_300 = {"XPATH": "(//input[@type='checkbox'])[57]"}
    price_checkbox_400 = {"XPATH": "(//input[@type='checkbox'])[58]"}
    price_checkbox_500 = {"XPATH": "(//input[@type='checkbox'])[59]"}
    price_checkbox_600 = {"XPATH": "(//input[@type='checkbox'])[60]"}
    price_checkbox_700 = {"XPATH": "(//input[@type='checkbox'])[61]"}
    shop_by_colour = {"XPATH": "(//span[@class='facet__list__label'])[63]"}
    shop_by_size = {"XPATH": "(//span[@class='facet__list__label'])[75]"}
    shop_by_gender = {"XPATH": "//a[normalize-space()='Male']"}
    shop_by_collection = {"XPATH": "//a[normalize-space()='Surf']"}
    shop_by_category = {"XPATH": "//a[normalize-space()='Clothes']"}
    shop_by_brand = {"XPATH": "//span[@class='facet__text']//a[contains(text(),'Billabong')]"}
    sort_by_selector = {"CSS_SELECTOR": "#sortOptions1"}
    pag_top = {"XPATH": "//div[@class='pagination-bar top']//a[contains(text(),'2')]"}
    pag_bottom = {"XPATH": "//div[@class='pagination-bar bottom']//a[contains(text(),'4')]"}
    pick_item = {"XPATH": "//a[@title='Plan B Youth Pant peach XL']"}
    item_price = {"XPATH": "(//div[@class='price'][normalize-space()='£56.66'])[1]"}
    product_available = {"ID": "product_3004380860"}
    add_to_cart = {"XPATH": "//form[@id='addToCartForm300438086']//button[@type='submit']"}


class ProductAvailable:
    input_city = {"ID": "locationForSearch"}
    search_button = {"ID": "pickupstore_location_search_button"}
    pickup_city = {"XPATH": "//label[@for='pickup-entry-0']//span[@class='pickup-store-info']"}
    next_page = {"CLASS_NAME": "next"}
    prev_page = {"CLASS_NAME": "prev"}
    info_button = {"CSS_SELECTOR": "a[aria - label = 'Store Details']"}
    map_button = {"CSS_SELECTOR": "a[aria-label='Map']"}
    hours_button = {"CSS_SELECTOR": "a[aria-label='Hours']"}
    minus_item = {"XPATH": "//div[@id='colorbox']//div[@class='display-details']//span[1]//button[1]"}
    plus_item = {"XPATH": "//div[@id='colorbox']//span[2]//button[1]"}
    add_to_bag = {"CSS_SELECTOR": "form[id='add_to_cart_storepickup_form'] button[type='submit']"}
    close_button = {"ID": "cboxClose"}


class Cart:
    check_out_button = {"XPATH": "//a[normalize-space()='Check Out']"}
    continue_button = {"XPATH": "//a[normalize-space()='Continue Shopping']"}
    close_button = {"ID": "cboxClose"}
