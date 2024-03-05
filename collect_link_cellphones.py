from general_imports import *

def init_driver(url):
    service = Service(executable_path="chromedriver.exe")

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(
        service=service,
        options=options)
    
    driver.get(url)
    driver.maximize_window()

    return driver

def click_button_by_class(driver, element):
    button = driver.find_element(By.CLASS_NAME, element)
    button.click()

def move_to_element(driver, element):
    action = ActionChains(driver)
    element = driver.find_element(By.CLASS_NAME, element)
    action.move_to_element(element)
    
    action.perform()

def handle_popup(driver):
    # cancel-button-top
    # modal-close is-large
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cancel-button-top"))
        )
        click_button_by_class(driver, "cancel-button-top")
        print("Popup handled")
    except:
        return
    
def handle_popup_83(driver):
    # cancel-button-top
    # modal-close is-large
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '(//button[@aria-label="close"])[position()=2]'))
        )
        # Once the element is clickable, click on it
        element.click()
        print("Popup 83 handled")
    except:
        return False
    return True

def click_show_more(driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btn-show-more"))
        )
        click_button_by_class(driver, "btn-show-more")
        # handle_popup_83(driver)
        handle_popup(driver)
        # handle_popup(driver, "cancel-button-top")
        
        move_to_element(driver, "btn-show-more")
        handle_popup(driver) 
        # handle_popup(driver, "cancel-button-top")
    except:
        print("No more content")
        return False
    return True

def save_link_to_product(driver, base_url):
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    products = soup.find_all("div", class_ = "product-info", limit=None)
    product_info = []
    for product in products:
        # Get product's link
        relative_link = product.find("a", class_ = "product__link button__link").get("href")
        product_link = urljoin(base_url, relative_link)
        # Get product's title
        product_title = product.find("div", class_ = "product__name").find('h3').text

        product_info.append([product_title, product_link])

    return product_info