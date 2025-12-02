Feature: SortDesc2
 Given I open the Rozetka home page
 When I search for 'Iphone 16'
 When I sort products by price 'desc'
 Then should sort products by price 'desc'
