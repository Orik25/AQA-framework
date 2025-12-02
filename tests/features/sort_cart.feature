Feature: Cart1
 Given I open the Rozetka home page
 When I search for 'Iphone 17'
 When I sort products by price 'asc'
 Then should sort products by price 'asc'
 When I add first item to cart
 When I open cart
 Then Cart should contains '1' items
