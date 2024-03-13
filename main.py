from collect_link_cellphones import * 

if __name__=="__main__":
    main_url = r"https://cellphones.com.vn/mobile.html"
    base_url = r"https://cellphones.com.vn/"
    columns = ["ID", "Title", "Link"]
    current_day = dt.now().day
    current_month = dt.now().month

    driver = init_driver(main_url) # initialize the driver

    while handle_popup_83(driver):
        pass
    
    while click_show_more(driver): # continue clicking the show more button until there is no more content
        pass

    product_info = save_link_to_product(driver, base_url) # save the product's link and title to a list
    df = pd.DataFrame(product_info, columns=columns)

    data_path = f"data/products_cellphones_{current_day}_{current_month}.csv"
    
    if not os.path.exists("data"): # create a folder to store the data
        os.mkdir("data")
    df.to_csv(data_path, mode='w', encoding="utf-8") # save the data to a csv file
    
    driver.quit()

    # fun fact: takes 50 times to click the show more button to reach the end :)