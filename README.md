English:

This Python script demonstrates how to use the Shodan API to perform a search query and retrieve a list of IP addresses matching the specified criteria. The script's purpose is to showcase the basic functionality of the Shodan API.

Replace "YOUR_SHODAN_API_KEY" with your actual Shodan API key.
Set the search_query variable to the search term or query you want to perform on Shodan. For example, "Apache".
The url variable constructs the URL for the GET request to the Shodan API, incorporating your API key and the search query.
The response variable stores the result of the GET request to the Shodan API.
The data variable parses the API response as JSON to represent its contents.
The ip_addresses list stores the IP addresses extracted from the matching results in the JSON response.
The script writes the extracted IP addresses to the ip_addresses.txt text file, with each address on a separate line.
When you run this script, it will save the IP addresses that match your specified search query to the ip_addresses.txt file. This script provides a basic example of how to use the Shodan API and can be extended for more complex searches and data processing tasks.

Türkçe:

Bu Python scripti, Shodan API'sini kullanarak belirli bir arama sorgusuyla eşleşen IP adreslerinin listesini almanın nasıl yapıldığını gösterir. Script'in amacı, Shodan API'nin temel işlevselliğini sergilemektir.

"YOUR_SHODAN_API_KEY" kısmını gerçek Shodan API anahtarınızla değiştirin.
search_query değişkenini, Shodan üzerinde gerçekleştirmek istediğiniz arama terimini veya sorguyu belirleyin. Örneğin, "Apache".
url değişkeni, Shodan API'ye yapılan GET isteğinin URL'sini oluştururken API anahtarınızı ve arama sorgusunu içerir.
response değişkeni, Shodan API'ye yapılan GET isteğinin sonucunu saklar.
data değişkeni, API yanıtını JSON olarak çözerek içeriği temsil eder.
ip_addresses listesi, JSON yanıtındaki eşleşen sonuçlardan çıkarılan IP adreslerini saklar.
Script, çıkarılan IP adreslerini her biri ayrı bir satırda olacak şekilde ip_addresses.txt metin dosyasına yazar.
Bu scripti çalıştırdığınızda, belirttiğiniz arama sorgusuyla eşleşen IP adreslerini ip_addresses.txt dosyasına kaydeder. Bu script, Shodan API'nin temel kullanımını gösteren bir örnektir ve daha karmaşık aramalar ve veri işleme işlemleri için genişletilebilir.
