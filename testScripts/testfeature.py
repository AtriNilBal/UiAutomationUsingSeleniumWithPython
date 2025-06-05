from basicweb.edge_driver_windows import EdgeWebDriver

edgeBrowserTest = EdgeWebDriver(url='https://www.amazon.in')
(edgeBrowserTest
 .launch_web_app()
 .navigate_to_userSignIn()
 .user_input_username()
 .user_input_password_and_signin()
 .search_product_in_home_search_box("OnePlus Nord 4 5G (Obsidian Midnight, 8GB RAM, 256GB Storage)")
 .check_cart()
 .add_to_cart_from_search_results()
 .check_cart())