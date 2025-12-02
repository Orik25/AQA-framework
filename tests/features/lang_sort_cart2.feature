Feature: Cart1
 Given I open the Rozetka home page
 When I search for 'Iphone 17'
 When I change language to 'ru'
 Then language should be 'ru'
 When I sort products by price 'asc'
 Then should sort products by price 'asc'
 When I add first item to cart
 When I open cart
 Then Cart should contains '1' items
 When I delete item from cart
 Then Cart should contains '0' items
