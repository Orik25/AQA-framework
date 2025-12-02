Feature: Lang2s
 Given I open the Rozetka home page
 When I search for 'Iphone 16'
 When I change language to 'ru'
 Then language should be 'ru'
 When I change language to 'ua'
 Then language should be 'ua'
