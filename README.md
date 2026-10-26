# GeO-Pad
A 3 key macropad with a pet that you can see while playing Geometry Dash or use for other things. The reason I made this is because, while playing, my wrist gets stabbed by the corners of my laptop and develops bruises so it allows users to play comfortably without hurting their wrist on laptop corners such as me and allows easy portability unlike a 60% mechanical keyboard. It includes a oled screen so you can have a little pet while raging and making stuff.
# Software
1. KiCad-I used KiCad to actually design the Schematic and the PCB itself
2. PyCharm-This is where I wrote the code for the GeO-Pad while following tutorials on youtube (first time coding)
3. Onshape- I used this to model the case and to import the model, https://cad.onshape.com/documents/ef6d16a207c5b8c174a817fd/w/876528ba5902b90e52078595/e/ea60b42722162e659b97915d?renderMode=0&uiState=6ade0d7e211ee294f06135e0
# Instructions
1.Save the standard ssd1306.py driver module to your RP2040 device via Thonny or VS Code.
2.Flash the above script as main.py to run automatically on startup.
# A.I usage
Along with the coding tutorials I watched, I used Gemini to check my code for any mistakes and I would fix it with the suggestions from Gemini. During the revision process, I used Gemini as a second set of eyes to check my connections of the board. 
## Geo-Pad – Bill of Materials

| Week | Tier | Parts funding |
| :--- | :--- | :--- |
| Week 1 | Tier 1 | $30.00 |

| Part | What it's for | Qty | Unit | Total | Vendor |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [RP2040 pro micro](https://github.com/gutierrezcortesedgar76-max/GeO-Pad/blob/main/BOM.md#https://www.aliexpress.us/item/3256806781060135.html?src=google&src=google&albch=shopping&acnt=708-803-3821&isdl=y&slnk=&plac=&mtctp=&albbt=Google_7_shopping&aff_platform=google&aff_short_key=UneMJZVf&gclsrc=aw.ds&albagn=888888&ds_e_adid=&ds_e_matchtype=&ds_e_device=c&ds_e_network=x&ds_e_product_group_id=&ds_e_product_id=en3256806781060135&ds_e_product_merchant_id=5762056048&ds_e_product_country=US&ds_e_product_language=en&ds_e_product_channel=online&ds_e_product_store_id=&ds_url_v=2&albcp=19558607238&albag=&isSmbAutoCall=false&needSmbHouyi=false&gad_source=1&gad_campaignid=19566915268&gbraid=0AAAAAD6I-hHFuM5JDl6TUJptf0ACTEZmz&gclid=CjwKCAjw25fWBhAVEiwAMopNjlyufh_ijJvVy_PywzVok832ihfuf9-1KMYrm4mJodwwldlTehrMBhoCP3MQAvD_BwE&gatewayAdapt=glo2usa) | The main brain for the project! | 1 | $2.00 | $2.00 | [Aliexpress](https://github.com/gutierrezcortesedgar76-max/GeO-Pad/blob/main/BOM.md#https://www.aliexpress.us/item/3256806781060135.html?src=google&src=google&albch=shopping&acnt=708-803-3821&isdl=y&slnk=&plac=&mtctp=&albbt=Google_7_shopping&aff_platform=google&aff_short_key=UneMJZVf&gclsrc=aw.ds&albagn=888888&ds_e_adid=&ds_e_matchtype=&ds_e_device=c&ds_e_network=x&ds_e_product_group_id=&ds_e_product_id=en3256806781060135&ds_e_product_merchant_id=5762056048&ds_e_product_country=US&ds_e_product_language=en&ds_e_product_channel=online&ds_e_product_store_id=&ds_url_v=2&albcp=19558607238&albag=&isSmbAutoCall=false&needSmbHouyi=false&gad_source=1&gad_campaignid=19566915268&gbraid=0AAAAAD6I-hHFuM5JDl6TUJptf0ACTEZmz&gclid=CjwKCAjw25fWBhAVEiwAMopNjlyufh_ijJvVy_PywzVok832ihfuf9-1KMYrm4mJodwwldlTehrMBhoCP3MQAvD_BwE&gatewayAdapt=glo2usa) |
| [DO-35 Diodes](https://github.com/gutierrezcortesedgar76-max/GeO-Pad/blob/main/BOM.md#https://www.amazon.com/1N4148-Sealed-Switching-Electronic-Silicon/dp/B0DS1JLQ1X?th=1) | DC current | 1 | $4.00 | $4.00 | [amazon](https://github.com/gutierrezcortesedgar76-max/GeO-Pad/blob/main/BOM.md#https://www.amazon.com/1N4148-Sealed-Switching-Electronic-Silicon/dp/B0DS1JLQ1X?th=1) |
| [128x64 oled screen](https://github.com/gutierrezcortesedgar76-max/GeO-Pad/blob/main/BOM.md#https://geekworm.com/products/0-96-inch-oled?srsltid=AU7gw4X4595XJoicfSWN-w5RxvtSj3fx9DkIDwHyd9mX74WIFRMzGBiPOB4) | display | 1 | $5.00 | $5.00 | [geekworm](https://github.com/gutierrezcortesedgar76-max/GeO-Pad/blob/main/BOM.md#https://geekworm.com/products/0-96-inch-oled?srsltid=AU7gw4X4595XJoicfSWN-w5RxvtSj3fx9DkIDwHyd9mX74WIFRMzGBiPOB4) |
| **Parts subtotal** | — | — | — | **$11.00** | — |
| **Tax & shipping** | — | — | — | **$0.00** | — |
| **Total** | — | — | — | **$11.00** | — |

<img width="743" height="491" alt="Screenshot 2026-10-24 234105" src="https://github.com/user-attachments/assets/48b57f6a-a0d3-48df-88fd-a8860be7b5fb" />
<img width="977" height="675" alt="Screenshot 2026-10-25 094928" src="https://github.com/user-attachments/assets/bd8573c0-2937-4784-922d-42cee71df676" />
<img width="766" height="631" alt="Screenshot 2026-10-25 094850" src="https://github.com/user-attachments/assets/a87444b8-9f7a-4ecd-a193-7096f0a1491d" />
<img width="817" height="500" alt="Screenshot 2026-10-25 094908" src="https://github.com/user-attachments/assets/56183ee8-e469-4fe9-bec5-3fa22bd82ef1" />



